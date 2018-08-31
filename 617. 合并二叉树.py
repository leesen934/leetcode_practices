# -*- coding: utf-8 -*-
# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
#
# 你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
#
# 示例 1:
#
# 输入:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# 输出:
# 合并后的树:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7
# 注意: 合并必须从两个树的根节点开始。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # 边界条件
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val  # 原地修改
        # 也可以重新分配内存，新建节点, 但速度慢很多 ----------------
        # root = TreeNode(t1.val + t2.val)
        # root.right = self.mergeTrees(t1.right, t2.right)
        # root.left = self.mergeTrees(t1.left, t2.left)
        # return root
        # ----------------------------------------------------------------
        # 递归
        t1.right = self.mergeTrees(t1.right, t2.right)  # 用此方法的结果更新调用此方法的树的右侧，而不仅是调用这个方法，注意返回值
        t1.left = self.mergeTrees(t1.left, t2.left)
        # 返回值
        return t1



s = Solution()
root = TreeNode(1)
F1_1 = TreeNode(3)
F1_2 = TreeNode(2)
root.right = F1_2
root.left = F1_1
F2_1 = TreeNode(5)
F1_1.left = F2_1

broot = TreeNode(2)
bF1_1 = TreeNode(1)
bF1_2 = TreeNode(3)
broot.right = bF1_2
broot.left = bF1_1
bF2_2 = TreeNode(4)
bF2_4 = TreeNode(7)
bF1_1.right = bF2_2
bF1_2.right = bF2_4
s.mergeTrees(root, broot)