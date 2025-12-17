class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root):
        def dfs(node):
            if not node:
                return None
            lt = dfs(node.left)
            rt = dfs(node.right)
            if node.left:
                lt.right = node.right
                node.right = node.left
                node.left = None
            return rt or lt or node

        dfs(root)


def to_list(root):
    res = []
    while root:
        res.append(root.val)
        root = root.right
    return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    sol = Solution()
    sol.flatten(root)
    print(to_list(root))
