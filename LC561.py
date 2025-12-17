class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()

        return sum(nums[i] for i in range (0, len(nums), 2))

if __name__=="__main__":
    nums=[1,2,3,4,5]
    sol=Solution()
    result=sol.arrayPairSum(nums)
    print(result)