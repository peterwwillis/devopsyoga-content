#!/usr/bin/env python
import sys, json
import time

""" Take git logs from json, output just the bits we want. """

j = json.load(sys.stdin)
mylist = []
for item in j:
    msg = item['message']
    name = item['committer']['name']
    commit = item['commit']
    date = item['committer']['date']
    tz = item['committer']['timezone']
    files = [ i[2] for i in item['changes'] ]
    # !!! WARNING !!!
    # the timezone isn't handled properly here at all.
    date_s = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date))
    # !!! WARNING !!!
    obj = {
            'name': name,
            'date': date_s,
            'msg': msg,
            'files': files,
            'commit': commit
    }
    mylist.append(obj)
json.dump(mylist, sys.stdout)
