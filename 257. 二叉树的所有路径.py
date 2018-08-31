# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#
# 输入:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# 输出: ["1->2->5", "1->3"]
#
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # dfs + stack ,深度优先搜索+ 堆
        if not root:
            return []
        stack = [(root, "")]
        res = []

        # ["1->2->5", "1->3"]
        while stack:
            node, strr = stack.pop()
            if not node.right and not node.left:
                res.append(strr + str(node.val))
            if node.left:
                stack.append((node.left, strr + str(node.val) + "->"))
            if node.right:
                stack.append((node.right, strr + str(node.val) + "->"))
        return res


        # dfs recursively 递归dfs -----------------------------
        def binaryTreePaths(self, root):
            if not root:
                return []
            res = []
            self.dfs(root, "", res)
            return res

        def dfs(self, root, ls, res):
            if not root.left and not root.right:
                res.append(ls + str(root.val))
            if root.left:
                self.dfs(root.left, ls + str(root.val) + "->", res)
            if root.right:
                self.dfs(root.right, ls + str(root.val) + "->", res)
