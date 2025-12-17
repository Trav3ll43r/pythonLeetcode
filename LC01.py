nums = [1, 2, 3, 4, 5]
target = 4

class Solution(object):
    def twoSum(self, nums, target):
        num_d = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_d:
                return [num_d[complement], i]
            num_d[num] = i

        return []


# Driver code (this is required to run it in PyCharm)
if __name__ == "__main__":
    sol = Solution()
    result = sol.twoSum(nums, target)
    print(result)
