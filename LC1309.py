class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorder(self, l, root):
        if not root:
            return
        self.inorder(l, root.right)
        l.append(root.val)
        self.inorder(l, root.left)

    def getAllElements(self, root1, root2):
        l = []
        self.inorder(l, root1)
        self.inorder(l, root2)
        return sorted(l)


def build_bst(vals):
    if not vals:
        return None
    root = None
    for v in vals:
        root = insert(root, v)
    return root


def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


if __name__ == "__main__":
    root1 = build_bst([2, 1, 4])
    root2 = build_bst([1, 0, 3])

    sol = Solution()
    print(sol.getAllElements(root1, root2))
