#!/usr/bin/env python3
from bs4 import BeautifulSoup
import json, sys

data = BeautifulSoup( open(sys.argv[1]).read().encode('ascii', 'ignore'), "html.parser" )
table = {}
found=None
start_gloss = False

blah = data.body.find("div", attrs={"class": "article-info"})
for thing in blah.find_all(["h2","p"]):
    if thing.name == "h2" and thing.text == "DevOps Glossary":
        start_gloss = True
    if start_gloss == True:
        if thing.name == "p":
            rows = thing.find_all("a")
            for thing2 in rows:
                link = thing2.text
                after = thing2.next_sibling
                if after == None: continue
                after = after.strip()
                if len(after) < 1: continue
                #print("link \"%s\" after \"%s\"" % (link, after))
                table[link] = after[0].upper() + after[1:]

print( json.dumps(dict(table), indent=2, sort_keys=True) )
