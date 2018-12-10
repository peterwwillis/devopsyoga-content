#!/usr/bin/env python
from bs4 import BeautifulSoup

soup = None
with open('do-tool-chest.html') as f:
    soup = BeautifulSoup(f, 'html.parser')
    f.close()

body = soup.body

sections = body.find_all('section')
for section in sections:
    print "section %s\n" % section

