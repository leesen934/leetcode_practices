# 给定两个数组，写一个函数来计算它们的交集。
#
# 例子:
#
#  给定 num1= [1, 2, 2, 1], nums2 = [2, 2], 返回 [2].
#
# 提示:
#
# 每个在结果中的元素必定是唯一的。
# 我们可以不考虑输出结果的顺序。
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = set(nums1)
        n2 = set(nums2)
        res = list(n1 & n2)

        return res

        # 这才题目想让我们做的用双指针 -------------------
        a = 0
        b = 0
        nums1.sort()  # 排序之后才知道哪个指针应该往哪边移动，否则混乱了
        nums2.sort()
        if nums1 == [] or nums2 == []:
            return []
        intersection = []
        while a < len(nums1) and b < len(nums2):
            if nums1[a] == nums2[b]:
                if nums1[a] not in intersection:
                    intersection.append(nums1[a])
                a += 1
                b += 1
            elif nums1[a] < nums2[b]:
                a += 1
            elif nums2[b] < nums1[a]:
                b += 1


    # 比我快 ----------------
        nums1_set = set(nums1)
        res_set = set([num for num in nums2 if num in nums1_set])
        return list(res_set)

        # 写出花儿来了，用了二分查找法 --------------
        def binary_search(self, array, target):
            start, end = 0, len(array) - 1
            while start <= end:
                mid = (start + end) // 2
                if array[mid] == target:
                    return True
                elif target > array[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            return False

        def intersection(self, nums1, nums2):
            """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: List[int]
            """
            if len(nums2) < len(nums1):  # make 1st array always smaller
                nums1, nums2 = nums2, nums1
            nums1 = sorted(set(nums1))  # remove duplicates and sort
            result = set()
            for n2 in nums2:
                if self.binary_search(nums1, n2):
                    result.add(n2)
            return list(result)
s =Solution()
num1= [1, 2, 2, 1]
nums2 = [2, 2]
print(s.intersection(num1, []))