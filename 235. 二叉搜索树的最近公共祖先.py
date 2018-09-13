# 思路：
# 注意题目中有说这是一个BST。
# 那么满足左子树所有节点<根节点<右子树所有节点。
# 假设p.val < q.val，那么它们的最近公共祖先节点r，
# 一定满足：p.val <= r.val <=q.val。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        min_n = min(p.val, q.val)
        max_n = max(p.val, q.val)
        if root is None:
            return None
        if min_n <= root.val <= max_n:
            return root
        else:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            if left:
                return left
            if right:
                return right
