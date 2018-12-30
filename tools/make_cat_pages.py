#!/usr/bin/env python3
import json, sys, os

class CatFiles(object):

    force = 0
    clean_f=None
    write_f=None
    list_f=None

    def __init__(self, args=None):
        if args != None: self.opts(args)

    def _cat_files(self, fn, clean=False, dolist=False):
        file_list = []
        with open(fn) as f:
            j = json.load(f)

            for block in j:
                if not self.force and (not "cat" in block or not "category" in block):
                    raise Exception("Error: Not found 'cat' or 'category' in tool block '%s'" % block)
                fname = block["cat"] + ".md"
                file_list.append(fname)

                if clean == True:
                    if not self.force and not os.path.exists(fname):
                        raise Exception("Error: category file does not exist: %s" % fname)
                    if os.path.exists(fname):
                        print("Removing file: %s" % fname)
                        os.remove(fname)
                elif dolist == True:
                    continue
                else:
                    print("Writing file: %s" % fname)
                    if not self.force and os.path.exists(fname):
                        raise Exception("Error: category file exists: %s" % fname)
                    with open(fname, "w") as d:
                        text = """---
layout: tool_category
cat: %s
category: %s
categories: %s
title: DevOps %s Tools
---
This is content about %s tools.""" % ( block["cat"], block["category"], block["category"], block["category"], block["category"] )
                        d.write(text)

        return file_list

    def write_cat_files(self):
        if self.write_f: self._cat_files(self.write_f)

    def clean_cat_files(self):
        if self.clean_f: self._cat_files(self.clean_f, clean=True)

    def list_cat_files(self):
        if self.list_f:
            o = self._cat_files(self.list_f, dolist=True)
            print( "\n".join( o ) )
            return o

    def opts(self, args):
        a = enumerate(args)
        for c, item in a:
            if item == "--force":
                self.force = 1
            elif item == "--write":
                self.write_f = next(a)[1]
            elif item == "--clean":
                self.clean_f = next(a)[1]
            elif item == "--list":
                self.list_f = next(a)[1]
            else:
                raise Exception("Unknown arg '%s'" % item)

def usage():
    text = """Usage: %s [OPTIONS]...
    Writes categories sourced from tool_list.json

    Options:
      --write JSON
                        Writes new default markdown files based on categories
                        in the JSON file.
      --clean JSON
                        Removes markdown files based on categories in the JSON
                        file.	
      --list JSON
                        Lists markdown files based on categories in JSON file.
      --force
                        Try to force an operation.
    """
    args = [ sys.argv[0] ]
    print(text % args)
    exit(1)

   

def main():
    if len(sys.argv) < 2:
        usage()

    o = CatFiles(sys.argv[1:])
    o.clean_cat_files()
    o.write_cat_files()
    o.list_cat_files()

if __name__ == "__main__":
    main()
