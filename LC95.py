class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def generateTrees(self, n):
        def generate(left, right):
            if left > right:
                return [None]
            res = []
            for val in range(left, right + 1):
                for l in generate(left, val - 1):
                    for r in generate(val + 1, right):
                        res.append(TreeNode(val, l, r))
            return res

        if n == 0:
            return []
        return generate(1, n)


def preorder(root):
    if not root:
        return None
    return (root.val, preorder(root.left), preorder(root.right))


if __name__ == "__main__":
    sol = Solution()
    trees = sol.generateTrees(3)
    out = [preorder(t) for t in trees]
    print(out)
