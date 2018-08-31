# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
# 示例 3:
#
# 输入: "(]"
# 输出: false
# 示例 4:
#
# 输入: "([)]"
# 输出: false
# 示例 5:
#
# 输入: "{[]}"
# 输出: true

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 == 1:
            return False
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if i == ')' and stack[-1] == "(":
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(i)
        if not stack:
            return True
        return False

        # 答案之一 更快 ---------------------------------------------------------------------------
        dic = {')': '(', ']': '[', '}': '{'}
        ts = []
        for t in s:
            if t in ['(', '[', '{']:
                ts.append(t)
            elif t in [')', ']', '}']:
                if len(ts) == 0 or dic[t] != ts.pop():
                    return False

        return ts == []


s = Solution()
test = "{[}]"
print(s.isValid(test))