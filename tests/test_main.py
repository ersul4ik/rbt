import unittest

from main import RBTree, Node


class ApiUniTest(unittest.TestCase):
    def setUp(self):
        self.tree = RBTree()
