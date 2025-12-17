class Solution(object):
    def numTrees(self, n):
        numt = [1] * (n + 1)
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                total += numt[left] * numt[right]
            numt[nodes] = total
        return numt[n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.numTrees(1))
    print(sol.numTrees(2))
    print(sol.numTrees(3))
    print(sol.numTrees(4))
