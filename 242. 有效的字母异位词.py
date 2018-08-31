# -*- coding: UTF-8 -*-
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
# 说明:
# 你可以假设字符串只包含小写字母。
#
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 哈希表----------------------------
        if len(s) != len(t):
            return False
        dic1 = {}
        dic2 = {}
        for i in s:
            dic1[i] = dic1.get(i, 0) + 1
        for j in t:
            dic2[j] = dic2.get(j, 0) + 1

        return dic1 == dic2

        # 答案之一 ---------------------
        return sorted(s) == sorted(t)
        # 二 --------------------------
        # 用set整理去重字符串，str.count()计数判断
        return set(s) == set(t) and all(s.count(i) == t.count(i) for i in set(s))


s = Solution()
test1 = "cat"
test2 = "tab"
print(s.isAnagram(test1, test2))