class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def bstToGst(self, root):
        def dfs(node, acc):
            if not node:
                return 0
            r = dfs(node.right, acc)
            v = node.val
            node.val = v + acc + r
            l = dfs(node.left, acc + v + r)
            return r + v + l

        dfs(root, 0)
        return root


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(6)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)

    sol = Solution()
    res = sol.bstToGst(root)
    print(inorder(res))
