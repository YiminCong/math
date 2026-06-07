#!/usr/bin/env python3
"""Convert the guide/glossary HTML files in this repo to GitHub-flavored Markdown."""
import re, sys, os
from html.parser import HTMLParser

VOID = {"br","img","meta","link","input","hr","col"}

class Node:
    __slots__=("tag","attrs","children","data","parent")
    def __init__(self, tag, attrs=None, parent=None):
        self.tag=tag; self.attrs=attrs or {}; self.children=[]; self.data=None; self.parent=parent
    def cls(self): return self.attrs.get("class","")
    def hascls(self,c): return c in self.cls().split()
    def text(self):
        if self.data is not None: return self.data
        return "".join(ch.text() for ch in self.children)

class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root=Node("#root"); self.cur=self.root
    def handle_starttag(self, tag, attrs):
        a={k:(v or "") for k,v in attrs}
        n=Node(tag,a,self.cur); self.cur.children.append(n)
        if tag not in VOID: self.cur=n
    def handle_startendtag(self, tag, attrs):
        a={k:(v or "") for k,v in attrs}
        self.cur.children.append(Node(tag,a,self.cur))
    def handle_endtag(self, tag):
        n=self.cur
        while n is not self.root and n.tag!=tag: n=n.parent
        if n is not self.root and n.parent is not None: self.cur=n.parent
    def handle_data(self, data):
        t=Node("#text",parent=self.cur); t.data=data; self.cur.children.append(t)

def parse(html):
    t=Tree(); t.feed(html); return t.root

def find(node, pred):
    if pred(node): return node
    for ch in node.children:
        if ch.tag=="#text": continue
        r=find(ch,pred)
        if r: return r
    return None

def findall(node, pred, out=None):
    if out is None: out=[]
    if pred(node): out.append(node)
    for ch in node.children:
        if ch.tag!="#text": findall(ch,pred,out)
    return out

# ---------- math + inline ----------
def conv_math(s):
    return (s.replace("\\[","$$").replace("\\]","$$")
             .replace("\\(","$").replace("\\)","$"))

def ws(s):  # collapse whitespace
    return re.sub(r"[ \t\r\n]+"," ",s)

def inline(node):
    """Render inline markdown for a node's content."""
    parts=[]
    for ch in node.children:
        if ch.tag=="#text":
            parts.append(conv_math(ch.data))
        elif ch.tag in ("strong","b"):
            parts.append("**"+inline(ch).strip()+"**")
        elif ch.tag in ("em","i"):
            parts.append("*"+inline(ch).strip()+"*")
        elif ch.tag=="code":
            parts.append("`"+ch.text()+"`")
        elif ch.tag=="a":
            parts.append("["+inline(ch).strip()+"]("+ch.attrs.get("href","")+")")
        elif ch.tag=="sub":
            parts.append("<sub>"+inline(ch).strip()+"</sub>")
        elif ch.tag=="sup":
            parts.append("<sup>"+inline(ch).strip()+"</sup>")
        elif ch.tag=="br":
            parts.append(" ")
        else:
            parts.append(inline(ch))
    return ws("".join(parts))

def emph(s):
    s=s.strip()
    return s if ("*" in s or not s) else "*"+s+"*"

def cellfix(s):
    # protect pipes inside math, then escape the rest, for markdown table cells
    s=re.sub(r"\$[^$]*\$", lambda m:m.group().replace("|","\\vert "), s)
    s=s.replace("|","\\|")
    return s.strip()

# ---------- block rendering ----------
def render_table(tbl):
    rows=findall(tbl, lambda n:n.tag=="tr")
    header=None; data=[]
    for tr in rows:
        cells=[c for c in tr.children if c.tag in ("th","td")]
        if not cells: continue
        is_head = any(c.tag=="th" for c in cells)
        vals=[cellfix(inline(c)) or " " for c in cells]
        if is_head and header is None: header=vals
        else: data.append(vals)
    if header is None:
        if not data: return ""
        ncol=len(data[0]); header=[" "]*ncol;
    ncol=len(header)
    out=["| "+" | ".join(header)+" |","|"+ "|".join([" --- "]*ncol)+"|"]
    for r in data:
        if len(r)<ncol: r=r+[" "]*(ncol-len(r))
        out.append("| "+" | ".join(r[:ncol])+" |")
    return "\n".join(out)+"\n"

