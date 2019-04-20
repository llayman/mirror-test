# keys are all the same type

# __delite__
# contains
# len
# traverse_inorder
# traverse_preorder
# traverse_postorder
# __ iter__
# reversed
# clear
# keys
# values
# items

class BinaryNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        raddr = laddr = None
        if self.left:
            laddr = "BinaryNode at " + hex(id(self.left))
        if self.right:
            raddr = "BinaryNode at " + hex(id(self.right))
        return "<BinaryNode at {}, key: {}, value: {}, left: {}, right: {}>".format(hex(id(self)), self.key, self.value, laddr, raddr)


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
    suite.test_05_setitem_differenttype()
    # suite.test_01_powers_of_two()
    # suite.test_02_is_palindrome()
    # suite.test_03_folding_method()
    # suite.test_04_load_driver_data()
    # suite.test_05_find_plate()
    # suite.test_06_find_palindrome_in_plates()
    # suite.test_07_find_suspicious()

if __name__ == '__main__':
    main()