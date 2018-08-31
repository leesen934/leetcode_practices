# 统计所有小于非负整数 n 的质数的数量。
#
# 示例:
#
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 一个合数必然能分解成质因子之积.
        # 因此我们每当找到一个素数, 设它为 i, 那么对于2∗i,3∗i,4∗i,....,n这些数来说肯定都是合数.
        # 照着这个思想, 再吃几颗Python的语法糖, 我们便能把速度拉上去.
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        # print(primes)
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])  # TypeError: must assign iterable to extended slice
                # print(primes)
        return sum(primes)

        # 超出时间限制 -------------------------
        # if n == 0 or n == 1:
        #     return 0
        # l1 = list(range(2, n))
        # for i in range(2, round(n ** 0.5) + 1):
        #     if i not in l1:
        #         continue
        #     else:
        #         for j in range(i, n // i + 1):
        #             if i * j in l1:
        #                 l1.remove(i * j)

        return len(l1)


s = Solution()
print(s.countPrimes(10))