def render_blocks(node, hlvl, out):
    """Render the block-level children of `node`."""
    for ch in node.children:
        if ch.tag=="#text":
            if ch.data.strip(): out.append(ws(conv_math(ch.data)).strip()+"\n")
            continue
        c=ch
        if c.hascls("howto") or c.hascls("secnum") or c.tag=="button":
            continue
        if c.tag=="h3":
            out.append("#"*min(hlvl+1,6)+" "+inline(c).strip()+"\n")
        elif c.tag=="h4":
            out.append("#"*min(hlvl+2,6)+" "+inline(c).strip()+"\n")
        elif c.tag=="p" and (c.hascls("intro") or c.hascls("lede")):
            out.append(emph(inline(c))+"\n")
        elif c.tag=="p":
            t=inline(c).strip()
            if t: out.append(t+"\n")
        elif c.tag=="ul":
            for li in [x for x in c.children if x.tag=="li"]:
                out.append("- "+inline(li).strip())
            out.append("")
        elif c.tag=="ol":
            render_ol(c,out)
        elif c.tag=="table":
            out.append(render_table(c))
        elif c.hascls("fcard"):
            render_fcard(c,out)
        elif c.hascls("demo"):
            render_demo(c,out)
        elif c.hascls("concept") or c.hascls("rel") or c.hascls("why"):
            render_callout(c,out)
        elif c.hascls("pillrow"):
            pills=[inline(p).strip() for p in c.children if p.tag=="span"]
            out.append(" · ".join("`"+p+"`" for p in pills if p)+"\n")
        elif c.hascls("flow"):
            out.append("> "+inline(c).strip()+"\n")
        else:
            # transparent container (map, fcards wrappers, etc.)
            render_blocks(c,hlvl,out)

def split_math_blocks(node):
    """Return (lab, list_of_display_math, note) for an fcard-like node."""
    lab=None; maths=[]; note=None
    for ch in node.children:
        if ch.tag=="#text": continue
        if ch.hascls("lab"): lab=inline(ch).strip()
        elif ch.hascls("math"): maths.append(conv_math(ch.text()))
        elif ch.hascls("note"): note=inline(ch).strip()
    return lab,maths,note

def render_fcard(c,out):
    lab,maths,note=split_math_blocks(c)
    if lab: out.append("**"+lab+"**\n")
    for m in maths:
        m=ws(m).strip()
        # ensure $$ delimiters on own lines
        m=m.strip("$").strip()
        out.append("$$"+m+"$$\n")
    if note: out.append("*"+note+"*\n")

def render_callout(c,out):
    lines=[]
    tag=None
    for ch in c.children:
        if ch.tag!="#text" and ch.hascls("tag"): tag=inline(ch).strip()
    body=[]
    for ch in c.children:
        if ch.tag=="#text":
            if ch.data.strip(): body.append(ws(conv_math(ch.data)).strip())
        elif ch.hascls("tag"):
            continue
        elif ch.tag=="p":
            body.append(inline(ch).strip())
        elif ch.tag=="ul":
            for li in [x for x in ch.children if x.tag=="li"]:
                body.append("- "+inline(li).strip())
        else:
            t=inline(ch).strip()
            if t: body.append(t)
    qlines=[]
    if tag: qlines.append("**"+tag+"**")
    for b in body:
        if b:
            if qlines: qlines.append("")
            qlines.append(b)
    out.append("\n".join("> "+l if l else ">" for l in qlines))
    out.append("")

def render_demo(c,out):
    tag=None
    for ch in c.children:
        if ch.tag!="#text" and ch.hascls("tag"): tag=inline(ch).strip()
    out.append("**"+(tag or "Demonstration")+"**\n")
    ol=find(c, lambda n:n.tag=="ol")
    if ol: render_ol(ol,out)
    for ch in c.children:
        if ch.tag!="#text" and ch.hascls("qed"):
            out.append("*"+inline(ch).strip()+"*\n")

