#!/usr/bin/env python3
import bookmarks_parser
import sys
import json
bookmarks = bookmarks_parser.parse(sys.argv[1])
print(json.dumps(bookmarks))
