#!/usr/bin/env python
import json, sys, re
from tool_chest import ToolChest

def simplify(s):
    s = re.sub(r"[^\w\s]", '', s)
    s = re.sub(r"\s+", '-', s)
    return s.lower()

def html(page):
    for i, s in page.categories().items():
        print('<a href="%s">%s</a>') % (i, s)

def js(page):
    l=[]
    for t,c in page.categories().items():
        l.append({"type":t, "category":c, "cat": simplify(c) })
    print json.dumps(l)

def main():
    page = ToolChest()
    if len(sys.argv) > 1 and sys.argv[1] == "html":
        html(page)
    else:
        js(page)

if __name__ == "__main__":
    main()

