# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # --------- 迭代 -------------------
    if not head:
        return []
    prev = None
    while head:
        cur = head
        head = head.next  # If you do cur.next = prev before head = head.next, you are modifying head because it is
        #  not a deep copy.However, if you do curr = ListNode(head.val), this solution will work just fine.
        cur.next = prev
        prev = cur
    return prev
    # -------- 递归 -------------------
    # def reverseList(self, head):
    #     return self._reverse(head)
    #
    # def _reverse(self, node, prev=None):
    #     if not node:
    #         return prev
    #     n = node.next
    #     node.next = prev
    #     return self._reverse(n, node)

# ------------------------------------------------------------------
def printList(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    print(out)

if __name__ == "__main__":

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    printList(node1)
    res = reverseList(node1)
    printList(res)