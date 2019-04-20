import inspect
import unittest
from old.binary_tree_SOLN import *

class BinaryTreeTest(unittest.TestCase):

    def setUp(self):
        self.tree = BinarySearchTree()

    def test_01_insert(self):
        name = inspect.currentframe().f_code.co_name
        self.assertIsNone(self.tree.insert('L'), name)

    def test_02_insert_multiple(self):
        name = inspect.currentframe().f_code.co_name
        self.assertIsNone(self.tree.insert('L'), name)
        self.assertIsNone(self.tree.insert('A'), name)
        self.assertIsNone(self.tree.insert('Z'), name)

    def test_03_delete(self):
        name = inspect.currentframe().f_code.co_name
        self.assertIsNone(self.tree.insert('L'), name)
        self.assertIsNone(self.tree.delete('L'), name)

    def test_04_delete_multiple(self):
        name = inspect.currentframe().f_code.co_name
        self.assertIsNone(self.tree.insert('L'), name)
        self.assertIsNone(self.tree.insert('A'), name)
        self.assertIsNone(self.tree.insert('Z'), name)
        self.assertIsNone(self.tree.delete('A'), name)
        self.assertIsNone(self.tree.delete('L'), name)
        self.assertIsNone(self.tree.delete('Z'), name)

    def test_05_delete_not_exit(self):
        name = inspect.currentframe().f_code.co_name
        self.assertIsNone(self.tree.delete('L'), name)

    def test_06_contains(self):
        name = inspect.currentframe().f_code.co_name
        self.tree.insert('L')
        self.assertTrue('L' in self.tree, name)

    def test_07_contains_multiple(self):
        name = inspect.currentframe().f_code.co_name
        self.tree.insert('L')
        self.tree.insert('A')
        self.tree.insert('Z')
        self.tree.insert('B')
        self.assertTrue('L' in self.tree, name)
        self.assertTrue('A' in self.tree, name)
        self.assertTrue('Z' in self.tree, name)
        self.assertTrue('B' in self.tree, name)

    def test_08_contains_false(self):
        name = inspect.currentframe().f_code.co_name
        self.tree.insert('L')
        self.tree.insert('A')
        self.tree.insert('Z')
        self.tree.insert('B')
        self.assertFalse('NN' in self.tree, name)

    def test_09_contains_empty(self):
        name = inspect.currentframe().f_code.co_name
        self.assertFalse('L' in self.tree, name)

    def test_10_contains_false_multiple_adds_removes(self):
        name = inspect.currentframe().f_code.co_name
        self.tree.insert('L')
        self.tree.insert('A')
        self.tree.insert('Z')
        self.tree.insert('B')

        self.tree.delete('L')
        self.tree.delete('A')
        self.assertFalse('L' in self.tree, name)
        self.assertFalse('A' in self.tree, name)
        self.assertTrue('Z' in self.tree, name)
        self.assertTrue('B' in self.tree, name)

    def test_11_len_empty(self):
        name = inspect.currentframe().f_code.co_name
        self.assertEqual(0, len(self.tree), name)

    def test_12_len_one(self):
        name = inspect.currentframe().f_code.co_name
        self.tree.insert('L')
        self.assertEqual(1, len(self.tree), name)

    def test_13_len(self):
        name = inspect.currentframe().f_code.co_name
        self.tree.insert('L')
        self.tree.insert('A')
        self.assertEqual(2, len(self.tree), name)
        self.tree.insert('Z')
        self.assertEqual(3, len(self.tree), name)
        self.tree.insert('B')
        self.assertEqual(4, len(self.tree), name)

    def test_14_len_delete(self):
        name = inspect.currentframe().f_code.co_name
        self.tree.insert('L')
        self.tree.insert('A')
        self.tree.insert('Z')
        self.tree.insert('B')
        self.assertEqual(4, len(self.tree), name)

        self.tree.delete('L')
        self.assertEqual(3, len(self.tree), name)
        self.tree.delete('A')
        self.assertEqual(2, len(self.tree), name)
        self.tree.delete('Z')
        self.assertEqual(1, len(self.tree), name)
        self.tree.delete('B')
        self.assertEqual(0, len(self.tree), name)

    def test_15_len_delete_duplicate(self):
        name = inspect.currentframe().f_code.co_name
        self.tree.insert('L')
        self.tree.insert('A')
        self.tree.insert('Z')
        self.tree.insert('B')
        self.assertEqual(4, len(self.tree), name)

        self.tree.delete('L')
        self.assertEqual(3, len(self.tree), name)
        self.tree.delete('L')
        self.assertEqual(3, len(self.tree), name)

    def test_16_inorder(self):
        name = inspect.currentframe().f_code.co_name
        print("=== INORDER ======================")
        self.tree.insert('L')
        self.tree.insert('A')
        self.tree.insert('B')
        self.tree.insert('Q')
        self.tree.insert('O')
        self.tree.insert('Y')
        self.tree.insert('Z')
        self.tree.traverse_inorder()

    def test_17_preorder(self):
        name = inspect.currentframe().f_code.co_name
        print("=== PREORDER ======================")

        self.tree.insert('L')
        self.tree.insert('A')
        self.tree.insert('B')
        self.tree.insert('Q')
        self.tree.insert('O')
        self.tree.insert('Y')
        self.tree.insert('Z')
        self.tree.traverse_preorder()

    def test_18_postorder(self):
        name = inspect.currentframe().f_code.co_name
        print("=== POSTORDER ======================")

        self.tree.insert('L')
        self.tree.insert('A')
        self.tree.insert('B')
        self.tree.insert('Q')
        self.tree.insert('O')
        self.tree.insert('Y')
        self.tree.insert('Z')
        self.tree.traverse_postorder()

    def test_19_max_height(self):
        name = inspect.currentframe().f_code.co_name
        self.assertEqual(0, self.tree.max_height())

    def test_20_max_height_root_only(self):
        name = inspect.currentframe().f_code.co_name
        self.tree.insert('L')
        self.assertEqual(0, self.tree.max_height())

    def test_21_max_height_one(self):
        name = inspect.currentframe().f_code.co_name
        self.tree.insert('L')
        self.tree.insert('A')
        self.assertEqual(1, self.tree.max_height())

    def test_22_max_height_multiple(self):
        name = inspect.currentframe().f_code.co_name
        self.tree.insert('L')
        self.tree.insert('A')
        self.tree.insert('B')
        self.tree.insert('Q')
        self.tree.insert('O')
        self.tree.insert('Y')
        self.tree.insert('Z')
        self.assertEqual(3, self.tree.max_height())

if __name__ == '__main__':
    unittest.main(verbosity=2)

