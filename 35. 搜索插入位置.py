# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素
# 示例 1:
#
# 输入: [1,3,5,6], 5
# 输出: 2
# 示例 2:
#
# 输入: [1,3,5,6], 2
# 输出: 1
# 示例 3:
#
# 输入: [1,3,5,6], 7
# 输出: 4
# 示例 4:
#
# 输入: [1,3,5,6], 0
# 输出: 0
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start , end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return end + 1
        # -------------------------------------------------
        # 答案之一，没有用二分法，只达到题目要求 ，利用有序性找到插入的合适位置
        n = len(nums)
        if target > nums[n-1]:
            return n
        for k in range(n):
            if target <= nums[k]:
                return k
        # ---------------------------------------------------
        # 答案之一，用递推来写二分法，速度不错
        def rec(nums, target, lower, upper):
            if (lower > upper):
                return lower
            mid = int((upper + lower) / 2)
            if (nums[mid] > target):
                return rec(nums, target, lower, mid - 1);
            elif (nums[mid] < target):
                return rec(nums, target, mid + 1, upper);
            else:
                return mid

        class Solution:
            def searchInsert(self, nums, target):
                return (rec(nums, target, 0, len(nums) - 1))
        # ----------------------------------------------------
        # 答案之一 如果没找到target，直接append到尾巴，然后sort排序，再遍历全部元素找到target此刻的位置并返回其索引
        if target in nums:
            for i in range(len(nums)):
                if target == nums[i]:
                    return i
        else:
            nums.append(target)
            nums.sort()
            for i in range(len(nums)):
                if target == nums[i]:
                    return i

s = Solution()
test = [1,3,5,6]
print(s.searchInsert(test, 5))