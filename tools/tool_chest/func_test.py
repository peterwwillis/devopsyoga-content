#!/usr/bin/env python
import sys
if sys.version_info < (3, 5):
    raise Exception("Error: must use python 3.5 or greater")

import unittest
from subprocess import run

class TestToolChestCmdLine(unittest.TestCase):
    tool_chest_py = "./tool_chest.py"
    def test_tools(self):
        cp = run( [ self.tool_chest_py, "--tools" ] )
        self.assertEqual(cp.returncode, 0)
    def test_categories(self):
        cp = run( [ self.tool_chest_py, "--categories" ] )
        self.assertEqual(cp.returncode, 0)
    def test_categories_more(self):
        cp = run( [ self.tool_chest_py, "--categories-more" ] )
        self.assertEqual(cp.returncode, 0)

if __name__ == "__main__":
    unittest.main()
