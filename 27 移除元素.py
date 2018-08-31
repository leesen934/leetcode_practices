# 给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。 O(1):常量空间, 和n无关
#
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
#
# 示例 1:
#
# 给定 nums = [3,2,2,3], val = 3,
#
# 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
#
# 你不需要考虑数组中超出新长度后面的元素。
# 示例 2:
#
# 给定 nums = [0,1,2,2,3,0,4,2], val = 2,
#
# 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
#
# 注意这五个元素可为任意顺序。
#
# 你不需要考虑数组中超出新长度后面的元素。
# 说明:
#
# 为什么返回数值是整数，但输出的答案是数组呢?
#
# 请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
#
# 你可以想象内部操作如下:
#
# // nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
# int len = removeElement(nums, val);
#
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 双头指针 -------------------------------
        # left = 0
        # for right in range(len(nums)):
        #     if nums[right] != val:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         left += 1
        # return left

        # 头尾指针 -------------------------------
        # 反向时，交换后的数组元素顺序镜像，也可以用来分类奇偶数

        i = 0
        j = len(nums)-1
        while i <= j:
            if nums[i] != val:
                i += 1
            else:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                j -= 1
        return (i if i > j else 0)

        # -----------------------------------------
        # 好聪明，遍历所有元素，一旦值相同，del删除数组中此元素，输出最后剩下的数组长度
        # l = len(nums)
        # for i in range(l):
        #     if nums[i] == val:
        #         del nums[i]
        #         l -= 1
        # return l


s = Solution()
test = [0,1,2,2,3,0,4,2]
res = s.removeElement(test, 2)
print(res)
print(test[:res])