# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 回溯法 -----------------------------------
        def dfs(nums, temp, index):
            res.append(temp[:])  # 如果直接append（temp），后期temp的改变会影响res，因此做temp的一个副本
            if index == len(nums):
                return
            for j in range(index, len(nums)):
                temp.append(nums[j])
                dfs(nums, temp, j + 1)
                temp.pop()  # 返回上层去时要pop出去这层做出的改变
        res = []
        temp = []
        dfs(nums, temp, 0)
        return res

        # 组合？ -----------------------------------
        if not nums:
            return [[]]
        dp=[[]]
        n=len(nums)
        for i in range(n):
            temp=[item+[nums[i]] for item in dp]
            dp+=temp
        return dp

s = Solution()
test = [1,2,3]
print(s.subsets(test))