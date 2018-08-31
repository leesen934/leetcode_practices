# 给定一个没有重复数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.gen(nums, [], res)
        return res

    def gen(self, nums, temp, res):
        if len(temp) == len(nums):
            res.append(temp[:])  # 记得要深复制，否则res里的temp会受影响
            return
        for j in range(len(nums)):
            if nums[j] in temp:
                continue
            temp.append(nums[j])
            self.gen(nums, temp, res)
            temp.pop()  # 返回上级时记得pop出去刚才做的改变，变成原样继续找别的路



s = Solution()
test = [1,2,3]
print(s.permute(test))