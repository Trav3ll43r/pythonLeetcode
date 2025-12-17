class Solution(object):
    def minEnd(self, n, x):
        res = x
        bit = 1
        k = n - 1

        while k > 0:
            if (bit & x) == 0:
                if k & 1:
                    res |= bit
                k >>= 1
            bit <<= 1

        return res


if __name__ == "__main__":
    n = 3
    x = 4

    sol = Solution()
    res = sol.minEnd(n, x)
    print(res)
