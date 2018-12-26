#!/usr/bin/env python3
import json, sys
with open(sys.argv[1]) as f:
    j = json.load(f)

    for block in j:
        if not "cat" in block or not "category" in block:
            raise Exception("Not found 'cat' or 'category' in tool category")
        fname = block["cat"] + ".md"
        print("Writing file '%s'" % fname)

        with open(fname, "w") as d:
            text = "---\nlayout: category\ncategory: %s\n---\n" % (block["category"])
            d.write(text)
