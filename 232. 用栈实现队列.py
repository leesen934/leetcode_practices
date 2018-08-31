#
# 使用栈实现队列的下列操作：
#
# push(x) -- 将一个元素放入队列的尾部。
# pop() -- 从队列首部移除元素。
# peek() -- 返回队列首部的元素。
# empty() -- 返回队列是否为空。
# 示例:
#
# MyQueue queue = new MyQueue();
#
# queue.push(1);
# queue.push(2);
# queue.peek();  // 返回 1
# queue.pop();   // 返回 1
# queue.empty(); // 返回 false
# 说明:
#
# 你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
# 假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        temp = []
        for i in range(len(self.queue)):
            temp.append(self.queue.pop())
        res = temp.pop()
        while len(temp) != 0:
            self.queue.append(temp.pop())  # 恢复queue原样，但其实增加了复杂度，可以参考下面的答案，一开始就初始化两个list，一正一反
        return res

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        temp = []
        for i in range(len(self.queue)):
            temp.append(self.queue.pop())
        res = temp[-1]
        while len(temp) != 0:
            self.queue.append(temp.pop())
        return res
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.queue) == 0:
            return True
        return False

    # 最快的答案 --------------------------------------------------------------------------
    # 可以直接初始化两个全局stack，一个顺序排放元素，一个逆序元素
    def __init__(self):
        '''
        Initialize your data structure here.
        '''
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        '''
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        '''
        self.stack1.append(x)
        # assume stack2 is empty, put element on top of stack1

    def peek(self):
        '''
        Get the front element
        :rtype: int
        '''
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    # stack2 is empty, move elements from stack1 to stack2 one by one, ex: stack1 = [1, 2, 3], stack2 = [3, 2, 1],
    # and return the last one of stack2, which is the first element of queue:1
    def pop(self):
        '''
        Remove the element from in front of queue and returns the element
        '''
        self.peek()
        return self.stack2.pop()

    # stack2 = [3, 2, 1], stack2.pop() = 1, self.peek() = 1

    def empty(self):
        '''
        Returns whether the queue is empty
        :rtype:bool
        '''
        return len(self.stack1) == 0 and len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
# print(obj.peek())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.empty())