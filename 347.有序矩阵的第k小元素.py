# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
# 请注意，它是排序后的第k小元素，而不是第k个元素。
#
# 示例:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# 返回 13。
# 说明:
# 你可以假设 k 的值永远是有效的, 1 ≤ k ≤ n2
class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
# 思路
# 直接求解矩阵中的第8小元素很难，我们可以用二分法设定一个值mid，查看mid值是否是矩阵第8小元素。
# 具体思路为：
# 1.首先设置mid的初值为矩阵matrix，最后一个数和第一个数的平均值。
# 2.统计矩阵中每一行小于mid值的个数之和。若该值小于8，记录当前mid，L = mid + 1，并更新mid；若该值大于8，R = mid - 1。
# 3.重复上述搜索，直至L和R不满足L <= R,此时的mid值即为所求。
        l = matrix[0][0]
        r = matrix[-1][-1]
        while l <= r:
            row = 0
            col = len(matrix) - 1
            cnt = 0
            mid = (l + r) >> 1
            while row < len(matrix) and col > -1:
                if matrix[row][col] <= mid:
                    cnt += col + 1
                    row += 1
                else:
                    col -= 1
            if cnt < k:
                l = mid + 1
            else:
                r = mid - 1
        return l



s = Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
print(s.kthSmallest(matrix, 8))

# N = len(matrix)
# l, r = matrix[0][0], matrix[-1][-1]
#
# while l <= r:
#     mid = (l + r) >> 1
#     high = N - 1
#     count = 0
#     for row in range(N):
#         while high > -1 and matrix[row][high] > mid:
#             high -= 1
#         count += high + 1
#
#     if count >= k:
#         r = mid - 1
#     else:
#         l = mid + 1
# return l
