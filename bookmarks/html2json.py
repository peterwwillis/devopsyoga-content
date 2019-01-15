#!/usr/bin/env python3
#from bs4 import BeautifulSoup
from bs4 import BeautifulSoup, NavigableString
import json, sys
import re

def log(arg):
    sys.stderr.write(arg + "\n")

class BookmarksList(object):
    def __init__(self):
        self.category = None
        self.categories = {}
        self.flip = 0
        self.k, self.v = None, None
    def set_category(self, text):
        self.category = text
        self.categories[self.category] = []
        log("Set category '%s'" % self.category)
    def add_k(self, text):
        self.k = text
        self.flip = 1
    def add_v(self, text):
        self.v = text
        self.add_item()
        self.flip = 0
    def add_item(self):
        self.categories[self.category].append( {'url': self.k, 'title': self.v } )
    def add(self, text):
        log("Adding '%s'" % text)
        if self.flip == 0: self.add_k(text)
        elif self.flip == 1: self.add_v(text)

data = BeautifulSoup( open(sys.argv[1]).read().encode('ascii', 'ignore'), "html.parser" )
table = {}
found=None

bookslist = BookmarksList()

start = data.find("h3", text=re.compile('^DevOps$') )
log("Start '%s'" % start)
bookslist.set_category(start.text)
hmm = start.parent
for thing in hmm.find_all(["h3","a"], text=True, recursive=True):
    if thing.name == "h3":
        log("FOUND H3")
        bookslist.set_category(thing.text)
    if thing.name == "a":
        bookslist.add(thing['href'])
        bookslist.add(thing.text)
        #log("Found a '%s', href '%s' text '%s'" % (thing, thing['href'], thing.text))
        #bookslist.add(thing.href)

table = bookslist.categories

print( json.dumps(dict(table)) )
