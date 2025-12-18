class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True
            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[l] > nums[m]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                l += 1
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.search([2,5,6,0,0,1,2], 0))
    print(sol.search([2,5,6,0,0,1,2], 3))
    print(sol.search([1,0,1,1,1], 0))
