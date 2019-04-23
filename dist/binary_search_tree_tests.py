import io
import re
import traceback
from contextlib import redirect_stdout


def _test(expected, actual, call):
    try:
        assert actual == expected, "{} should return {}. Your code: {}".format(call, expected, actual)
        print("\u2713 passed: {} \u2192 {}".format(call, expected))
    except AssertionError as ae:
        print("\u2717 failed: {}".format(ae))


class TestSuite:

    def __init__(self, module_name):
        self.module = module_name

    def test_01_constructor(self):
        tree = self.module.TreeMap()
        try:
            _test(expected=None,
                  actual=tree.root,
                  call="getting the root of an empty tree")
        except Exception as e:
            print("\u2717 FAILED. The constructor raised an exception. {}: {}".format(type(e).__name__, e))
            print(traceback.format_exc())

    def test_02_setitem_doesnt_explode(self):
        tree = self.module.TreeMap()
        try:
            tree[5] = 'Bob'
        except NotImplementedError:
            print(
                "\u2717 FAILED: call to tree[5]='Bob' failed because  __setitem__ is not implemented. Aborting tests of __setitem__")
            return

        except Exception as e:
            print("\u2717 FAILED. calling tree[5] = 'Bob' raised an exception. {}: {}".format(type(e).__name__, e))
            print(traceback.format_exc())

        try:
            tree[6] = 'Alice'
        except Exception as e:
            print("\u2717 FAILED. calling tree[6] = 'Alice' raised an exception. {}: {}".format(type(e).__name__, e))
            print(traceback.format_exc())

        try:
            tree[7] = 'Alice'
        except Exception as e:
            print("\u2717 FAILED. calling tree[7] = 'Charles' raised an exception. {}: {}".format(type(e).__name__, e))
            print(traceback.format_exc())

    def test_03_getitem_keyerrors(self):
        tree = self.module.TreeMap()
        try:
            tree[5]
            print("\u2717 FAILED: call to 'tree[5]' on an empty tree should have raised a KeyError")
        except NotImplementedError:
            print("\u2717 FAILED:  __getitem__ is not implemented. Aborting tests of __getitem__")
            return
        except KeyError:
            print("\u2713 passed: __getitem__ on an empty tree correctly raised a KeyError")

        try:
            tree[5] = 'Bob'
            tree[6]
            print("\u2717 FAILED: __getitem__ using a key not in the tree (tree length = 1) should raise a KeyError")
        except KeyError:
            print(
                "\u2713 passed: __getitem__ using a key not in the tree (tree length = 1) correctly raised a KeyError")

        try:
            tree[5] = 'Bob'
            tree[6] = 'Alice'
            tree[7] = 'Charles'
            tree[0]
            print("\u2717 FAILED: __getitem__ using a key not in the tree (tree length = 3) should raise a KeyError")
        except KeyError:
            print(
                "\u2713 passed: __getitem__ using a key not in the tree (tree length = 3) correctly raised a KeyError")

    def test_04_setitem_and_getitem(self):
        tree = self.module.TreeMap()

        try:
            tree[5] = 'Alice'
            _test(expected='Alice',
                  actual=tree[5],
                  call="setting tree[5]='Alice' then calling tree[5]")
        except NotImplementedError:
            print("\u2717 FAILED: call to tree[5]='Alice' or tree[5]. __setitem__  or __getitem__ is not implemented.")
            return

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

        tree = self.module.TreeMap()
        tree['Alice'] = 5
        tree['Wilson'] = 6

        _test(expected=True,
              actual=(tree['Alice'] == 5 and tree['Wilson'] == 6),
              call="checking that the tree supports keys that aren't integers")

    def test_05_len(self):
        tree = self.module.TreeMap()

        try:
            _test(expected=0,
                  actual=len(tree),
                  call="len() of empty tree should be 0")
        except NotImplementedError:
            print("\u2717 FAILED: call to len(tree) FAILED. __len__ is not implemented. Aborting tests of len() calls")
            return

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

        tree = self.module.TreeMap()
        tree['Bob'] = 'Jones'
        tree['Adam'] = 'Smith'

        _test(expected=2,
              actual=len(tree),
              call="reset tree. adding a root and left child: len(tree) should be 2")

        tree['Adam'] = 'Barnes'
        _test(expected=2,
              actual=len(tree),
              call="replaced right child value. len(tree) should still be 2")

        tree = self.module.TreeMap()
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

    def test_06_contains(self):
        tree = self.module.TreeMap()
        try:
            _test(expected=False,
                  actual='Joe' in tree,
                  call="calling 'in' on an empty tree should return False")
        except NotImplementedError:
            print("\u2717 FAILED: call to \"'Joe' in tree\" failed. __contains__ is not implements. Aborting tests of 'in'")
            return

        tree['Joe'] = 'Jones'
        _test(expected=True,
              actual=('Joe' in tree),
              call="'in' finds root node's key")

        _test(expected=False,
              actual=('Jones' in tree),
              call="'in' should not search for values, only keys. This should be False because it is a value in the tree")

        tree = self.module.TreeMap()
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

    def test_07_delitem(self):
        tree = self.module.TreeMap()
        try:
            del tree[5]
            print("\u2717 FAILED: call to 'del tree[5]' on an empty tree should have raised a KeyError")
        except NotImplementedError:
            print("\u2717 FAILED: call to 'del tree[5]' failed. __delitem__ is not implemented. Aborting tests of del")
            return
        except KeyError:
            print("\u2713 passed: called del tree[5] on an empty tree correctly raised a KeyError")

        tree[10] = 'Alice'
        del tree[10]
        _test(expected=0,
              actual=len(tree),
              call="len(tree) should be zero after deleting the only node in the tree")

        _test(expected=False,
              actual=10 in tree,
              call="'10 in tree' should return False after the key was deleted")

        _test(expected=None,
              actual=tree.root,
              call="tree.root should be None after deleting the only node in the tree")

        try:
            del tree[10]
            print("\u2717 FAILED: call to 'del tree[10]' on a now-empty tree should have raised a KeyError")
        except KeyError:
            print("\u2713 passed: called del tree[10] on a now-empty tree correctly raised a KeyError")

        tree[10] = 'Alice'
        tree[5] = 'Bob'
        tree[15] = 'Charlie'

        del tree[10]
        _test(expected='Charlie',
              actual=tree.root.value,
              call="tree.root.value should be Charlie after deleting the root with two children")

        _test(expected=2,
              actual=len(tree),
              call="len(tree) should be two after adding 3 nodes and deleting 1")

        _test(expected=False,
              actual=10 in tree,
              call="'10 in tree' should return False after the key was deleted")

        try:
            del tree[10]
            print("\u2717 FAILED: called del[10] (which was previously deleted) should have raised a KeyError")
        except KeyError:
            print("\u2713 passed: called del[10] (which was previously deleted) correctly raised a KeyError")

        _test(expected=2,
              actual=len(tree),
              call="len(tree) should be still two after trying to delete a node that wasn't there")

        del tree[5]
        _test(expected='Charlie',
              actual=tree.root.value,
              call="tree.root.value should be Bob after deleting the root with one child")

        _test(expected=1,
              actual=len(tree),
              call="len(tree) should be one after deleting another node")

        _test(expected=False,
              actual=5 in tree,
              call="'5 in tree' should return False after the key was deleted")

        del tree[15]
        _test(expected=0,
              actual=len(tree),
              call="len(tree) should be zero after deleting all the nodes")

        _test(expected=None,
              actual=tree.root,
              call="tree.root should be None after deleting all the nodes")

        _test(expected=False,
              actual=15 in tree,
              call="'15 in tree' should return False after the key was deleted")

        tree = self.module.TreeMap()
        tree[10] = 'Alice'
        tree[5] = 'Bob'
        tree[1] = 'Charlie'
        tree[15] = 'Dave'
        tree[12] = 'Ernie'

        del tree[1]
        _test(expected=4,
              actual=len(tree),
              call='deleted a leaf node (tree[1]). length should be 4')

        _test(expected=None,
              actual=tree.root.left.left,
              call='left grandchild of root should be None after deleting that leaf node')

        _test(expected=False,
              actual=1 in tree,
              call="'1 in tree' should return False after the key was deleted")

        del tree[15]
        _test(expected=3,
              actual=len(tree),
              call='deleted a node with one child (tree[15]). length should now be 3')

        _test(expected='Ernie',
              actual=tree.root.right.value,
              call="root's right child should have key=12, value='Ernie' after deleting the original right child")

        _test(expected=False,
              actual=15 in tree,
              call="'15 in tree' should return False after the key was deleted")

        tree = self.module.TreeMap()
        tree['Frank'] = 'Zonk'
        tree['Bob'] = 12345
        tree['Alice'] = 84431
        tree['Dave'] = 131234
        tree['Charlie'] = 123455
        tree['Cara'] = 99999

        del tree['Bob']
        _test(expected='Cara',
              actual=tree.root.left.key,
              call="called del tree['Bob'] who is the left child of the root. Should be replaced by its inorder successor node, whoese key is Cara")

        _test(expected=5,
              actual=len(tree),
              call='length should now be 5')

        _test(expected=False,
              actual='Bob' in tree,
              call="('Bob' in tree) should return False after the key was deleted")

        del tree['Cara']
        _test(expected='Charlie',
              actual=tree.root.left.key,
              call="called del tree['Cara'] who is now the left child of the root. Should be replaced by its inorder successor node, whose key is Charlie")

        _test(expected=4,
              actual=len(tree),
              call='length should now be 4')

        _test(expected=False,
              actual='Cara' in tree,
              call="('Cara' in tree) should return False after the key was deleted")

    def test_08_inorder_traversal(self):

        try:
            tree = self.module.TreeMap()
            tree['Charlie'] = 55555
            tree['Bob'] = 44444
            tree['Alice'] = 33333
            tree['Banks'] = 123145
            tree['Dave'] = 891273
            tree['Chris'] = 9012
            tree['Ernie'] = 0000000
            tree['Doug'] = 123
            tree['Frank'] = 0000000
            expected = "(Alice,33333)(Banks,123145)(Bob,44444)(Charlie,55555)(Chris,9012)(Dave,891273)(Doug,123)(Ernie,0)(Frank,0)"

            f = io.StringIO()
            with redirect_stdout(f):
                tree.traverse_inorder()
            actual = re.sub(r'\s+', '', f.getvalue())
            _test(expected=expected,
                  actual=actual,
                  call="traverse_inorder()")
        except NotImplementedError:
            print("\u2717 FAILED: traverse_inorder() not implemented. aborting further tests")
            return

        tree = self.module.TreeMap()
        f = io.StringIO()
        with redirect_stdout(f):
            tree.traverse_inorder()
        actual = re.sub(r'\s+', '', f.getvalue())
        _test(expected='',
              actual=actual,
              call="traverse_inorder() on an empty tree should not print anything")

    def test_09_preorder_traversal(self):

        try:
            tree = self.module.TreeMap()
            tree['Charlie'] = 55555
            tree['Bob'] = 44444
            tree['Alice'] = 33333
            tree['Banks'] = 123145
            tree['Dave'] = 891273
            tree['Chris'] = 9012
            tree['Ernie'] = 0000000
            tree['Doug'] = 123
            tree['Frank'] = 0000000
            expected = "(Charlie,55555)(Bob,44444)(Alice,33333)(Banks,123145)(Dave,891273)(Chris,9012)(Ernie,0)(Doug,123)(Frank,0)"

            f = io.StringIO()
            with redirect_stdout(f):
                tree.traverse_preorder()
            actual = re.sub(r'\s+', '', f.getvalue())
            _test(expected=expected,
                  actual=actual,
                  call="traverse_preorder()")
        except NotImplementedError:
            print("\u2717 FAILED: traverse_preorder() not implemented. aborting further tests")
            return

        tree = self.module.TreeMap()
        f = io.StringIO()
        with redirect_stdout(f):
            tree.traverse_preorder()
        actual = re.sub(r'\s+', '', f.getvalue())
        _test(expected='',
              actual=actual,
              call="traverse_preorder() on an empty tree should not print anything")

    def test_10_postorder_traversal(self):

        try:
            tree = self.module.TreeMap()
            tree['Charlie'] = 55555
            tree['Bob'] = 44444
            tree['Alice'] = 33333
            tree['Banks'] = 123145
            tree['Dave'] = 891273
            tree['Chris'] = 9012
            tree['Ernie'] = 0000000
            tree['Doug'] = 123
            tree['Frank'] = 0000000
            expected = "(Banks,123145)(Alice,33333)(Bob,44444)(Chris,9012)(Doug,123)(Frank,0)(Ernie,0)(Dave,891273)(Charlie,55555)"

            f = io.StringIO()
            with redirect_stdout(f):
                tree.traverse_postorder()
            actual = re.sub(r'\s+', '', f.getvalue())
            _test(expected=expected,
                  actual=actual,
                  call="traverse_postorder()")
        except NotImplementedError:
            print("\u2717 FAILED: traverse_postorder() not implemented. aborting further tests")
            return

        tree = self.module.TreeMap()
        f = io.StringIO()
        with redirect_stdout(f):
            tree.traverse_postorder()
        actual = re.sub(r'\s+', '', f.getvalue())
        _test(expected='',
              actual=actual,
              call="traverse_postorder() on an empty tree should not print anything")

    def test_11_keys(self):

        try:
            tree = self.module.TreeMap()
            tree['Charlie'] = 55555
            tree['Bob'] = 44444
            tree['Alice'] = 33333
            tree['Banks'] = 123145
            tree['Dave'] = 891273
            tree['Chris'] = 9012
            tree['Ernie'] = 0000000
            tree['Doug'] = 123
            tree['Frank'] = 0000000
            expected = ['Alice', 'Banks', 'Bob', 'Charlie', 'Chris', 'Dave', 'Doug', 'Ernie', 'Frank']

            _test(expected=expected,
                  actual=tree.keys(),
                  call="keys()")

        except NotImplementedError:
            print("\u2717 FAILED: keys() not implemented. aborting further tests")
            return

        tree = self.module.TreeMap()
        _test(expected=[],
              actual=tree.keys(),
              call="keys() on an empty tree should return an empty list")

    def test_12_values(self):

        try:
            tree = self.module.TreeMap()
            tree['Charlie'] = 55555
            tree['Bob'] = 44444
            tree['Alice'] = 33333
            tree['Banks'] = 123145
            tree['Dave'] = 891273
            tree['Chris'] = 9012
            tree['Ernie'] = 0000000
            tree['Doug'] = 123
            tree['Frank'] = 0000000
            expected = [33333, 123145, 44444, 55555, 9012, 891273, 123, 0, 0]

            _test(expected=expected,
                  actual=tree.values(),
                  call="values()")

        except NotImplementedError:
            print("\u2717 FAILED: values() not implemented. aborting further tests")
            return

        tree = self.module.TreeMap()
        _test(expected=[],
              actual=tree.keys(),
              call="values() on an empty tree should return an empty list")

    def test_13_height(self):
        try:
            tree = self.module.TreeMap()
            tree['Charlie'] = 55555
            tree['Bob'] = 44444
            tree['Alice'] = 33333
            tree['Banks'] = 123145
            tree['Dave'] = 891273
            tree['Chris'] = 9012
            tree['Ernie'] = 0000000
            tree['Doug'] = 123
            tree['Frank'] = 0000000

            _test(expected=3,
                  actual=tree.height(),
                  call="tree.height()")
        except NotImplementedError:
            print("\u2717 FAILED: height() not implemented. aborting further tests")
            return

        tree = self.module.TreeMap()
        tree[1] = 55555
        tree[0] = 'aaaa'
        tree[2] = 44444
        tree[3] = 33333
        tree[4] = 123145
        tree[5] = 891273
        tree[6] = 9012
        tree[7] = 0000000
        tree[8] = 123
        tree[9] = 0000000

        _test(expected=8,
              actual=tree.height(),
              call="tree.height()")

        tree = self.module.TreeMap()
        tree[1] = 55555
        _test(expected=0,
              actual=tree.height(),
              call="tree.height()")
        try:
            tree = self.module.TreeMap()
            tree.height()
            print("\u2717 FAILED: height() on an empty tree should raise a ValueError")
        except ValueError:
            print("\u2713 passed: called height() on an empty tree correctly raised a ValueError")

    def test_14_find_min(self):
        try:
            tree = self.module.TreeMap()
            tree['Charlie'] = 55555
            tree['Bob'] = 44444
            tree['Alice'] = 33333
            tree['Banks'] = 123145
            tree['Dave'] = 891273
            tree['Chris'] = 9012
            tree['Ernie'] = 0000000
            tree['Doug'] = 123
            tree['Frank'] = 0000000

            _test(expected='Alice',
                  actual=tree.find_min(),
                  call="tree.find_min()")
        except NotImplementedError:
            print("\u2717 FAILED: find_min() not implemented. aborting further tests")
            return

        try:
            tree = self.module.TreeMap()
            tree.find_min()
            print("\u2717 FAILED: find_min() on an empty tree should raise a ValueError")
        except ValueError:
            print("\u2713 passed: called find_min() on an empty tree correctly raised a ValueError")

    def test_15_find_max(self):
        try:
            tree = self.module.TreeMap()
            tree['Charlie'] = 55555
            tree['Bob'] = 44444
            tree['Alice'] = 33333
            tree['Banks'] = 123145
            tree['Dave'] = 891273
            tree['Chris'] = 9012
            tree['Ernie'] = 0000000
            tree['Doug'] = 123
            tree['Frank'] = 0000000

            _test(expected='Frank',
                  actual=tree.find_max(),
                  call="tree.find_max()")
        except NotImplementedError:
            print("\u2717 FAILED: find_max() not implemented. aborting further tests")
            return

        try:
            tree = self.module.TreeMap()
            tree.find_max()
            print("\u2717 FAILED: find_max() on an empty tree should raise a ValueError")
        except ValueError:
            print("\u2713 passed: called find_max() on an empty tree correctly raised a ValueError")