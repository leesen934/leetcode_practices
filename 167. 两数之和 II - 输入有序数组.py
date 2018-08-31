#
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
#
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
#
# 说明:
#
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
# 示例:
#
# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 第一种
        # 双指针方法：解决有序数组中元素之间存在某种关系的问题
        s, e = 0, len(numbers) - 1
        while s < e:
            if numbers[s] + numbers[e] > target:
                e -= 1
            elif numbers[s] + numbers[e] < target:
                s += 1
            else:
                return s+1, e+1


    # 第二种　最快
    # 字典方法：注意此时输出是数组索引，那么就将索引设置为字典的值，键就为加和可以是目标值的元素
    def twoSum2(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num] + 1, i + 1]
            dic[num] = i
    #　第三种
    # 二分法：外层是从头到尾遍历数组固定一个数ｉ，内层从［ｉ＋１：］查找另一个目标值，复杂度高，超出时间限制
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1

        # ------------------------------------------------------------------
        # 自己第一次写的，超出时间限制。。。。因为外层还是从头到尾遍历，里层才是二分查找，复杂度还是太高
#         def binary_search(nums, t):
#             start, end = 0, len(nums) - 1
#             while start <= end:
#                 mid = (start + end) // 2
#                 if nums[mid] == t:
#                     return mid
#                 elif nums[mid] < t:
#                     start += 1
#                 else:
#                     end -= 1
#             return -1
#
#         for i in range(len(numbers)):
#             if numbers[i] < 0:
#                 j = binary_search(numbers[i + 1:], target - numbers[i])
#                 if j >= 0:
#                     return i+1, j+i+1+1
#             elif numbers[i] >= 0:
#                 j = binary_search(numbers[:i], target - numbers[i])
#                 if j >= 0:
#                     return j+1, i+1
s = Solution()
test = [-2,-1,0,3,7]
print(s.twoSum(test, 2))