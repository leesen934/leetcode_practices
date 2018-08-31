# 设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。
#
# 你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。
#
# 示例:
#
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8
# 说明:
# 你可以假设 nums 的长度≥ k-1 且k ≥ 1。
import heapq
class KthLargest:
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums
        self.length = len(self.heap)
        heapq.heapify(self.heap)  # Transform list into a heap, in-place
        while self.length > self.k:
            heapq.heappop(self.heap)
            self.length -= 1


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.length < self.k:
            heapq.heappush(self.heap, val)
            self.length += 1
        elif val > self.heap[0]:  # elif 不是 if ，只能两种情况之一，要么长度不够，直接加进去，就不再replace了，要么就长度够，
            # 直接检测最小值的对比，判断是否replace
            heapq.heapreplace(self.heap, val)
        return self.heap[0]
    # def __init__(self, k, nums):
    #     self.pool = nums
    #     self.k = k
    #     self.size = len(self.pool)
    #     heapq.heapify(self.pool)
    #     while self.size > k:
    #         heapq.heappop(self.pool)
    #         self.size -= 1
    #
    # def add(self, val):
    #     if self.size < self.k:
    #         heapq.heappush(self.pool, val)
    #         self.size += 1
    #     elif val > self.pool[0]:
    #         heapq.heapreplace(self.pool, val)
    #     return self.pool[0]

    # def __init__(self, k, nums):
    #     """
    #     :type k: int
    #     :type nums: List[int]
    #     """
    #     self.k = k
    #     self.nums = sorted(nums, reverse=True)
    #
    # def add(self, val):
    #     """
    #     :type val: int
    #     :rtype: int
    #     """
    #     if not self.nums:
    #         self.nums.append(val)
    #         return val
    #     else:
    #         s = 0
    #         e = len(self.nums) - 1
    #         while s <= e:
    #             m = (s + e) >> 1
    #             if self.nums[m] <= val:
    #                 e = m - 1
    #             elif self.nums[m] > val:
    #                 s = m + 1
    #             else:
    #                 break
    #         self.nums.insert(s, val)
    #
    #         return self.nums[self.k - 1]



        # Your KthLargest object will be instantiated and called as such:
        # obj = KthLargest(k, nums)
        # param_1 = obj.add(val)
test = [4,5,8,2]
obj = KthLargest(3, test)
print(obj.add(3))  # 4
print(obj.add(5))  # 5
print(obj.add(10))  # 5
print(obj.add(9))  # 8
print(obj.add(4))  # 8