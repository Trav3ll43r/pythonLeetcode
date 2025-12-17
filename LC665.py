class Solution(object):
    def checkPossibility(self, nums):

        change = False
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue
            if change == True:
                return False
            if i == 0 or nums[i + 1] >= nums[i - 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]
            change = True
        return True
if __name__=="__main__":
    nums=[1,2,3,4,5,6,7]
    sol=Solution()
    res=sol.checkPossibility(nums)
    print(res)