# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1 or not l2:
            return l1 or l2
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

# ------------------------------ Another format -------------------------
#         if not l1:
#             return l2
#
#         if not l2:
#             return l1
#
#         head = ListNode(0)
#         tail = head
#
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 tail.next = l1
#                 l1 = l1.next
#             else:
#                 tail.next = l2
#                 l2 = l2.next
#
#             tail = tail.next
#             tail.next = None
#
#         if l1 != None:
#             tail.next = l1
#         elif l2 != None:
#             tail.next = l2
#
#         return head.next
# ------------------------------------------------------------------
def printList(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    print(out)

# 从前插入：---------------------------------------------

# 被插入数据为空，返回
# 使用该输入数据创建一个节点，并将该节点指向原来头节点
# 设置该节点为头节点
# 时间复杂度和空间复杂度均为O(1)
def insertToFront(self,data):
    #功能：输入data，插入到头节点前，并更改为头节点
    #输出：当前头节点
    if data is None:
        return None
    node = ListNode(data)
    self.head = node
    return node
# -----------------------------------------------------
# 从后：append ----------------------------------------
# 若输入数据为空，返回None
# 若头节点为空，直接将输入数据作为头节点
# 遍历整个链表，直到当前节点的下一个节点为None时，将当前节点的下一个节点设置为输入数据
# 时间复杂度为O(n),空间O(1)

def append(self,data):
    #功能：输入data,作为节点插入到末尾
    if data is None:
        return None
    node = ListNode(data)
    if self.head is None:
        self.head = node
        return node
    curr_node = self.head
    while curr_node.next is not None:
        curr_node = curr_node.next
    curr_node.next = node
    return node

if __name__ == "__main__":

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)
    node1.next = node2
    node2.next = node3

    l1 = ListNode(1)
    l2 = ListNode(3)
    l3 = ListNode(4)
    l1.next = l2
    l2.next = l3

    printList(node1)
    printList(l1)
    res = mergeTwoLists(node1, l1)
    printList(res)
