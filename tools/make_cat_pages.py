#!/usr/bin/env python3
import json, sys, os

def _cat_files(fn, clean=False, dolist=False):
    file_list = []
    with open(fn) as f:
        j = json.load(f)

        for block in j:
            if not "cat" in block or not "category" in block:
                raise Exception("Error: Not found 'cat' or 'category' in tool block '%s'" % block)
            fname = block["cat"] + ".md"
            file_list.append(fname)

            if clean == True:
                if not os.path.exists(fname):
                    raise Exception("Error: category file does not exist: %s" % fname)
                os.remove(fname)
            elif dolist == True:
                continue
            else:
                print("Writing file: %s" % fname)
                if os.path.exists(fname):
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

def write_cat_files(fn):
    _cat_files(fn)

def clean_cat_files(fn):
    _cat_files(fn, clean=True)

def list_cat_files(fn):
    return _cat_files(fn, dolist=True)

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
    """
    args = [ sys.argv[0] ]
    print(text % args)
    exit(1)

def main():
    if len(sys.argv) < 2:
        usage()

    if sys.argv[1] == "--write":
        write_cat_files(sys.argv[2])
    elif sys.argv[1] == "--clean":
        clean_cat_files(sys.argv[2])
    elif sys.argv[1] == "--list":
        print( "\n".join( list_cat_files(sys.argv[2]) ) )

if __name__ == "__main__":
    main()
