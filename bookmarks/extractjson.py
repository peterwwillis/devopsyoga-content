#!/usr/bin/env python3
import sys, json

class Find(object):
    """ Look for nested structures and return them """
    def __init__(self, d):
        self._data = d
        self._dict_match = None
    def walk_list(self, l):
        for i in l:
            r = self.walk(i)
            if r != None: return r
        return None
    def walk_dict(self, d):
        if self._dict_match: # look for a dict with elements matching self._dict_match
            c=0
            for k in self._dict_match:
                if k in d and self._dict_match[k] == d[k]: c = c+1
            if c == self._dict_match_l: # match
                return d
        for k,v in d.items():
            r = self.walk(v)
            if r != None: return r
        return None
    def walk(self, i):
        r=None
        if isinstance(i, list):
            r = self.walk_list(i)
        elif isinstance(i, dict):
            r = self.walk_dict(i)
        else:
            #if isinstance(i, str):
            #    print("string <%s>" % i)
            pass
        if r != None: return r

    def find_folder(self, name):
        self._dict_match = { 'type': 'folder', 'title': name }
        self._dict_match_l = len(self._dict_match)
        return self.walk(self._data)

def exclude_items(dct):
    for i in excluded:
        if isinstance(i, str):
            if i in dct:
                del dct[i]
        elif isinstance(i, dict):
            for k, v in i.items():
                if k in dct and dct[k] == v:
                    del dct[k]
    return dct


global excluded
excluded = ['icon', 'add_date', {'type': 'bookmark'}]

with open(sys.argv[1]) as f:
    data = json.loads( f.read(), object_hook=exclude_items )

o = Find(data)
res = o.find_folder(sys.argv[2])

print(json.dumps(res, indent=2, sort_keys=True))
