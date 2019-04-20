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

    def insert(self, item):
        if self.root is None:
            self.root = BinaryNode(item)
        else:
            curr = self.root
            done = False
            while not done:
                if item < curr.data:
                    if curr.left is None:
                        curr.left = BinaryNode(item)
                        done = True
                    else:
                        curr = curr.left
                elif item > curr.data:
                    if curr.right is None:
                        curr.right = BinaryNode(item)
                        done = True
                    else:
                        curr = curr.right
                else:
                    print('Value is already in the tree!')
                    done = True

    def traverse_inorder(self, node=None):
        curr = node
        if node is None:
            curr = self.root

        if curr.left is not None:
            self.traverse_inorder(curr.left)
        print(curr)
        if curr.right is not None:
            self.traverse_inorder(curr.right)

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

    # precondition: this method is only called on a node with left and right child
    def _find_inorder_successor(self, node):
        curr = node.right
        parent = node
        while curr.left is not None:
            parent = curr
            curr = curr.left
        return curr, parent

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

    def delete(self, item):
        if self.root is not None:
            # 1. We need to find the node we want to delete and its parent.
            found, curr, parent = self._locate_node(item)
            if found:
                # handle the case where node has 2 children
                # 1. Find the target node's inorder successor
                # 2. replace the value in the node to be deleted with its successor's value
                # 3. Delete the successor node
                if curr.left is not None and curr.right is not None:
                    successor, succ_parent = self._find_inorder_successor(curr)
                    curr.data = successor.data
                    curr = successor
                    parent = succ_parent


                # * handle the case where we're deleting a leaf or a node w/ 1 child
                # 1) select the target node's non-empty subtree if one exists
                # 2) if target is the root, then root = subtree
                # 3) else; replace parent's reference to target node with the subtree
                if curr.left is not None:
                    subtree = curr.left
                else:
                    subtree = curr.right
                if parent is None:
                    self.root = subtree
                elif parent.left == curr:
                    parent.left = subtree
                else:
                    parent.right = subtree



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


    tree.delete('L')
    tree.traverse_inorder()