def render_ol(ol,out):
    i=0
    for li in [x for x in ol.children if x.tag=="li"]:
        i+=1
        # separate display math (.mq) from inline text
        disp=[]; inl=[]
        for ch in li.children:
            if ch.tag!="#text" and ch.hascls("mq"):
                disp.append(conv_math(ch.text()))
            elif ch.tag=="#text":
                inl.append(conv_math(ch.data))
            else:
                # an inline element, unless it contains mq
                if find(ch, lambda n:n.tag!="#text" and n.hascls("mq")):
                    inl.append(inline(ch))  # fallback
                else:
                    inl.append(inline(ch))
        text=ws("".join(inl)).strip()
        out.append(f"{i}. {text}")
        for m in disp:
            m=ws(m).strip().strip("$").strip()
            out.append("")
            out.append("   $$"+m+"$$")
    out.append("")

# ---------- top level ----------
def doc_title(root):
    h1=find(root, lambda n:n.tag=="h1")
    return inline(h1).strip() if h1 else "Untitled"

def convert_guide(root, relback):
    out=[]
    title=doc_title(root)
    out.append("# "+title+"\n")
    lede=find(root, lambda n:n.tag=="p" and n.hascls("lede"))
    if lede: out.append(emph(inline(lede))+"\n")
    out.append(f"[← Back to all guides]({relback}README.md)\n")
    main=find(root, lambda n:n.tag=="main") or root
    has_parts = bool(findall(main, lambda n:n.hascls("part")))
    seclvl = 3 if has_parts else 2
    for ch in main.children:
        if ch.tag=="#text": continue
        if ch.hascls("part"):
            out.append("\n## "+inline(ch).strip()+"\n")
        elif ch.tag=="section":
            sid=ch.attrs.get("id","")
            if sid: out.append(f'<a id="{sid}"></a>')
            h2=find(ch, lambda n:n.tag=="h2")
            htext=inline(h2).strip() if h2 else ""
            out.append(("#"*seclvl)+" "+htext+"\n")
            # render section body, skipping the h2 we already used
            tmp=Node("section")
            tmp.children=[x for x in ch.children if not (x.tag=="h2")]
            render_blocks(tmp, seclvl, out)
        elif ch.tag=="footer":
            out.append("\n---\n")
            out.append("*"+inline(ch).strip()+"*\n")
        elif ch.tag=="header":
            continue
        else:
            render_blocks(ch, seclvl, out)
    md="\n".join(out)
    md=re.sub(r"\n{3,}","\n\n",md)
    return md.strip()+"\n"

def convert_glossary(root, relback):
    out=[]
    h1=find(root, lambda n:n.tag=="h1")
    cn=find(h1, lambda n:n.hascls("cn")) if h1 else None
    full=inline(h1).strip() if h1 else "Glossary"
    cntext=inline(cn).strip() if cn else ""
    if cntext and full.endswith(cntext):
        title=full[:-len(cntext)].strip()+" · "+cntext
    else:
        title=full
    out.append("# "+title+"\n")
    desc=find(root, lambda n:n.tag=="header")
    if desc:
        p=find(desc, lambda n:n.tag=="p")
        if p: out.append(inline(p).strip()+"\n")
    out.append(f"[← Back to all guides]({relback}README.md)\n")
    cats=findall(root, lambda n:n.tag=="section" and n.hascls("cat"))
    def cattitle(c):
        dt=c.attrs.get("data-title","")
        if dt: return dt.strip()
        return inline(find(c,lambda n:n.tag=='h2')).strip()
    out.append("**Categories:** "+" · ".join(
        f"[{cattitle(c)}](#{c.attrs.get('id','')})" for c in cats)+"\n")
    for c in cats:
        cid=c.attrs.get("id","")
        if cid: out.append(f'<a id="{cid}"></a>')
        out.append("## "+cattitle(c)+"\n")
        tbl=find(c, lambda n:n.tag=="table")
        if tbl: out.append(render_table(tbl))
    md="\n".join(out)
    md=re.sub(r"\n{3,}","\n\n",md)
    return md.strip()+"\n"

def main():
    files=sys.argv[1:]
    for f in files:
        html=open(f,encoding="utf-8").read()
        root=parse(html)
        relback="../"  # all guides live one dir deep
        is_gloss = bool(find(root, lambda n:n.attrs.get("id")=="glossary"))
        md = convert_glossary(root,relback) if is_gloss else convert_guide(root,relback)
        outp=os.path.splitext(f)[0]+".md"
        open(outp,"w",encoding="utf-8").write(md)
        print(f"{f} -> {outp}  ({md.count(chr(10))} lines)")

if __name__=="__main__":
    main()
