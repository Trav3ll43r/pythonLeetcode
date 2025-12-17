class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def balanceBST(self, root):
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            vals.append(node.val)
            traverse(node.right)

        def construct(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            return TreeNode(vals[m], construct(l, m - 1), construct(m + 1, r))

        vals = []
        traverse(root)
        return construct(0, len(vals) - 1)


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)

    sol = Solution()
    new_root = sol.balanceBST(root)
    print(inorder(new_root))
