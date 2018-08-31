# -*- coding: utf-8 -*-
# 翻转一棵二叉树。
#
# 示例：
#
# 输入：
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# 输出：
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Edge 边界条件
        if not root:
            return

        # Swap 交换node，而不仅仅是交换val
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursion 迭代过程
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return 返回值
        return root
        # 答案一、另一种递归写法----------------------------------------
        if root == None:
            return
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root
        # 答案二，更快 -------------------------------------------------

        def helper(root):
            if not root:
                return
            else:
                root.left, root.right = helper(root.right), helper(root.left)  # 递归的同时完成交换
                return root

        return helper(root)
s = Solution()
root = TreeNode(4)
F1_1 = TreeNode(7)
F1_2 = TreeNode(2)
root.right = F1_2
root.left = F1_1
F2_1 = TreeNode(9)
F2_2 = TreeNode(6)
F2_3 = TreeNode(3)
F2_4 = TreeNode(1)
F1_1.left = F2_1
F1_1.right = F2_2
F1_2.left = F2_3
F1_2.right = F2_4
print(s.invertTree(root))