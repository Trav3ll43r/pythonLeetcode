nums=[1,2,3,4,5]
k=2

class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        l, r = 0, len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = 0, k - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = k, len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
if __name__=="__main__":
    sol=Solution()
    sol.rotate(nums,k)
    print(nums)