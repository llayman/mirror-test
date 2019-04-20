import time
from old.binary_tree import *

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

def format_time(t):
    if t > 1:
        return '{:.1f}s'.format(t)
    if t * 1000 > 1:
        return '{:.1f}ms'.format(t * 1000)
    if t * 1000000 > 1:
        return '{:.1f}{:}s'.format(t * 1000000, u'\u03BC')
    return '<1{:}s'.format(u'\u03BC')


class UserInfo:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __str__(self):
        return "username: {}, password: {}".format(self.username, self.password)

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.username == other.username and self.password == other.password
        return NotImplemented

    def __lt__(self, other):
        if isinstance(self, other.__class__):
            return self.username < other.username
        return NotImplemented

    def __gt__(self, other):
        if isinstance(self, other.__class__):
            return self.username > other.username
        return NotImplemented


if __name__ == "__main__":
    tree = BinarySearchTree()
    user_list = []

    start = time.time()
    with open('users_10000000.csv') as file:
        for line in file:
            line = line.strip().split(',')
            # user_list.append(UserInfo(line[0], line[1]))
            tree.insert(UserInfo(line[0], line[1]))
    # tree.traverse_preorder()
    # print('Tree height:', tree.height())
    # user_list.sort()
    print('Time to build:', format_time(time.time()-start))

    done = False
    while not done:
        username = input("Enter username, or leave blank to quit: ")
        if username == '':
            done = True
            continue
        password = input("Password: ")
        user = UserInfo(username, password)
        start = time.time()
        # if user in user_list:
        if user in tree:
        # if binarySearch(user_list, user):
            print('Valid')
        else:
            print('Invalid')
        print('Time to search:', format_time(time.time() - start))
