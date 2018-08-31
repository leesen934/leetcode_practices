# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 说明:
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
# --------------------------------------------------
# O(NlogN)
# class Solution:
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         nums.sort()
#         return nums[-k]
# ---------------------------------------------------
from heapq import *
# class Solution:
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         heap = []     # 最小堆
#         for i in range(len(nums)):
#             if len(heap) < k:   # 如果堆中元素个数小于k，直接push进入堆
#                 heappush(heap,nums[i])
#             elif  heap[0] < nums[i]:    # 如果堆顶比新元素小，弹出堆顶
#                 heappop(heap)
#                 heappush(heap,nums[i])
#                 # heapreplace(heap, nums[i])     # 等价于以上两句
#         return heap[0]    # 返回堆顶
# -----------------------------------------------------------------------------------------------------
# I think this solution below is faster. It avoids doing the n-k heappop() operations.
# I use that fact that storing negative numbers in a min queue can be used as a max-queue. Just remember to do one more
# negation when you pop from the queue. This solution is O(n) for creating a negative list. Then O(n) for the heapify()
# and then O(k) for popping a few times to find the k:th item. So the final complexity is O(n).
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        neg = [-i for i in nums]
        heapq.heapify(neg)
        result = None
        for i in range(k):
            result = -heapq.heappop(neg)
        return result
s = Solution()
nums = [3,2,3,1,2,4,5,5,6]
nums2 = [3,2,1,5,6,4]
print(s.findKthLargest(nums, 2))