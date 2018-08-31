# 有一个二维矩阵A其中每个元素的值为0或1 。
# 移动是指选择任一行或列，并转换该行或列中的每一个值：将所有0都更改为1，将所有1都更改为0。
# 在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。返回尽可能高的分数。
# 示例：
#
# 输入：[[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
# 输出：39
# 解释：
# 转换为[[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]]
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
#
# 提示：
#
# 1 <= A.length <= 20
# 1 <= A[0].length <= 20
# A[i][j]是0或1

# 解题思路：

# 返回尽可能高分这个要求，理解为对同一组数，高位尽可能置1，对不同组的相同位尽可能多的置1。
#
# 上述即为本代码的流程：
#
# 1，判断最高位是否为1，否，移动当前行。
#
# 2，判断每列的的0的个数，如果0较多，移动当前列。
#
# 3，输出最高分数。
#

class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        m,n = len(A), len(A[0])

        def flipRow(row):
            for j in range(n):
                A[row][j] ^= 1
        def flipCol(col):
            for i in range(m):
                A[i][col] ^= 1
        for i in range(m):
            if A[i][0] == 0:
                flipRow(i)
        for j in range(n):
            if [A[i][j] for i in range(m)].count(0) > m // 2:
                flipCol(j)
        ans = 0
        for i in range(m):
            temp = 0
            for j in range(n):
                temp += A[i][j] << n - j - 1
            ans += temp

        return ans

        # 不太明白的高级答案---------------------------------------
        height, width = len(A), len(A[0])
        score = (1 << width - 1) * height
        for column in range(1, width):
            one_count = sum(A[row][column] == A[row][0] for row in range(height))
            score += max(height - one_count, one_count) * (1 << (width - 1 - column))
        return score

s = Solution()
test = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
print(s.matrixScore(test))