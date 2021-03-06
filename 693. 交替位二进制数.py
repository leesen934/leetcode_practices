# -*- coding: utf-8 -*-
# 给定一个正整数，检查他是否为交替位二进制数：换句话说，就是他的二进制数相邻的两个位数永不相等。
# 示例 1:
#
# 输入: 5
# 输出: True
# 解释:
# 5的二进制数是: 101
# 示例 2:
#
# 输入: 7
# 输出: False
# 解释:
# 7的二进制数是: 111
# 示例 3:
#
# 输入: 11
# 输出: False
# 解释:
# 11的二进制数是: 1011
#  示例 4:
#
# 输入: 10
# 输出: True
# 解释:
# 10的二进制数是: 1010
class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 2:
            return True
        bin_n = bin(n)[2:]
        for i in range(len(bin_n) - 1):
            if bin_n[i] == bin_n[i+1]:
                return False
        return True

s = Solution()
print(s.hasAlternatingBits(11))
print(s.hasAlternatingBits(10))