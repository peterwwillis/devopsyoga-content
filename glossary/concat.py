#!/usr/bin/env python3
import sys, json, ruamel.yaml
biglist = {}
d = { 'letters': {} }
for fname in sys.argv[1:]:
    with open(fname) as f:
        biglist.update(json.load(f))
for k in sorted(biglist, key=str.lower):
    firstletter = k[0].upper()
    if not firstletter in d['letters']:
        d['letters'][firstletter] = []
    d['letters'][firstletter].append( { 'term': k, 'desc': biglist[k] } )
ruamel.yaml.YAML().dump(d, sys.stdout)
