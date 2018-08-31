# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
#
# 示例:
#
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
# 进阶：
#
# 一个直观的解决方案是使用计数排序的两趟扫描算法。
# 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
# 你能想出一个仅使用常数空间的一趟扫描算法吗？

# 思路：设置两个指针，l记录第一个非0的位置，l左边为0，r记录第一个非2的位置，r右边
# 为2.然后使用i从头到尾扫一遍，直到与r相遇。i遇到0就换到左边去，遇到2就换到右边去，遇到1就跳过。
#
# 需要注意的是：
#
# 当遇到2就换到右边去，换回来的可能是0（或者1），i不能前进。因为如果换回来的是0，l在i前面，那么i前面会有1，要继续交换；
#
# 由此该数组分为4段：[0,left)-->0; [left,i)-->1; [i,right]-->乱序; (right,n-1]-->2

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 建立第一个分界标志，其左侧全是0
        first = i = 0  # fisrt 和 last 这种影响全局的变量，要先赋予默认值
        while i < len(nums):
            if nums[i] != 0:
                first = i
                break
            else:
                i += 1
        # 建立第二个分界标志，其右侧全是2
        last = j = len(nums) - 1
        while j > 0:
            if nums[j] != 2:
                last = j
                break
            else:
                j -= 1
         # 遍历 first 到 last 之间的元素
        index = first
        while index <= last:
            if nums[index] == 1:
                index += 1
            elif nums[index] == 2:
                nums[index], nums[last] = nums[last], nums[index]
                last -= 1  # 此时index 不改变，因为从last换过去的元素还未处理
            else:
                nums[index], nums[first] = nums[first], nums[index]
                first += 1
                index += 1
        # return nums  # do not return anything, change nums in-place

        # 答案之一 ：计数排序 -----------------------------------
        zero = nums.count(0)
        one = nums.count(1)
        two = nums.count(2)
        nums.clear()
        for i in range(zero):
            nums.append(0)
        for i in range(one):
            nums.append(1)
        for i in range(two):
            nums.append(2)


s = Solution()
nums = [2,0,2,1,1,0]
print(s.sortColors([0]))
print(nums)