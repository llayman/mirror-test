class BinaryNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        raddr = laddr = None
        if self.left:
            laddr = "BinaryNode at " + hex(id(self.left))
        if self.right:
            raddr = "BinaryNode at " + hex(id(self.right))
        return "<BinaryNode at {}, data: {}, left: {}, right: {}>".format(hex(id(self)), self.data, laddr, raddr)


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self._height = 0

    def insert(self, item):

        if self.root is None:
            self.root = BinaryNode(item)
            self.size += 1
        else:
            curr = self.root
            height = 0

            # 1. Handle duplicates
            # 2. implement it recursively
            done = False
            while not done:
                height += 1
                if item < curr.data:
                    if curr.left is None:
                        curr.left = BinaryNode(item)
                        done = True
                        self.size += 1
                    else:
                        curr = curr.left
                elif item > curr.data:
                    if curr.right is None:
                        curr.right = BinaryNode(item)
                        self.size += 1
                        done = True
                    else:
                        curr = curr.right
                else:
                    print('Value is already in the tree!')
                    done = True
            if height > self._height:
                self._height = height

    def max_height(self):
        return self._height

    def _locate_node(self, item):
        found = False
        curr = self.root
        parent = None
        while curr is not None and not found:
            if item == curr.data:
                found = True
            elif item > curr.data:
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

    def delete(self, item):
        # 1. First, we need to find the leaf we want to delete. We must also keep track of the parent.
        found, node, parent = self._locate_node(item)
        if found:  # Do nothing if item is not in the tree
            self.size -= 1
            # a) handle the case where node has 2 children
            # 1. Find node's inorder successor (leftmost right descendant) and the successor's parent
            # 2. Replace the value in the node to be deleted with its successor's value
            # 3. Delete the successor node using the strategy below (the successor node only at most 1 child)
            if node.left is not None and node.right is not None:
                successor, succ_parent = self._find_inorder_successor(node)
                node.data = successor.data
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

    def __len__(self):
        return self.size

    def __contains__(self, item):
        found = False
        curr = self.root
        while curr is not None and not found:
            if item == curr.data:
                found = True
            elif item > curr.data:
                curr = curr.right
            else:
                curr = curr.left
        return found

    def traverse_inorder(self, node=None):
        curr = node
        if node is None:
            curr = self.root

        if curr.left is not None:
            self.traverse_inorder(curr.left)
        print(curr)
        if curr.right is not None:
            self.traverse_inorder(curr.right)

    def traverse_preorder(self, node=None):
        curr = node
        if node is None:
            curr = self.root

        print(curr)
        if curr.left:
            self.traverse_preorder(curr.left)
        if curr.right:
            self.traverse_preorder(curr.right)

    def traverse_postorder(self, node=None):
        curr = node
        if node is None:
            curr = self.root

        if curr.left:
            self.traverse_postorder(curr.left)
        if curr.right:
            self.traverse_postorder(curr.right)
        print(curr)


if __name__ == "__main__":
    tree = BinarySearchTree()

    tree.insert('L')
    tree.insert('F')
    tree.insert('C')
    tree.insert('G')
    tree.insert('B')
    tree.insert('E')
    tree.insert('R')
    tree.insert('O')
    tree.insert('Z')
    tree.insert('Q')
    tree.insert('P')
    tree.traverse_inorder()
    # tree.delete('E')
    tree.traverse_preorder()
