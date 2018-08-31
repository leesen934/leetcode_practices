# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
#
# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
# 示例:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []  # 同步建立最小栈，新元素与最小栈最后的元素做对比，加入最小值到末尾

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            if x < self.min_stack[-1]:
                self.min_stack.append(x)
            else:
                self.min_stack.append(self.min_stack[-1])

    def pop(self):
        """
        :rtype: void
        """
        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
    # 超级慢的算法，自己写的 -------------------------------------------------
    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.stack = []
    #
    # def push(self, x):
    #     """
    #     :type x: int
    #     :rtype: void
    #     """
    #     self.stack.append(x)
    #
    # def pop(self):
    #     """
    #     :rtype: void
    #     """
    #     return self.stack.pop()
    #
    # def top(self):
    #     """
    #     :rtype: int
    #     """
    #     return self.stack[-1]
    # def getMin(self):
    #     """
    #     :rtype: int
    #     """
    #     min_s = float("Inf")
    #     for i in self.stack:  # 超级慢。。。
    #         if i < min_s:
    #             min_s = i
    #     return min_s


        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # --> 返回 -3.
print(minStack.pop())
print(minStack.top())  #      --> 返回 0.
print(minStack.getMin())