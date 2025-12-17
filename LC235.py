class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
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
    vals = [6, 2, 8, 0, 4, 7, 9, 3, 5]
    root = None
    for v in vals:
        root = insert(root, v)

    p = root.left
    q = root.left.right.right

    sol = Solution()
    lca = sol.lowestCommonAncestor(root, p, q)
    print(lca.val)
