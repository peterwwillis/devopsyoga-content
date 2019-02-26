#!/usr/bin/env python
import sys, json

md_begin = """
# Changes %(first)i-%(last)i:
"""

md_template = """
 - <a href="https://github.com/peterwwillis/devopsyoga-content/commit/%(commit)s">**%(date)s** (%(name)s)</a> . . *("%(msg)s")* *(%(files)s)*
"""

md_end = """
"""

class Paginate:
    paginate_lim = 10
    paginate_per = 50
    results = []
    def __init__(self, fname, dname, prefix):
        self.fname = fname
        self.dname = dname
        self.prefix = prefix

    def print_page(self, j, c):
        items = j[c:(c+self.paginate_per)]
        items_len = len(items)

        fname = self.dname + "/" + self.prefix + "-%i.md" % (c)
        with open(fname,'w') as f:
            tmp = { 'first': c, 'last': c+items_len }
            f.write(md_begin % tmp)

            for item in items:
                if 'files' in item:
                    # Only use the first line of the commit message
                    item['msg'] = item['msg'].splitlines()[0]
                    # Turn the file list into "`filename`, `filename`"
                    item['files'] = ", ".join( [ "`"+i+"`" for i in item['files'] ] )
                f.write(md_template % item)

            f.write(md_end)

        return c + items_len

    def gen_pages(self):
        with open(self.fname) as f:
            j = json.load(f)
            if len(j) > self.paginate_lim:
                c = self.paginate_lim + 1
                while c < len(j):
                    c = self.print_page(j, c)


if __name__ == "__main__":
    P = Paginate(sys.argv[1], sys.argv[2], sys.argv[3])
    P.gen_pages()

