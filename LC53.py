class Solution:
    def maxSubArray(self, nums):
        max_sum = cur_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(num, num + cur_sum)
            max_sum = max(max_sum, cur_sum)
        return max_sum


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(sol.maxSubArray([1]))
    print(sol.maxSubArray([5, 4, -1, 7, 8]))
