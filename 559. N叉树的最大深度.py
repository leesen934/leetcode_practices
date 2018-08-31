# 给定一个N叉树，找到其最大深度。
#
# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
# 说明:
#
# 树的深度不会超过 1000。
# 树的节点总不会超过 5000。

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # 　　f(n) = 0; n=None,
        # 　　f(n) = 1+ max(f(n.children))
        if not root:
            return 0
        elif not root.children:
            return 1
        else:
            # ()包围着生成一个生成器generator，即用即存取
            # []包围则生成list，占内存
            # 也可以先列表生成式，再max ： max([self.maxDepth(child) for child in root.children])
            max_depth = 1 + max(self.maxDepth(child) for child in root.children)
            return max_depth

        # 自己写的很罗嗦的代码 ----------------------------
        # else:
        #     child_depth = []
        #     for child in root.children:
        #         child_depth.append(self.maxDepth(child))
        #     if len(child_depth) > 0:
        #         max_depth = 1 + max(child_depth)
        #     else:
        #         max_depth = 1
        #         map(self.maxDepth, root.children)
        #     return max_depth