# 给定
# S
# 和
# T
# 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。  # 代表退格字符。
#
#
#
# 示例
# 1：
#
# 输入：S = "ab#c", T = "ad#c"
# 输出：true
# 解释：S
# 和
# T
# 都会变成 “ac”。
# 示例
# 2：
#
# 输入：S = "ab##", T = "c#d#"
# 输出：true
# 解释：S
# 和
# T
# 都会变成 “”。
# 示例
# 3：
#
# 输入：S = "a##c", T = "#a#c"
# 输出：true
# 解释：S
# 和
# T
# 都会变成 “c”。
# 示例
# 4：
#
# 输入：S = "a#c", T = "b"
# 输出：false
# 解释：S
# 会变成 “c”，但
# T
# 仍然是 “b”。
#
#
# 提示：
#
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S
# 和
# T
# 只含有小写字母以及字符
# '#'。

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.findString_keepOrder(S) == self.findString_keepOrder(T)
    def findString(self, old_s):
        skip = 0
        new_s = ""
        for i in old_s[::-1]:   # 字符串不能pop出栈，就逆序遍历, 最后再逆序一次就是结果
            if i == "#":  # 每个字符要想进入新字符串，先过第一关：不等于#
                skip += 1
            elif skip:  # 第二关 如果不等于#，还要看是否之前有#标记了这个字符要删除，只有跳跃的数目归为0，才能过这一关
                skip -= 1
            else:  # 终于打过两关，成功进入战队
                new_s += i
        return new_s[::-1]  # 因为之前是逆序遍历，现在再倒回正常顺序
    # 答案之一 ====================================================================

    def build_string(self, string):
        stack = []  # 借用list的出栈方法
        for s in string:
            if s != '#':
                stack.append(s)
            elif s == '#' and stack:
                stack.pop()
        return ''.join(stack)  # list转str方法！

    # 答案之一 ====================================================================
    # 此方法正常从头遍历字符串，没有用到双指针，也没问题
    def findString_keepOrder(self, old_s):
        new_s = ""
        for i in range(len(old_s)):
            if old_s[i] == "#":
                if len(new_s) > 0:
                    new_s = new_s[:-1]
            else:
                new_s += old_s[i]
        return new_s

    # ======================================================================================
    # 答案之一，确实写的厉害，用两个变量，一个做标记一个遍历数组也称为双指针，并非必须要都指向同一个数组

    # def backspaceCompare(self, S, T):
    #     return self.findString(S) == self.findString(T)
    #
    # def findString(self, S):
    #     skips = 0
    #     string1 = ""
    #     for char in S[::-1]:  # 字符串不能pop出栈，就逆序遍历
    #         if char == "#":
    #             skips += 1
    #         elif skips:
    #             skips -= 1
    #         else:
    #             string1 += char
    #     return string1[::-1]
s = Solution()
S = "a##c"
T = "#a#c"
print(s.backspaceCompare(S, T))