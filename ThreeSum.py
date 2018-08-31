# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# 分析一下这道题的特点，要我们找出三个数且和为0，那么除了三个数全是0的情况之外，肯定会有负数和正数，我们还是要先fix一个数，然后去找另外两个数，
# 我们只要找到两个数且和为第一个fix数的相反数就行了，既然另外两个数不能使用Two Sum的那种解法来找，如果能更有效的定位呢？
# 我们肯定不希望遍历所有两个数的组合吧，所以如果数组是有序的，那么我们就可以用双指针以线性时间复杂度来遍历所有满足题意的两个数组合。

# 我们对原数组进行排序，然后开始遍历排序后的数组，这里注意不是遍历到最后一个停止，而是到倒数第三个就可以了。
# 这里我们可以先做个剪枝优化，就是当遍历到正数的时候就break，为啥呢，因为我们的数组现在是有序的了，如果第一个要fix的数就是正数了，那么后面
# 的数字就都是正数，就永远不会出现和为0的情况了。然后我们还要加上重复就跳过的处理，处理方法是从第二个数开始，如果和前面的数字相等，就跳过，
# 因为我们不想把相同的数字fix两次。对于遍历到的数，用0减去这个fix的数得到一个target，然后只需要再之后找到两个数之和等于target即可。我们用
# 两个指针分别指向fix数字之后开始的数组首尾两个数，如果两个数和正好为target，则将这两个数和fix的数一起存入结果中。然后就是跳过重复数字的步
# 骤了，两个指针都需要检测重复数字。如果两数之和小于target，则我们将左边那个指针i右移一位，使得指向的数字增大一些。同理，如果两数之和大于
# target，则我们将右边那个指针j左移一位，使得指向的数字减小一些，代码如下：
#

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    out = []
    nums.sort()
    for i in range(len(nums) - 2):
        if len(nums)<3:
            return []
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = 0 - nums[i]
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                out.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] < target:
                while left < right:
                    left += 1
                    if nums[left] > nums[left - 1]:
                        break
            else:
                while left < right:
                    right -= 1
                    if nums[right] < nums[right + 1]:
                        break
    return out

    # ---------------- Second format -----------------
    # nums.sort()
    # result = []
    # for i in range(len(nums) - 2):
    #     if (i == 0 or nums[i] >= nums[i - 1]):
    #         left = i + 1
    #         right = len(nums) - 1
    #         while (left < right):
    #             if (nums[left] + nums[right] == -nums[i]):
    #                 if ([nums[i], nums[left], nums[right]] not in result):
    #                     result.append([nums[i], nums[left], nums[right]])
    #                 left += 1
    #                 right -= 1
    #                 while (left < right and nums[left] == nums[left - 1]):
    #                     left += 1
    #                 while (left < right and nums[right] == nums[right + 1]):
    #                     right -= 1
    #             elif (nums[left] + nums[right] < -nums[i]):
    #                 while (left < right):
    #                     left += 1
    #                     if (nums[left] > nums[left - 1]):
    #                         break
    #             else:
    #                 while (left < right):
    #                     right -= 1
    #                     if (nums[right] < nums[right + 1]):
    #                         break
    # return result

    # ------------------ best method -------------------------------------------
    freq = {}
    for elem in nums:
        freq[elem] = freq.get(elem, 0) + 1
    if 0 in freq and freq[0] > 2:
        res = [[0, 0, 0]]
    else:
        res = []
    neg = sorted((filter(lambda x: x < 0, freq)))
    nneg = sorted((filter(lambda x: x >= 0, freq)))
    for elem1 in neg:  # -4 -1
        for elem2 in nneg:  # 0 1 2
            target = -(elem1 + elem2)
            if target in freq:
                if target in (elem1, elem2) and freq[target] > 1:  # 此target为elem1, elem2其中一个
                    res.append([elem1, target, elem2])
                elif target > elem1 and target < elem2:  # 此target不为elem1或elem2
                    res.append([elem1, target, elem2])

    return res
    # ---------------------------------------------------------------------------
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))