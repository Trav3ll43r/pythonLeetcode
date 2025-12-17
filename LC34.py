class Solution:
    def searchRange(self, nums, target):
        left = self.bs(nums, target, True)
        right = self.bs(nums, target, False)
        return [left, right]

    def bs(self, nums, target, leftbias):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = l + (r - l) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftbias:
                    r = m - 1
                else:
                    l = m + 1
        return i


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 6))
    print(sol.searchRange([], 0))
