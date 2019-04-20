import sys

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


if __name__ == "__main__":
    a_node = BinaryNode('A')
    print(sys.getsizeof(a_node))
    print(id(a_node))
    print(hex(id(a_node)))
    print(a_node)

    b_node = BinaryNode('B')
    print(b_node)
    c_node = BinaryNode('C')
    print(c_node)

    a_node.left = c_node
    a_node.right = b_node
    print(sys.getsizeof(a_node))
    print(a_node)

