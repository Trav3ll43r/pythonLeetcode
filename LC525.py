class Solution(object):
    def findMaxLength(self, nums):
        seen_at = {}
        seen_at[0] = -1

        ans = count = 0

        for i, num in enumerate(nums):
            count += 1 if num else -1

            if count in seen_at:
                ans = max(ans, i - seen_at[count])
            else:
                seen_at[count] = i

        return ans
if __name__=="__main__":
    nums=[1,0,1,1,0,0]
    sol=Solution()
    result=sol.findMaxLength(nums)
    print(result)