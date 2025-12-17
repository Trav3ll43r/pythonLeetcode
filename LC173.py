class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        node = self.stack.pop()
        cur = node.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return node.val

    def hasNext(self):
        return self.stack != []


if __name__ == "__main__":
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    it = BSTIterator(root)
    out = []
    while it.hasNext():
        out.append(it.next())
    print(out)
