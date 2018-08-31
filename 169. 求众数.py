#
# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在众数。
#
# 示例 1:
#
# 输入: [3,2,3]
# 输出: 3
# 示例 2:
#
# 输入: [2,2,1,1,1,2,2]
# 输出: 2

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 答案之一：分治法 ------------------------------------------------------------------
        # 分治法是将整个问题化简为一个一个的小问题去解，将数组分成简单的几部分，比如讲一组数分为两部分，第一部分的众数如果等于第二部分的众数，
        # 则这个数就是上一层那一组的众数，如果第一部分不等于第二部分，则遍历这一组数，记录这两个数的出现频率，返回为频率最大的，
        # 如果频率相同，返回谁都无所谓，因为在这里众数x肯定存在的，那么肯定会有至少两个x相连，如果不相连的话，那最后一个数字肯定是众数x。
        # （例如：1 2 1 2 1 2 1，12112）。时间复杂度为o(n)。

        def find(nums, begin, end):
            if (begin == end):
                return nums[begin]
            else:
                mid = (begin+end) // 2
                left = find(nums, begin, mid)
                right = find(nums, mid+1, end)

            if left == right:  # 左右两部分的众数相同 则这个数是这部分的众数
                return left;
            else:  # 左右两部分的众数不相同则这两个数都有可能是这部分的众数,那么遍历这个数组看一下哪个数字的出现频率高
                countLeft = 0
                countRight = 0
                for i in range(begin, end+1):
                    if nums[i] == left:
                        countLeft += 1
                    elif nums[i] == right:
                        countRight += 1
                if countLeft > countRight:
                    return left
                else:
                    return right

        return find(nums, 0, len(nums) - 1)
        # 答案之一：摩尔投票算法（Moore voting algorithm）------------------------------------------

        # 每次从数组中找出一对不同的元素，将它们从数组中删除，直到遍历完整个数组。
        # 由于这道题已经说明一定存在一个出现次数超过一半的元素，所以遍历完数组后数组中一定会存在至少一个元素。

        # --------------------------------------------------------------------------------------
        # 答案之一： 因为众数是出现次数大于n/2的数字，所以排序之后中间的那个数字一定是众数。即nums[n/2]为众数
        return sorted(nums)[len(nums) / 2]

        # --------------------------------------------------------------------------------------
        # 答案之一，set去重之后，用已有方法count()统计出现次数，如果满足要求就直接输出
        tmp = list(set(nums))
        for i in tmp:
            if nums.count(i) > len(nums)/2:
                return i

        # 自己写的,有点长,速度也不如答案-------------------------------------------------------------
        count = len(nums) // 2
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for k, v in dic.items():
            if v > count:
                return k
        return None

s = Solution()
test = [2,2,1,1,1,2,2]
print(s.majorityElement(test))


