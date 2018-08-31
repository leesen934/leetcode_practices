# 我们把符合下列属性的数组
# A
# 称作山脉：
#
# 1.  A.length >= 3
# 2. 存在 0 < i < A.length - 1 使得A[0] < A[1] < ...< A[i - 1] < A[i] > A[i + 1] > ... > A[A.length - 1]
# 给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ...< A[i - 1] < A[i] > A[i + 1] > ... > A[A.length - 1] 的i的值。
#
# 示例
# 1：
#
# 输入：[0, 1, 0]
# 输出：1
# 示例
# 2：
#
# 输入：[0, 2, 1, 0]
# 输出：1
#
# 提示：
# 3 <= A.length <= 10000
# 0 <= A[i] <= 10 ^ 6
# A是如上定义的山脉
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        start , end = 0, len(A) - 1
        while start <= end:  # 二分查找注意while循环的条件判断中加等于，因为会出现start和end在同一索引情况，
                             # 此时要继续执行才能得出最终结果
            mid = (start + end) // 2
            if mid + 1 > len(A) - 1 or mid - 1 < 0:  # 注意mid+1 或 mid-1 会超出索引范围，不过此时也找到头尾了
                return mid
            if A[mid] < A[mid + 1]:
                start = mid + 1
            elif A[mid] < A[mid - 1]:
                end = mid - 1
            else:
                return mid

        # 答案之一 ： 从头遍历，一旦发现出现比后一个更大的值，就找到了峰值 -------
            for i in range(0, len(A) - 1, 1):
                if A[i] < A[i + 1]:
                    continue
                else:
                    return i

s = Solution()
test = [0,1,3,30]
print(s.peakIndexInMountainArray(test))
