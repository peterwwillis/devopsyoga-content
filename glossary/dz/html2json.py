#!/usr/bin/env python3
#from bs4 import BeautifulSoup
from bs4 import BeautifulSoup, NavigableString
import json, sys

def recurse_thing(obj):
    if obj.next_sibling != None:
        blah = obj.next_sibling
        print("Found next sibling '%s'" % blah)
        recurse_thing(blah)

class GlossaryList(object):
    def __init__(self):
        self.categories = {}
        self.flip = 0
        self.name, self.desc = None, None
    def set_category(self, text):
        self.category = text
        self.categories[self.category] = []
    def add_name(self, text):
        self.name = text
        self.flip = 1
    def add_desc(self, text):
        self.desc = text
        self.add_item()
        self.flip = 0
    def add_item(self):
        self.categories[self.category].append( {'name': self.name, 'description': self.desc } )
    def add(self, text):
        if self.flip == 0: self.add_name(text)
        elif self.flip == 1: self.add_desc(text)

data = BeautifulSoup( open(sys.argv[1]).read().encode('ascii', 'ignore'), "html.parser" )
table = {}
found=None
start_gloss = False

glosslist = GlossaryList()

start = data.body.find("div", attrs={"class": ['section-inner','sectionLayout--insetColumn']})
for thing in start.find_all(["h3","p"]):
    if thing.name == "h3" and "devops terms you need to know" in thing.text.lower():
        #print("Found start of list")
        start_gloss = True
        continue
    if start_gloss == True:
        if thing.name == "h3":
            glosslist.set_category(thing.text)
        if thing.name == "p":
            for text in thing.find_all(text=True, recursive=True):
                glosslist.add(text)

table = {}
for cat, a in glosslist.categories.items():
    for h in a:
        table[ h['name'] ] = h[ 'description' ]

print( json.dumps(dict(table)) )
