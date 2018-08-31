# 给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。
#
# 示例 1:
#
# 输入: "2-1-1"
# 输出: [0, 2]
# 解释:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# 示例 2:
#
# 输入: "2*3-4*5"
# 输出: [-34, -14, -10, -10, 10]
# 解释:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        #  答案之一，写的简短漂亮的分治法 -----------------------------------------------
        # def helper(m, n, op):
        #     if op == "+":
        #         return m + n
        #     elif op == "-":
        #         return m - n
        #     else:
        #         return m * n
        #
        # if input.isdigit():  # isdigit() 如果字符串只包含数字则返回 True 否则返回 False。
        #     return [int(input)]
        # ans = []
        # for i in range(len(input)):
        #     if input[i] in "+-*":
        #         left = self.diffWaysToCompute(input[:i])
        #         right = self.diffWaysToCompute(input[i + 1:])
        #         ans.extend([helper(l, r, input[i]) for l in left for r in right])  # expend()是把参数里的每个内容添加到列表中
        #         #  而append()是往列表中添加以参数作为整体的一个对象
        # return ans

        #  自己写的，append和extend傻傻分不清 --------------------------------------
        def ways(inp):
            # if len(inp) == 1:  # 如果只通过一个长度判断是否是数字，报错，对于只输入“11”时，没有任何操作符号，直接返回就好
                # isdigit() 如果字符串只包含数字则返回 True 否则返回 False。
            if inp.isdigit():
                return [int(inp)]  # 就算是数字也统一返回列表格式，方便统一遍历取出元素
            sym = "+-*"
            ans = []
            for i in range(len(inp)):
                if inp[i] in sym:
                    lres = ways(inp[:i])
                    rres = ways(inp[i + 1:])
                    #  处理左右两侧返回来的结果
                    # append()表示 --------------------------------------
                    for j in lres:  # 其实这段重复性代码可以写成一个函数，更美观
                        for k in rres:
                            if inp[i] == '+':
                            # ans.extend([j + k])  # 这里必须用extend，讲答案作为一个个的元素加入ans，如果是append会出现嵌套列表，后面取元素运算时报错
                            #  但如果用append（）参数里每次只能是一个数字，不能是列表，才能作为元素加入
                                ans.append(j+k)
                            elif inp[i] == '-':
                                ans.append(j-k)
                            else:
                                ans.append(j*k)
                    # ------------------------------------
                    #  extend() 表示 --------------------
                    if inp[i] == '+':
                        for j in lres:
                            for k in rres:
                                ans.extend([j + k])
                    elif inp[i] == '-':
                        for j in lres:
                            for k in rres:
                                ans.extend([j - k])
                    else:
                        for j in lres:
                            for k in rres:
                                ans.extend([j * k])


            return ans

        return ways(input)

s = Solution()
test = "2-1-1"  # [2,0]
test1 = "2*3-4*5"  # [-34, -14, -10, -10, 10]
print(s.diffWaysToCompute(test1))