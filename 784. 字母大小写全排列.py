# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
#
# 示例:
# 输入: S = "a1b2"
# 输出: ["a1b2", "a1B2", "A1b2", "A1B2"]
#
# 输入: S = "3z4"
# 输出: ["3z4", "3Z4"]
#
# 输入: S = "12345"
# 输出: ["12345"]
# 注意：
#
# S 的长度不超过12。
# S 仅由数字和字母组成。
#
# 回溯法 ----------------------------------------------------------
# 看到这个题，仍然想到了回溯法。这个题要求数字保留，字母分成大小写两种。使用回溯法就是分类成数字和字母，字母再分为大写和小写继续。
#
# 要注意的一点是不需要使用for循环了。做39. Combination Sum题目的时候使用for循环的目的是能在任意位置起始求和得到目标。本题不需要从任意位置开始。
#
# dfs即可，遇到数字跳过，遇到字母，分为两种情况传给子问题。
class Solution:
    def dfs(self, s, index, path, res):
        if index == len(s):
            res.append(path)
            return
        if s[index].isalpha():
            self.dfs(s, index + 1, path + s[index].upper(), res)
            self.dfs(s, index + 1, path + s[index].lower(), res)
        else:
            self.dfs(s, index + 1, path + s[index], res)

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        path = ""
        self.dfs(S, 0, path, res)
        return res

s = Solution()
test1 = "a1b2"
test2 = "3z4"
test3 = "12345"
print(s.letterCasePermutation(test3))