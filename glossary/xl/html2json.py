#!/usr/bin/env python3
from bs4 import BeautifulSoup
import json, sys

data = BeautifulSoup( open(sys.argv[1]).read().encode('ascii', 'ignore'), "html.parser" )
table = {}

for row2 in data.body.find_all("div", attrs={"class": "az-term"}):
    desc = row2.p.text.replace('\n',' ').strip()
    table[row2.a.text] = desc[0].upper() + desc[1:]

print( json.dumps(dict(table), indent=2, sort_keys=True) )
