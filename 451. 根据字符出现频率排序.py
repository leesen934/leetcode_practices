#
# 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
#
# 示例 1:
#
# 输入:
# "tree"
#
# 输出:
# "eert"
#
# 解释:
# 'e'出现两次，'r'和't'都只出现一次。
# 因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
# 示例 2:
#
# 输入:
# "cccaaa"
#
# 输出:
# "cccaaa"
#
# 解释:
# 'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
# 注意"cacaca"是不正确的，因为相同的字母必须放在一起。
# 示例 3:
#
# 输入:
# "Aabb"
#
# 输出:
# "bbAa"
#
# 解释:
# 此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
# 注意'A'和'a'被认为是两种不同的字符。

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 自己理解后的 ----------------------------------------
        dic = {}
        for item in set(s):
            dic[item] = s.count(item)
        # TypeError: must use keyword argument for key function, key= lambda x: x[1]
        tmp = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return "".join(j[0]*j[1] for j in tmp)

        # O(n) ------------------------------------------
        from collections import Counter
        c1, c2 = Counter(s), {}
        for k, v in c1.items():
            c2.setdefault(v, []).append(k*v)
        return "".join(["".join(c2[i]) for i in range(len(s), -1, -1) if i in c2])


        # dic = {}
        # res = []
        # for i in s:
        #     if i not in dic:
        #         dic[i] = 1
        #     else:
        #         dic[i] += 1
        # cnt = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        # for i in cnt:
        #     temp = list(i[0]) * i[1]
        #     res.extend(temp)
        # return res  # 搞错了，题目要求最后返回字符串，不是列表，此法时间太慢。。。。

s = Solution()
print(s.frequencySort('tree'))