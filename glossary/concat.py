#!/usr/bin/env python3
import sys, json, ruamel.yaml
biglist = {}
d = { 'letters': [] }
foo = {}
for fname in sys.argv[1:]:
    with open(fname) as f:
        biglist.update(json.load(f))
for k in sorted(biglist, key=str.lower):
    firstletter = k[0].upper()
    if not firstletter in foo:
        foo[firstletter] = []
    foo[firstletter].append( { 'term': k, 'desc': biglist[k] } )
d['letters'] = [ { 'letter':letter, 'entries':foo[letter] } for letter in foo ]
ruamel.yaml.YAML().dump(d, sys.stdout)
