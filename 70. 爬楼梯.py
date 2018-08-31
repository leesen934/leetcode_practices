# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
#
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 示例 2：
#
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 自己写的，占用空间有些大，可以用变量代替存储数组 ----------------
        if n == 1:
            return 1
        Fb = [1, 1]
        i = 1
        while i < n:
            Fb.append(Fb[-1] + Fb[-2])
            i += 1
        return Fb[-1]
        # 变量代替fb数组，更快 ----------------------
        # same as calculating fibonacci(n)
        if n == 1:
            return 1
        elif n == 2:
            return 2
        prev = 1
        curr = 2
        for i in range(2, n):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr

s = Solution()
print(s.climbStairs(3))