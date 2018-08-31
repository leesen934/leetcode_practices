# 给定一个N叉树，返回其节点值的后序遍历。
#
#
#
# 例如，给定一个3叉树:
#      1
#    / | \
#   3  2  4
#  / \
# 5   6
# 返回其后序遍历: [5, 6, 3, 2, 4, 1].
#
# 说明: 递归法很简单，你可以使用迭代法完成此题吗?

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # val是节点的值，children是一个列表，这个列表保存了其所有节点。
        #
        # 递归法------------------------------------------------------
        # 后序遍历，如果通过递归还是非常简单的。对其子节点遍历，在对其本身节点遍历即可。
        # 由于所有的子节点是个列表，这样甚至比二叉树还要简单，只需对列表进行循环就行了。
        res = []
        if not root:
            return res
        else:
            for child in root.children:
                # 用extend就是保证每次给extend的值都是可迭代对象，因此上面的return都是输出列表格式
                res.extend(self.postorder(child))
            res.append(root.val)
        return res

        # 迭代法 ------------------------
        # 相当于前序BFS，只要pop一个节点，就push进该节点的子节点,但最后倒序输出结果
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack.extend(cur.children)  # children是list，要么显示for循环使用append，要么extend一个迭代器按元素加入堆
        return res[::-1]

