# 给定两个数组，编写一个函数来计算它们的交集。
#
# 示例 1:
#
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]
# 示例 2:
#
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]
# 说明：
#
#    输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
#    我们可以不考虑输出结果的顺序。
# 进阶:
#
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1 = {}
        dic2 = {}
        res = []
        for i in nums1:
            dic1[i] = dic1.get(i, 0) + 1
        for j in nums2: # 没必要多建立一个字典，直接用另一个查阅已存在的字典，如key存在则加入结果中，计数器-1就好
            dic2[j] = dic2.get(j, 0) + 1
        for k, v in dic1.items():
            if k in dic2:
               res.extend([k] * min(v, dic2[k]))

        return res

        # 答案之一 --------------------------------------------
        # 对长度相差大的两个数组更友好更快速
        #  nums1 = [4,9,5]
        #  nums2 = [9,4,9,8,4]

        l1 = len(nums1)
        l2 = len(nums2)
        return self.intersectionHelper(nums1, nums2) if l1 < l2 else self.intersectionHelper(nums2, nums1)

    # len(num1) <= len(num2)
    def intersectionHelper(self, nums1, nums2):
        # store the nums2 using a counting dictionary
        # 依据长数组建立字典，查阅计数
        count = {}
        res = []
        for n in nums2:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        for n in nums1:
            if n in count and count[n] > 0:
                res.append(n)
                count[n] -= 1  # 出现子集并添加到结果后更新计数
        return res

        # 答案二---------------------------------------
        dict1 = dict()
        for i in nums1:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        ret = []
        for i in nums2:
            if i in dict1 and dict1[i]>0:
                ret.append(i)
                dict1[i] -= 1
        return ret

s = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(s.intersect(nums1, nums2))