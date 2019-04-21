import traceback


# def _test_exception(expected, actual, call):
#     if expected:
#         try:
#             assert isinstance(actual, expected), "{} should raise a {}. Your code: {}".format(call, str(expected), str(actual))
#             print("\u2713 passed: {} \u2192 {}".format(call, expected))
#         except AssertionError as ae:
#             print("\u2717 failed: {}".format(ae))
#     else:
#         print("\u2717 failed. You code raised an exception {}".format())


def _test(expected, actual, call):
    try:
        assert actual == expected, "{} should return {}. Your code: {}".format(call, expected, actual)
        print("\u2713 passed: {} \u2192 {}".format(call, expected))
    except AssertionError as ae:
        print("\u2717 failed: {}".format(ae))


class TestSuite:

    def __init__(self, module_name):
        self.module = module_name

    def test_01_constructor(self, title="constructor"):
        tree = self.module.BinarySearchTree()

        try:
            tree = self.module.BinarySearchTree()
            _test(expected=None,
                  actual=tree.root,
                  call="getting the root of an empty tree")
        except Exception as e:
            print("\u2717 failed. The {} raised an exception. {}: {}".format(title, type(e).__name__, e))
            print(traceback.format_exc())

    def test_02_setitem_doesnt_explode(self):
        tree = self.module.BinarySearchTree()
        try:
            tree[5] = 'Bob'
        except Exception as e:
            print("\u2717 failed. calling tree[5] = 'Bob' raised an exception. {}: {}".format(type(e).__name__, e))
            print(traceback.format_exc())

        try:
            tree[6] = 'Alice'
        except Exception as e:
            print("\u2717 failed. calling tree[6] = 'Alice' raised an exception. {}: {}".format(type(e).__name__, e))
            print(traceback.format_exc())

        try:
            tree[7] = 'Alice'
        except Exception as e:
            print("\u2717 failed. calling tree[7] = 'Charles' raised an exception. {}: {}".format(type(e).__name__, e))
            print(traceback.format_exc())

    def test_03_getitem_keyerrors(self):
        tree = self.module.BinarySearchTree()
        try:
            tree[5]
        except KeyError as ke:
            print("\u2713 passed: __getitem__ on an empty tree correctly raised a KeyError")

        try:
            tree[5] = 'Bob'
            tree[6]
        except KeyError as ke:
            print("\u2713 passed: __getitem__ using a key not in the tree (tree length = 1) correctly raised a KeyError")

        try:
            tree[5] = 'Bob'
            tree[6] = 'Alice'
            tree[7] = 'Charles'
            tree[0]
        except KeyError as ke:
            print("\u2713 passed: __getitem__ using a key not in the tree (tree length = 3) correctly raised a KeyError")

    def test_04_setitem_and_getitem(self):
        tree = self.module.BinarySearchTree()
        tree[5] = 'Alice'

        _test(expected='Alice',
              actual=tree[5],
              call="setting tree[5]='Alice' then calling tree[5]")

        tree[5] = 'Bob'
        _test(expected='Bob',
              actual=tree[5],
              call="verifying that the value 'Alice' is now replaced after calling tree[5]='Bob'")

        tree[7] = 'Wilson'
        _test(expected='Wilson',
              actual=tree[7],
              call="adding a right child: tree[7]='Wilson'")

        tree[-3] = 'Charles'
        _test(expected='Charles',
              actual=tree[-3],
              call="adding a left child: tree[-3]='Charles'")

        tree[-5] = 'Ed'
        tree[-2] = 'Dave'
        _test(expected=True,
              actual=(tree[-5] == 'Ed' and tree[-2] == 'Dave'),
              call="added grandchildren to left child with keys -2 and 0")

        tree[-2] = 'Ed'
        tree[0] = 'Dave'
        _test(expected=True,
              actual=(tree[-2] == 'Ed' and tree[0] == 'Dave'),
              call="added grandchildren to left child with keys -2 and 0")

        tree[6] = 'Harry'
        tree[10] = 'Ron'
        _test(expected=True,
              actual=(tree[6] == 'Harry' and tree[10] == 'Ron'),
              call="added grandchildren to right child with keys 6 and 10")

        tree[-1] = 'Hagrid'
        _test(expected='Hagrid',
              actual=tree[-1],
              call="added great grandchild with key -1")

        tree[-100] = 'Hermione'
        _test(expected='Hermione',
              actual=tree[-100],
              call="added great grandchild with key -100")

    def test_05_setitem_differenttype(self):
        tree = self.module.BinarySearchTree()
        tree['Alice'] = 5
        tree['Wilson'] = 6

        _test(expected=True,
              actual=(tree['Alice'] ==5 and tree['Wilson'] == 6),
              call="checking that the tree supports keys that aren't integers")

    def test_06_len(self):
        tree = self.module.BinarySearchTree()

        _test(expected=0,
              actual=len(tree),
              call="len() of empty tree should be 0")

        tree['Bob'] = 'Jones'
        _test(expected=1,
              actual=len(tree),
              call="len() of empty tree with only root should be 1")

        tree['Bob'] = 'Smith'
        _test(expected=1,
              actual=len(tree),
              call="replaced root. len() should still be 1")

        tree['Charles'] = 'Wilson'
        _test(expected=2,
              actual=len(tree),
              call="adding a right child value. len(tree) should be 2")

        tree['Charles'] = 'Jones'
        _test(expected=2,
              actual=len(tree),
              call="replaced right child value. len(tree) should still be 2")

        tree = self.module.BinarySearchTree()
        tree['Bob'] = 'Jones'
        tree['Adam'] = 'Smith'

        _test(expected=2,
              actual=len(tree),
              call="reset tree. adding a root and left child: len(tree) should be 2")

        tree['Adam'] = 'Barnes'
        _test(expected=2,
              actual=len(tree),
              call="replaced right child value. len(tree) should still be 2")

        tree = self.module.BinarySearchTree()
        tree[5] = 'Bob'
        tree[7] = 'Wilson'
        tree[-3] = 'Charles'
        tree[-5] = 'Ed'
        tree[-2] = 'Dave'
        tree[0] = 'Dave'
        tree[6] = 'Harry'
        tree[10] = 'Ron'
        tree[-1] = 'Hagrid'
        tree[-100] = 'Hermione'

        _test(expected=10,
              actual=len(tree),
              call="reset the tree and added 11 items. len(tree) should be 10")

    def test_07_contains(self):
        tree = self.module.BinarySearchTree()

        _test(expected=False,
              actual=('Joe' in tree),
              call="calling 'in' on an empty tree should return False")

        tree['Joe'] = 'Jones'
        _test(expected=True,
              actual=('Joe' in tree),
              call="'in' finds root node's key")

        _test(expected=False,
              actual=('Jones' in tree),
              call="'in' should not search for values, only keys. This should be False because it is a value in the tree")

        tree = self.module.BinarySearchTree()
        tree[5] = 'Bob'
        tree[7] = 'Wilson'
        tree[-3] = 'Charles'
        tree[-5] = 'Ed'
        tree[-2] = 'Dave'
        tree[0] = 'Dave'
        tree[6] = 'Harry'
        tree[10] = 'Ron'
        tree[-1] = 'Hagrid'
        tree[-100] = 'Hermione'

        _test(expected=True,
              actual=-100 in tree,
              call='reset and added many keys. -100 is a key in the tree')

        _test(expected=True,
              actual=0 in tree,
              call='0 is a key in the tree')