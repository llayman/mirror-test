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
            print("\u2713 passed: __getitem__ on an empty tree raised a KeyError")

        try:
            tree[5] = 'Bob'
            tree[6]
        except KeyError as ke:
            print("\u2713 passed: __getitem__ using a key not in the tree (tree length = 1) raised a KeyError")

        try:
            tree[5] = 'Bob'
            tree[6] = 'Alice'
            tree[7] = 'Charles'
            tree[0]
        except KeyError as ke:
            print("\u2713 passed: __getitem__ using a key not in the tree (tree length = 3) raised a KeyError")

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

        tree[6] = 'Wilson'
        _test(expected='Wilson',
              actual=tree[6],
              call="verifying that the value 'Alice' is now replaced after calling tree[5]='Bob'")

        tree[-1] = 'Charles'
        _test(expected=True,
              actual=(tree[5] == 'Bob' and tree[6] == 'Wilson' and tree[-1] == 'Charles'),
              call="tree appears to be storing multiple values")

    def test_05_setitem_differenttype(self):
        tree = self.module.BinarySearchTree()
        tree['Alice'] = 5
        tree['Wilson'] = 6

        _test(expected=True,
              actual=(tree['Alice'] ==5 and tree['Wilson'] == 6),
              call="checking that the tree supports keys that aren't integers")



        #
        # _test(expected=[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
        #       actual=self.module.problem1_powers_of_two(10),
        #       call="powers_of_two(10)")
        #
        # _test(expected=[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072,
        #                 262144],
        #       actual=self.module.problem1_powers_of_two(18),
        #       call="powers_of_two(18)")
        #
        # _test(expected=[1],
        #       actual=self.module.problem1_powers_of_two(0),
        #       call="powers_of_two(0)")