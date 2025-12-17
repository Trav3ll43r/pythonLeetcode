class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def bstFromPreorder(self, preorder):
        stack = []
        root = TreeNode(preorder[0])
        stack.append(root)

        for i in range(1, len(preorder)):
            if preorder[i] < stack[-1].val:
                stack[-1].left = TreeNode(preorder[i])
                stack.append(stack[-1].left)
            else:
                while stack and preorder[i] > stack[-1].val:
                    last = stack.pop()
                last.right = TreeNode(preorder[i])
                stack.append(last.right)
        return root


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


if __name__ == "__main__":
    preorder = [8, 5, 1, 7, 10, 12]
    sol = Solution()
    root = sol.bstFromPreorder(preorder)
    print(inorder(root))
