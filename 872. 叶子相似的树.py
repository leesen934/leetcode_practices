# 请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个叶值序列 。
#
# 如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是叶相似的。
#
# 如果给定的两个头结点分别为root1和root2的树是叶相似的，则返回true；否则返回false 。
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        # 因此可以借助堆栈的数据结构，由于堆栈是后进先出的顺序，由此可以先将右子树压栈，然后再对左子树压栈，
        #
        # 这样一来，左子树结点就存在了栈顶上，因此某结点的左子树能在它的右子树遍历之前被遍历。

        leaf1 = self.leaf_dfs(root1)
        leaf2 = self.leaf_dfs(root2)

        return leaf1 == leaf2

    def leaf_dfs(self,root):
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if not node.left and not node.right:
                res.append(node.val)

        return res

s = Solution()
print(s.leafSimilar())