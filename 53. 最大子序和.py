# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 暴力法 O(n^2)----------------------------------------------------------------
        # maximum = - 2 ** 31
        # for i in range(len(nums)):
        #     pre_sum = 0
        #     for j in range(i, len(nums)):
        #         pre_sum += nums[j]
        #         if pre_sum > maximum:
        #             maximum = pre_sum
        # return maximum

        # 动态规划 --------------------------------------------------------------------
        print(max(0, float('-inf')))
        max_sum = nums[0]
        pre_sum = nums[0]
        for i in range(1, len(nums)):
            pre_sum = max(pre_sum + nums[i], nums[i])
            max_sum = max(pre_sum, max_sum)
        return max_sum
        # 动态规划改变版 ------------------------------
        # 求和，然后判断和是否小于0，因为只要前面的和小于0，那么后面的数加上前面的和就一定比自身小，所以又重新求和，并和之前的最大子序和比较，取最大值。

        max_sub, prev_sub = float('-inf'), float('-inf')
        for n in nums:
            if prev_sub < 0:
                prev_sub = n  # 如果前面的和小0，那么重新开始求和
            else:
                prev_sub += n
            max_sub = max(max_sub, prev_sub)
        return max_sub


        # 分治法 O(n*logn) -------------------------------------------------------------
        return self.maxsubArray(nums, 0, len(nums) - 1)
    def maxsubArray(self, nums, left, right):
        if right == left:
            return nums[left]
        if left == right - 1:  # 不加这个判断的话会陷入死循环，lrm都相等，一直输出同一值。所以要在两个值的时候也遏制住，输入两个元素下所以子数组情况的最大值
            return max(nums[left] + nums[right], max(nums[left], nums[right]))
        else:
            mid = (right + left) // 2
            leftMSS = self.maxsubArray(nums, left, mid)
            rightMSS = self.maxsubArray(nums, mid + 1, right)
            crossMSS = self.maxCrossingSubArray(nums, left, mid, right)

            return max(crossMSS, max(leftMSS, rightMSS))

    def maxCrossingSubArray(self, nums, left, mid, right):
        left_sum = - 2 ** 31
        pre_sum = 0
        for i in reversed(range(left, mid)):  # 计算跨越中点的最大子数组时一定要数组每个元素都遍历到，并且mid只在某一段中读一次，不要重复前后两段都读
            # 注意range（）不取第二个参数，所以容易遗漏最尾巴的元素（right），改为range(mid,right+1)就好
            pre_sum += nums[i]
            if pre_sum > left_sum:
                left_sum = pre_sum
                left_max_index = i  # 也可以返回左侧最大子数组的左侧索引位置
        pre_sum = 0
        right_sum = - 2 ** 31
        for i in range(mid, right + 1):
            pre_sum += nums[i]
            if pre_sum > right_sum:
                right_sum = pre_sum
                right_max_index = i
        return max(left_sum + right_sum, max(left_sum, right_sum))  # 注意这里不仅考虑已经算好的左右两段（分别以mid结尾和mid开头）
        # 还要考虑左右两段连在一起的和


s = Solution()
test_6 = [-2,1,-3,4,-1,2,1,-5,4]
test2_8 = [1,-2,3,5,-3,2]
test3_9 = [0, -2, 3, 5, -1, 2]
test4__2 = [-9,-2,-3,-5,-3]
print(s.maxSubArray(test_6))