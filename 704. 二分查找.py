# 给定一个n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums中的 target，如果目标值存在返回下标，否则返回 - 1。
#
# 示例1:
#
# 输入: nums = [-1, 0, 3, 5, 9, 12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
# 示例2:
#
# 输入: nums = [-1, 0, 3, 5, 9, 12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 - 1
#
# 提示：
#
# 你可以假设 nums 中的所有元素是不重复的。 n 将在[1, 10000] 之间。nums 的每个元素都将在[-9999, 9999] 之间。
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1



s = Solution()
test = [-1, 0, 3, 5, 9, 12]
print(s.search(test, 12))

