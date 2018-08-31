#
# 给定一个Excel表格中的列名称，返回其相应的列序号。
#
# 例如，
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
# 示例 1:
#
# 输入: "A"
# 输出: 1
# 示例 2:
#
# 输入: "AB"
# 输出: 28
# 示例 3:
#
# 输入: "ZY"
# 输出: 701
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 相当于26 进制 计数
        # 例如AAA， dic[A] * 26 ^2 + dic[A] * 26^1 + dic[A] * 26^0
        rule = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        dic = dict(zip(rule, list(range(1, 27))))
        res = 0
        for i in range(len(s)):
            res += dic[s[len(s) - 1 - i]] * 26 ** i
        return res
        #  -----------------------------------------------------------------------------
        # 取位数时，个十百千位依次为0,1,2,3， 与字符串下标相反，可以取字符串逆序
        dic_letter = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,
                     'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
        output = 0
        for index, val in enumerate(s[::-1]):
            output += dic_letter[val]*(26**index)
        return output

s = Solution()
print(s.titleToNumber('A'))