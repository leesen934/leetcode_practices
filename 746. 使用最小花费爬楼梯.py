#
# 数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
#
# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
#
# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
#
# 示例 1:
#
# 输入: cost = [10, 15, 20]
# 输出: 15
# 解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
#  示例 2:
#
# 输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出: 6
# 解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
# 注意：
#
# cost 的长度将会在 [2, 1000]。
# 每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。

# 到达终点i只能是两种方式，一种从i-1过来，一种从i-2过来，因此第i阶的成本为： step[i] = min(step[i-1]+cur, step[i-2] + cur)
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) <= 1:
            return 0
        curMin = cost[1]
        preMin = cost[0]
        for i in range(2, len(cost)):
            preMin, curMin = curMin, cost[i] + min(preMin, curMin)
        return min(preMin, curMin)  # 最后到末尾的后一个台阶为终点，也是两种方法，可以从末尾过去或者从末尾前一阶过去，所以取两者最小值

s = Solution()
test = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(s.minCostClimbingStairs([1,2]))
