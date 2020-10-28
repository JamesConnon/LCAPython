

import unittest
import LCAPython

class LCAPythonTest(unittest.TestCase):

    def test_emptyTree(self):
        self.assertEqual(LCAPython.findLCA(None, None, None), None)

    def test_tree(self):
        self.assertEqual(LCAPython.findLCA(LCAPython.root, 2, 3).key, 1)

    def test_leftTree(self):
        self.assertEqual(LCAPython.findLCA(LCAPython.root, 4, 5).key, 2)

    def test_rightTree(self):
        self.assertEqual(LCAPython.findLCA(LCAPython.root, 6, 7).key, 3)

    def test_sameNode(self):
        self.assertEqual(LCAPython.findLCA(LCAPython.root, 1, 1).key, 1)

    def test_sameLine(self):
        self.assertEqual(LCAPython.findLCA(LCAPython.root, 2, 4).key, 2)



