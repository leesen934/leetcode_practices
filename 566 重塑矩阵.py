# 在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。
#
# 给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。
#
# 重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。
#
# 如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
#
# 示例 1:
#
# 输入:
# nums =
# [[1,2],
#  [3,4]]
# r = 1, c = 4
# 输出:
# [[1,2,3,4]]
# 解释:
# 行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。
# 示例 2:
#
# 输入:
# nums =
# [[1,2],
#  [3,4]]
# r = 2, c = 4
# 输出:
# [[1,2],
#  [3,4]]
# 解释:
# 没有办法将 2 * 2 矩阵转化为 2 * 4 矩阵。 所以输出原矩阵。
# 注意：
#
# 给定矩阵的宽和高范围在 [1, 100]。
# 给定的 r 和 c 都是正数。

class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # if len(nums) == 0:
        #     return nums
        # r_len = len(nums)
        # c_len = len(nums[0])
        # if r * c != r_len * c_len:
        #     return nums
        # res = []
        # temp = []
        # count = 0
        # for row in nums:
        #     for i in row:
        #         if count != c:
        #             temp.append(i)
        #             count += 1
        #             if count == c:
        #                 res.append(temp)
        #                 count = 0
        #                 temp = []
        # return res

        # 复杂度更低的算法，多维数组捋成一维数组，超酷炫 ---------------

        if not nums or not nums[0]:
            return []

        if r * c != len(nums) * len(nums[0]):
            return nums

        res = []

        sub = []
        for i in nums:
            sub.extend(i)

        i = 0
        # 一次添加一行，帅气，注意下标的计算
        while i < len(sub):
            res.append(sub[i:i + c])
            i += c

        return res

        # 最好的算法 ------------------------------
        # if r*c != len(nums)*len(nums[0]):
        #     return nums
        # lst = [m for row in nums for m in row]  # 这个写法要创建一个新列表接收，不改变原列表
        # res = (lst[i*c:i*c+c] for i in range(r))
        # return list(res

s = Solution()
test =[[1, 2], [3, 4], [5, 6]]
r = 2
c = 3
print(s.matrixReshape(test, r, c))