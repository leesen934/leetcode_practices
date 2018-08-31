# -*- coding: utf-8 -*-
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
# 示例 2:
#
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 示例 3:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # improved ------------------------------------------------------------
        # 使用贪心算法，只要可以产生利润（后一天比前一天股票价值上升），就进行一次买卖
        # 分割所有收益为两天的定量，如[1,2,3，4,5]，最终收益5-1=4，分割成(2-1) + (3-2) + (4-3) + (5-4) = 4
        profit = 0
        for i in range(len(prices)-1):   # index goes up to len(prices) - 2
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit

        # 自己的写的，慢 ---------------------------------------
        res = []
        i = 0
        j = 0
        if not prices:
            return []
        while i < len(prices) and j < len(prices):
            cnt = 0
            j = i + 1
            while j < len(prices):
                if prices[j] <= prices[i] or prices[j] <= prices[j-1]:
                    if j - i > 1:
                        res.append(prices[j-1] - prices[i])
                        i = j
                        break
                    else:
                        i += 1
                        break
                else:
                    j += 1
                    cnt += 1
        if cnt > 0:
            res.append(prices[j-1] - prices[i])
        return sum(res)

s = Solution()
test = [7,1,5,3,6,4]
test2 = [1,2,3,4,5]
print(s.maxProfit(test2))