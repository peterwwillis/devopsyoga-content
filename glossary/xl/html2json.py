#!/usr/bin/env python3
from bs4 import BeautifulSoup
import json, sys

data = BeautifulSoup( open(sys.argv[1]).read().encode('ascii', 'ignore'), "html.parser" )
table = {}

for row2 in data.body.find_all("div", attrs={"class": "az-term"}):
    table[row2.a.text] = row2.p.text.replace('\n',' ').strip()

print( json.dumps(dict(table)) )
