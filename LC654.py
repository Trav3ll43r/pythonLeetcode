class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        idx = nums.index(max(nums))
        node = TreeNode(nums[idx])
        node.left = self.constructMaximumBinaryTree(nums[:idx])
        node.right = self.constructMaximumBinaryTree(nums[idx + 1:])
        return node


def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


if __name__ == "__main__":
    nums = [3, 2, 1, 6, 0, 5]
    sol = Solution()
    root = sol.constructMaximumBinaryTree(nums)
    print(preorder(root))
