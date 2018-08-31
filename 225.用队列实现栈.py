# 使用队列实现栈的下列操作：
#
# push(x) -- 元素 x 入栈
# pop() -- 移除栈顶元素
# top() -- 获取栈顶元素
# empty() -- 返回栈是否为空
# 注意:
#
# 你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
# 你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
# 你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0)) # 将q1中除尾元素外的所有元素转到q2中
        res = self.q1.pop(0)  # 弹出q1的最后一个元素
            # while self.q2.qsize>0:#将q2的元素转移到q1中
            # self.q1.put(self.q2.get())#这会出现超出时间显示错误,有实例不通过

        self.q1, self.q2 = self.q2, self.q1 # 交换q1,q2
        return res
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        res = self.q1.pop(0)
        self.q2.append(res)  # 与pop唯一不同的是需要将q1最后一个元素保存到q2中
        self.q1, self.q2 = self.q2, self.q1
        return res


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.q1) == 0:
            return True
        return False

        # Your MyStack object will be instantiated and called as such:
        # obj = MyStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.empty()
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.pop())

print(obj.empty())