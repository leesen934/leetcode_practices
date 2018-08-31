# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。
# 递归求解，递归公式
# 　　f(n) = 0; n=null,
# 　　f(n) = 1+ max(f(n左)， f(n右))
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            max_depth = 1
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            max_depth += max(left_depth, right_depth)
            return max_depth

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(4)
    F1_1 = TreeNode(7)
    F1_2 = TreeNode(2)
    root.right = F1_2
    root.left = F1_1
    # F2_1 = TreeNode(9)
    # F2_2 = TreeNode(6)
    F2_3 = TreeNode(3)
    F2_4 = TreeNode(1)
    # F1_1.left = F2_1
    # F1_1.right = F2_2
    F1_2.left = F2_3
    F1_2.right = F2_4
    print(s.maxDepth(root))