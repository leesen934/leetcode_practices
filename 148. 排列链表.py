# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
#
# 示例 1:
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 示例 2:
#
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归的归并排序 -----------------------------
        if head == None or head.next == None:
            return head
        # //slow move 1 step every time, fast move 2 step every time, pre record node before slow
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # change pre next to null, make two sub list(head to pre, slow to fast)
        right = slow.next
        slow.next = None

        res_l = self.sortList(head)
        res_r = self.sortList(right)
        return self.merge(res_l, res_r)

    def merge(self, l, r):
        tail = dummy = ListNode(0)

        while l and r:
            if l.val < r.val:
                tail.next = l
                l = l.next
            else:
                tail.next = r
                r = r.next
            tail = tail.next
        tail.next = l or r
        return dummy.next

        # 答案之一，用list 转换，但不符合题目要求--------------------------------------------------
        track = []
        while head:
            track.append(head.val)
            head = head.next
        heap = sorted(track)
        hold = result = ListNode(0)
        for item in heap:
            result.next = ListNode(item)
            result = result.next
        return hold.next

        # 迭代的归并排序，暂时看不懂 --------------------------------------
        # if head is None:
        #     return None
        #
        # def getSize(head):
        #     counter = 0
        #     while head is not None:
        #         counter += 1
        #         head = head.next
        #     return counter
        #
        # def split(head, step):
        #     i = 1
        #     while i < step and head:
        #         head = head.next
        #         i += 1
        #
        #     if head is None: return None
        #     # disconnect
        #     temp, head.next = head.next, None
        #     return temp
        #
        # def merge(l, r, head):
        #     cur = head
        #     while l and r:
        #         if l.val < r.val:
        #             cur.next, l = l, l.next
        #         else:
        #             cur.next, r = r, r.next
        #         cur = cur.next
        #
        #     cur.next = l if l is not None else r
        #     while cur.next is not None: cur = cur.next
        #     return cur
        #
        # size = getSize(head)
        # bs = 1
        # dummy = ListNode(0)
        # dummy.next = head
        # l, r, tail = None, None, None
        # while (bs < size):
        #     cur = dummy.next
        #     tail = dummy
        #     while cur:
        #         l = cur
        #         r = split(l, bs)
        #         cur = split(r, bs)
        #         tail = merge(l, r, tail)
        #     bs <<= 1
        # return dummy.next

    # 递归归并排序，写的好漂亮--------------------------------
    def merge_sort(self, head):
        if not head or not head.next:
            return head
        mid_next = self.get_middle(head)

        left = self.merge_sort(head)
        right = self.merge_sort(mid_next)
        return self.merge(left, right)

    def get_middle(self, head):
        current = head
        double_current = head.next
        while (double_current):
            double_current = double_current.next
            if double_current:
                double_current = double_current.next
                current = current.next
        current_next = current.next
        current.next = None
        return current_next

    def merge(self, left, right):
        pre_head = ListNode(None)
        current = pre_head
        while (right and left):
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        if not right:
            current.next = left
        else:
            current.next = right

        return pre_head.next



    # 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
node1 = ListNode(-1)
node2 = ListNode(5)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(0)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None
s = Solution()
print(s.sortList(node1))
a = 1