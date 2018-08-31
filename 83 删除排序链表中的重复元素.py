# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1:
#
# 输入: 1->1->2
# 输出: 1->2
# 示例 2:
#
# 输入: 1->1->2->3->3
# 输出: 1->2->3
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 好像我的更快哎------------------
        if head == None:
            return head
        prev = head
        cur = head.next
        while cur:
            print(str(prev.val) + '->' + str(cur.val))
            if cur.val != prev.val:
                prev.next = cur
                prev = cur
            else:
                prev.next = None
            cur = cur.next
            printList(head)
        return head

        # 新建一个链表，用集合set（）去重，新建节点加入到新链表中 ----------------
        p=dummy=ListNode(None)
        tmp = set()
        while head:
            if head.val not in tmp:
                p.next = ListNode(head.val)
                p = p.next
                tmp.add(head.val)
            # if p.val != head.val:
            #     if head.next:
            #         if head.next.val != p.val:
            #             p.next = head
            #     else:
            #         p.val = head.val
            #     p = p.next
            # tmp = head.val
            head = head.next or None
        return dummy.next

def printList(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    print(out)

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)
node4 = ListNode(1)
node5 = ListNode(2)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
s = Solution()
printList(node1)
a = s.deleteDuplicates(None)
printList(a)