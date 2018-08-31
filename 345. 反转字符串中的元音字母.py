# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
# 示例 1：
# 给定 s = "hello", 返回 "holle".
#
# 示例 2：
# 给定 s = "leetcode", 返回 "leotcede".
#
# 注意:
# 元音字母不包括 "y".

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        lib = "aeiouAEIOU"
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] not in lib:
                left += 1
            elif s[right] not in lib:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)

        # 也可以先找到一个固定下来，再去找另一个目标 ----------------
        l = 0
        r = len(s)-1
        _s = list(s)
        v = set('aeiouAEIOU')
        while l<r:
            if _s[l] in v:
                while _s[r] not in v:
                    r -= 1
                _s[l],_s[r] = _s[r],_s[l]
                r -= 1
            l += 1
        return "".join(_s)
        # ----------------------------------------------------

s = Solution()
test = "hello"
print(s.reverseVowels(test))