class Solution(object):
    def circularArrayLoop(self, nums):
        visited = set()
        n = len(nums)

        def getnext(index, curr_dir):
            next_index = (index + nums[index]) % n
            next_dir = 1 if nums[next_index] > 0 else -1
            if curr_dir != next_dir or index == next_index:
                return -1
            return next_index

        for i in range(n):
            if i in visited:
                continue

            sp, fp = i, i
            curr_dir = 1 if nums[i] > 0 else -1

            while True:
                visited.add(sp)
                visited.add(fp)
                sp = getnext(sp, curr_dir)
                fp = getnext(fp, curr_dir)
                if sp == -1 or fp == -1:
                    break

                fp = getnext(fp, curr_dir)
                if fp == -1:
                    break
                if sp == fp:
                    return True
        return False
if __name__=="__main__":
    nums=[1,2,3,4,5,6]
    sol=Solution()
    result=sol.circularArrayLoop(nums)
    print(result)