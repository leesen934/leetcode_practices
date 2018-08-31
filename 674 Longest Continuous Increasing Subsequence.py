# 给定一个未经排序的整数数组，找到最长且连续的的递增序列。
#
# 示例 1:
#
# 输入: [1,3,5,4,7]
# 输出: 3
# 解释: 最长连续递增序列是 [1,3,5], 长度为3。
# 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。
# 示例 2:
#
# 输入: [2,2,2,2,2]
# 输出: 1
# 解释: 最长连续递增序列是 [2], 长度为1。
# 注意：数组长度不会超过10000。
class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # ------------------------
        # l = 1
        # res = [1]
        # for i in range(1, len(nums)):
        #     if nums[i] > nums[i-1]:
        #         l += 1
        #     else:
        #         l = 1
        #     res.append(l)
        # res.sort()
        # return res[-1]

        # 更好的方法,由于没有list内部操作，更快----------------
        cur_len = 1
        max_len = 1
        for j in range(1, len(nums)):
            if nums[j] > nums[j - 1]:
                cur_len +=1
                if cur_len > max_len:
                    max_len = cur_len
            else:
                cur_len = 1
        return max_len

s = Solution()
test = [1, 3, 5, 4, 7]
print(s.findLengthOfLCIS(test))