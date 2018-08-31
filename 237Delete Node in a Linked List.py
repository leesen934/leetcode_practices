# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
# Given linked list -- head = [4,5,1,9], which looks like following:
#     4 -> 5 -> 1 -> 9
# Example 1:
#
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list
#              should become 4 -> 1 -> 9 after calling your function.
# Example 2:
#
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list
#              should become 4 -> 5 -> 9 after calling your function.
# Note:
#
# The linked list will have at least two elements.
# All of the nodes' values will be unique.
# The given node will not be the tail and it will always be a valid node of the linked list.
# Do not return anything from your function.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 要删除node，可以让node假装成node后面的结点，然后抛弃后面被利用完的小可怜结点
        # Because we know that the node we want to delete is not the tail of the list,
        # we can guarantee that this approach is possible.
        node.val = node.next.val
        node.next = node.next.next

        # 错误-------------------------
        # 注意：是用Solution类调用此方法，self是没有val和next属性的
        # if self.val == node.val:
        #     self.val = self.next.val
        #     self.next = self.next.next
        # else:
        #     cur = self.next
        #     back = self
        #     while cur.val != node.val:
        #         back = cur
        #         cur = cur.next
        #     back.next = cur.next

def printList(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    print(out)
node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node4 = ListNode(7)
node1.next = node2
node2.next = node3
node3.next = node4
s = Solution()
s.deleteNode(node3)
printList(node1)