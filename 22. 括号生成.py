#
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
class Solution:

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        temp = ""
        self.gen(temp, 0, 0, res, n)

        return res

    def gen(self, temp, left, right, res, n):
        if left + right == n * 2:
            res.append(temp)
            return
        if left < n:
            self.gen(temp + "(", left + 1, right, res, n)
        if left > right:
            self.gen(temp + ")", left, right+1, res, n)

    # 剩余计数也可以----------------------------
        result = []
        self.parenthesis(result,"",n,n)
        return result

    def parenthesis(self, result, source, left, right):
        if left==0 and right==0:
            result.append(source)
            return
        if left>0:
            self.parenthesis(result, source+"(", left-1, right)
        if left<right and right>0:
            self.parenthesis(result, source+")", left, right-1)

s = Solution()
print(s.generateParenthesis(3))