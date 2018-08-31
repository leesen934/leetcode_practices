# 实现函数
# ToLowerCase()，该函数接收一个字符串参数
# str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
#
#
#
# 示例
# 1：
#
# 输入: "Hello"
# 输出: "hello"
# 示例
# 2：
#
# 输入: "here"
# 输出: "here"
# 示例
# 3：
#
# 输入: "LOVELY"
# 输出: "lovely"
class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        l1 = [chr(ord("A") + i) for i in range(26)]
        l2 = [chr(ord("a") + j) for j in range(26)]
        dic = dict(zip(l1, l2))
        res = []
        for i in range(len(str)):
            if str[i] in dic:
                res.append(dic[str[i]])
            else:
                res.append(str[i])
        return ''.join(res)

        # 答案之一 ： 利用大写字母和小写字母之间的ASC码差值转换 -------------
        ret = ""
        for c in str:
            if ord(c) >= ord('A') and ord(c) <= ord('Z'):
                ret += chr(ord(c) - ord('A') + ord('a'))
            else:
                ret += c
        return ret

s = Solution()
test = "Hello"
print(s.toLowerCase(test))