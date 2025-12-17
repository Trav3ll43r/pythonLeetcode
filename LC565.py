class Solution(object):
    def arrayNesting(self, nums):

        ans = 0
        for i in range(len(nums)):
            if nums[i] == -1:
                continue
            length = 0
            x = i
            while nums[x] != -1:
                next_x = nums[x]
                nums[x] = -1
                x = next_x
                length += 1
            ans = max(ans, length)
        return ans
if __name__=="__main__":
    nums=[5,4,0,3,1,6,2]
    sol=Solution()
    result=sol.arrayNesting(nums)
    print(result)