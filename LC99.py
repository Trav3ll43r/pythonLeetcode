class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def recoverTree(self, root):
        curr = root
        prev = TreeNode(float('-inf'))
        replace = []
        stack = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            temp = stack.pop()
            if temp.val < prev.val:
                replace.append((prev, temp))

            prev = temp
            curr = temp.right

        replace[0][0].val, replace[-1][1].val = replace[-1][1].val, replace[0][0].val


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)

    print(inorder(root))
    sol = Solution()
    sol.recoverTree(root)
    print(inorder(root))
