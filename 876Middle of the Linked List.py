# 给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。
#
# 示例 1：
# 输入：[1,2,3,4,5]
# 输出：此列表中的结点 3 (序列化形式：[3,4,5])
# 返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
# 注意，我们返回了一个 ListNode 类型的对象 ans，这样：
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
# 示例 2：
# 输入：[1,2,3,4,5,6]
# 输出：此列表中的结点 4 (序列化形式：[4,5,6])
# 由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def middleNode(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # 列表中点 ----------------------------------------------
    a = []
    while head:
        a.append(head.val)
        head = head.next
    print(a)
    return a[len(a) // 2:]  # //除数取整

    # 快慢指针-----------------------------------------------
    # 利用两个指针，一个步长为1一个为2，当2走到尾端，第一个走到的就是答案
    slow = fast = head
    while fast and fast.next:  # 必须两个条件都满足，因为循环体里有fast.next.next
        slow = slow.next
        fast = fast.next.next
    return slow.val

node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node4 = ListNode(7)
node1.next = node2
node2.next = node3
node3.next = node4
print(middleNode(node1))