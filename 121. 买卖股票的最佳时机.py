# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
#
# 注意你不能在买入股票前卖出股票。
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 示例 2:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 解题思路一（最好）： ---------------------------------------------------
# 动态规划
# 1.始终保存最小的买入价格
# 2.始终保存最大的利润
# 比如数据2,7,1，3
# 首先找到最小买入是2，然后做差7-2=5，保存利润，然后到最小买入变成1，此时利润还是5，然后到3，注意，这里就是核心了。
# 如果1后面出现的数字足够大，大到和1做差的值大于5，那么最大利润值就改变，否则，最大利润还是5.
# 这里暗含的逻辑是，后面的数如果减1的差肯定比减2的差来的大。

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = float("inf")
        res = 0
        for i in range(len(prices)):
            buy = min(prices[i], buy)
            res = max(prices[i] - buy, res)
        return res
# 二、 DP ---------------
        diff=[prices[i+1]-prices[i] for i in range(len(prices)-1)]
        maxSum=0
        Sum=0
        for num in diff:
            Sum+=num
            if Sum>maxSum:
                maxSum=Sum
            if Sum<0:
                Sum=0
        return maxSum
s = Solution()
test1 = [7,1,5,3,6,4]
test2 = [7, 6, 4, 3, 1]
print(s.maxProfit([]))