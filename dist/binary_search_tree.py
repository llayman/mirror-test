# ==========================================================================
# PROGRAM:... ....... Assignment 8
# AUTHOR:............ <LastName>, <FirstName>
# COURSE:............ CSC 231 003
# TERM:.............. Spring 2019
# ==========================================================================


class TreeNode:
    """
    Do not change any existing code in the TreeNode class.
    """
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return "({}, {})".format(self.key, self.value)


class TreeMap:
    """
    The TreeMap data type implements the Map ADT (like a Python dictionary), e.g., tree[850123456]='Mike'
    The data structure is a binary search tree. Each node in the tree (a TreeNode) contains a key and a value.
    The keys are used to organize the tree. Examine the TreeNode's keys when inserting, searching, deleting, etc.,
    The values in each TreeNode are the data associated with the keys.
    """

    def __init__(self):
        self.root = None

    def __len__(self):
        """
        :return: the number of nodes in the TreeMap. This algorithm must have a O(1) implementation.
        """
        raise NotImplementedError

    def insert(self, curr, key, value):
        """
        Insert data into the TreeMap. This method must be recursive.
        When the key to insert already exists in the TreeMap, replace the existing TreeNode's value with 'value'.
        """
        raise NotImplementedError

    def __setitem__(self, key, value):
        """
        Support a call of the form tree[850123456]='Mike'. Make a call to the insert() method to do the actual
        insert. Also, handle the special case where the TreeMap is empty.
        """
        raise NotImplementedError

    def find(self, curr, key):
        """
        Find the key in the TreeMap and return its associated value. This method must be recursive.
        Raise a KeyError if the key is not in the TreeMap.
        """
        raise NotImplementedError

    def __getitem__(self, key):
        """
        Support a call of the form 'x = tree[850123456]'. Make a call to the find() method to do the work.
        Raise a KeyError if the tree is empty.
        """
        raise NotImplementedError

    def __contains__(self, item):
        """
        Support a call of the form 'x in tree'. Return True if x is a key in the tree, False otherwise.
        """
        raise NotImplementedError

    def _locate_node(self, key):
        """
        Find a node in the TreeMap based on the key. The method DOES NOT need to be recursive.
        Return three values:
        - found: True if the key was found in the TreeMap, False otherwise.
        - curr: the TreeNode containing the key
        - parent: the parent of the TreeNode containing the key
        :param key:
        :return:
        """
        found = False
        curr = self.root
        parent = None
        # Delete the following line and complete the method.
        raise NotImplementedError

        return found, curr, parent

    def _find_inorder_successor(self, node):
        """
        Return the in-order successor of a node, i.e., the node's leftmost right descendent. This method should ONLY
        be called on a node with both a left and a right child.
        Return the entire TreeNode object.
        """
        raise NotImplementedError

    def __delitem__(self, key):
        """
        Support a call of the form 'del tree[850123456]'. Remove the node containing the key per the procedure
        discussed in class for deleting nodes from a BST.
        - Raise a KeyError if the key is not in the TreeMap.
        - You will need to use the _locate_node() and _find_inorder_successor() supporting methods.
        """
        raise NotImplementedError

    def traverse_inorder(self, node=None):
        """
        Perform an in-order traversal of the TreeMap to print each TreeNode. Note that __str__ is already defined
        for TreeNodes.
        - Do not print anything if the TreeMap is empty.
        """
        raise NotImplementedError

    def traverse_preorder(self, node=None):
        """
        Perform a preorder traversal of the TreeMap to print each TreeNode. Do not print anything if the TreeMap is empty.
        """
        raise NotImplementedError

    def traverse_postorder(self, node=None):
        """
        Perform a postorder traversal of the TreeMap to print each TreeNode. Do not print anything if the TreeMap is empty.
        """
        raise NotImplementedError

    def keys(self, node=None, a_list=None):
        """
        Return a list of the keys in the TreeMap. Return an empty list if the TreeMap is empty.
        This method must be recursive.
        """
        raise NotImplementedError

    def values(self, node=None, a_list=None):
        """
        Return a list of the values in the TreeMap. Return an empty list if the TreeMap is empty.
        This method must be recursive.
        """
        raise NotImplementedError

    def height(self):
        """
        Return the height of the tree. Raise a ValueError if the TreeMap is empty.
        You may find it useful to implement a helper method that is recursive.
        """
        raise NotImplementedError

    def find_min(self):
        """
        Return the minimum key in the tree. Raise a ValueError if the TreeMap is empty.
        """
        raise NotImplementedError

    def find_max(self):
        """
        Return the maximum key in the tree. Raise a ValueError if the TreeMap is empty.
        """
        raise NotImplementedError


def main():
    # You may comment out the calls to the test_xxx() functions to reduce the amount printed to the screen as you work.
    # Uncomment them when you are ready to test.

    # You may add other code here to help you test and debug your code as you see fit.

    from binary_search_tree_tests import TestSuite
    import sys
    suite = TestSuite(sys.modules[__name__])
    suite.test_01_constructor()
    suite.test_02_setitem_doesnt_explode()
    suite.test_03_getitem_keyerrors()
    suite.test_04_setitem_and_getitem()
    suite.test_05_len()
    suite.test_06_contains()
    suite.test_07_delitem()
    suite.test_08_inorder_traversal()
    suite.test_09_preorder_traversal()
    suite.test_10_postorder_traversal()
    suite.test_11_keys()
    suite.test_12_values()
    suite.test_13_height()
    suite.test_14_find_min()
    suite.test_15_find_max()


if __name__ == '__main__':
    main()
