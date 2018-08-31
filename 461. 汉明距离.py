# -*- coding: utf-8 -*-
# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
#
# 给出两个整数 x 和 y，计算它们之间的汉明距离。
#
# 注意：
# 0 ≤ x, y < 231.
#
# 示例:
#
# 输入: x = 1, y = 4
#
# 输出: 2
#
# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# 上面的箭头指出了对应二进制位不同的位置。
# 整数转二进制数： 不断的除2求余，然后余数倒排
def d2b(n):
     re=[]
     n,m=divmod(n,2)
     re.append(str(m))
     while n!=0:
         n,m=divmod(n,2)
         re.insert(0,str(m))
     return ''.join(re)
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #答案一、 logN 异或运算后，取2 的余数 --------------------
        temp = x ^ y
        count = 0
        while temp != 0:
            if temp % 2 != 0:
                count += 1
            temp = temp // 2
        return count
        # 答案二、用python自带函数bin()，对异或后的结果转二进制，对“1”计数-------------
        return bin(x ^ y)[2:].count("1")

        # 自己写的，好慢----------------------------------
        a = bin(x).replace("0b", "")
        b = bin(y).replace("0b", "")
        max_num = a if len(a) >= len(b) else b
        min_num = a if len(a) < len(b) else b
        min_i = len(min_num)
        max_i = len(max_num)
        res = 0
        for i in range(min_i):
            if min_num[min_i - i - 1] != max_num[max_i - i - 1]:
                res += 1
        for j in range(len(max_num) - len(min_num)):
            if max_num[j] == "1":
                res += 1
        return res


s = Solution()
print(s.hammingDistance(93, 73))
