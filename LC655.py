class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root):
        h = self.calc_height(root)
        m = h
        n = 2 ** m - 1
        res = [[""] * n for _ in range(m)]

        def helper(node, row, l, r):
            if not node or row == m:
                return
            mid = (l + r) // 2
            res[row][mid] = str(node.val)
            helper(node.left, row + 1, l, mid - 1)
            helper(node.right, row + 1, mid + 1, r)

        helper(root, 0, 0, n - 1)
        return res

    def calc_height(self, root):
        if not root:
            return 0
        return max(self.calc_height(root.left), self.calc_height(root.right)) + 1


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)

    sol = Solution()
    out = sol.printTree(root)
    for row in out:
        print(row)
