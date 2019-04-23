# keys are all the same type


class TreeNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return "({}, {})".format(self.key, self.value)

    # def __iter__(self):
    #     if self:
    #         if self.left:
    #             for elem in self.left:
    #                 yield elem
    #         yield self
    #         if self.right:
    #             for elem in self.right:
    #                 yield elem


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    # def __iter__(self):
    #     for elem in self.root:
    #         yield elem

    def __len__(self):
        return self.size

    def insert(self, curr, key, value):
        if curr.key == key:
            curr.value = value
        elif curr.key > key:
            if curr.left:
                self.insert(curr.left, key, value)
            else:
                curr.left = TreeNode(key, value)
                self.size += 1
        else:
            if curr.right:
                self.insert(curr.right, key, value)
            else:
                curr.right = TreeNode(key, value)
                self.size += 1

    def __setitem__(self, key, value):
        if not self.root:
            self.root = TreeNode(key, value)
            self.size += 1
        else:
            self.insert(self.root, key, value)

    # def find(self, curr, key):
    #     if not curr:
    #         raise KeyError
    #     elif curr.key == key:
    #         return curr
    #     elif key < curr.key:
    #         return self.find(curr.left, key)
    #     else:
    #         return self.find(curr.right, key)

    def __getitem__(self, key):
        # return self.find(self.root, key).value
        found, curr, parent = self._locate_node(key)
        if found:
            return curr.value
        else:
            raise KeyError

    def __contains__(self, item):
        found, curr, parent = self._locate_node(item)
        return found

    def _locate_node(self, key):
        found = False
        curr = self.root
        parent = None
        while curr is not None and not found:
            if key == curr.key:
                found = True
            elif key > curr.key:
                parent = curr
                curr = curr.right
            else:
                parent = curr
                curr = curr.left
        return found, curr, parent

    # precondition: this method is only called on a node with left and right child
    def _find_inorder_successor(self, node):
        curr = node.right
        parent = node
        while curr.left is not None:
            parent = curr
            curr = curr.left
        return curr, parent

    def __delitem__(self, key):
        # 1. First, we need to find the leaf we want to delete. We must also keep track of the parent.
        found, node, parent = self._locate_node(key)
        if found:  # Do nothing if item is not in the tree
            self.size -= 1
            # a) handle the case where node has 2 children
            # 1. Find node's inorder successor (leftmost right descendant) and the successor's parent
            # 2. Replace the value in the node to be deleted with its successor's value
            # 3. Delete the successor node using the strategy below (the successor node only at most 1 child)
            if node.left is not None and node.right is not None:
                successor, succ_parent = self._find_inorder_successor(node)
                node.key, node.value = successor.key, successor.value
                node = successor
                parent = succ_parent

            # b) handle deleting leaf or node with 1 child
            # 1. Select the target node’s non-empty subtree (if one exits)
            # 2. if target node is the root, then root = subtree
            # 3. else; replace parent’s reference to target node with the subtree (adoption)
            if node.left is None:
                subtree = node.right
            else:
                subtree = node.left
            if parent is None:
                self.root = subtree
            elif parent.left == node:
                parent.left = subtree
            else:
                parent.right = subtree

    def traverse_inorder(self, node=None):
        if self.root is None:
            return

        curr = node
        if node is None:
            curr = self.root

        if curr.left is not None:
            self.traverse_inorder(curr.left)
        print(curr)
        if curr.right is not None:
            self.traverse_inorder(curr.right)

    def traverse_preorder(self, node=None):
        if self.root is None:
            return

        curr = node
        if node is None:
            curr = self.root

        print(curr)
        if curr.left:
            self.traverse_preorder(curr.left)
        if curr.right:
            self.traverse_preorder(curr.right)

    def traverse_postorder(self, node=None):
        if self.root is None:
            return

        curr = node
        if node is None:
            curr = self.root

        if curr.left:
            self.traverse_postorder(curr.left)
        if curr.right:
            self.traverse_postorder(curr.right)
        print(curr)

    def keys(self, node=None, a_list=None):
        if self.root is None:
            return []

        curr = node
        if node is None:
            curr = self.root
            a_list = []

        if curr.left is not None:
            self.keys(curr.left, a_list)
        a_list.append(curr.key)
        if curr.right is not None:
            self.keys(curr.right, a_list)

        return a_list

    def values(self, node=None, a_list=None):
        if self.root is None:
            return []

        curr = node
        if node is None:
            curr = self.root
            a_list = []

        if curr.left is not None:
            self.values(curr.left, a_list)
        a_list.append(curr.value)
        if curr.right is not None:
            self.values(curr.right, a_list)

        return a_list

    def depth(self, node, depth=0):
        if not node:
            return 0
        elif not node.left and not node.right:
            return depth
        else:
            lheight = self.depth(node.left, depth + 1)
            rheight = self.depth(node.right, depth + 1)
            if lheight > rheight:
                return lheight
            else:
                return rheight

    def height(self):
        if self.root is None:
            raise ValueError

        return self.depth(self.root)


def main():
    # You may comment out the calls to the test_xxx() functions to reduce
    # the amount printed to the screen as you progress. Uncomment them when you are ready to test.

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


if __name__ == '__main__':
    main()
