# keys are all the same type



class BinaryNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return "({}, {})".format(self.key, self.value)


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __setitem__(self, key, value):
        if not self.root:
            self.root = BinaryNode(key, value)
            self.size += 1
        else:
            curr = self.root
            # if curr == key, replace
            # if curr = None, create node
            done = False
            while not done:
                if curr.key == key:
                    curr.value = value
                    done = True
                elif curr.key > key:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = BinaryNode(key, value)
                        self.size += 1
                        done = True
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = BinaryNode(key, value)
                        self.size += 1
                        done = True

    def __getitem__(self, key):
        curr = self.root
        while curr is not None and curr.key != key:
            if curr.key > key:
                curr = curr.left
            else:
                curr = curr.right

        if curr:
            return curr.value
        else:
            raise KeyError

    def __contains__(self, item):
        found = False
        curr = self.root
        while curr is not None and not found:
            if item == curr.key:
                found = True
            elif item > curr.key:
                curr = curr.right
            else:
                curr = curr.left
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
        if found:           # Do nothing if item is not in the tree
            self.size -= 1
            # a) handle the case where node has 2 children
            # 1. Find node's inorder successor (leftmost right descendant) and the successor's parent
            # 2. Replace the value in the node to be deleted with its successor's value
            # 3. Delete the successor node using the strategy below (the successor node only at most 1 child)
            if node.left is not None and node.right is not None:
                successor, succ_parent = self._find_inorder_successor(node)
                node.key, node.value = successor.key, successor.value
                node = successor
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


# __ iter__
# keys
# values
# items


if __name__ == '__main__':
    main()