"""
1新建函数 allValueSame(grid)，判断网格所有值是否相等。这是判断网格是否为叶子结点的依据。
2若grid只有一个元素，那么必然为叶子结点，且此节点的val根据这元素的1/0来赋值True/False。
3若grid所有值相等，同2。
4若grid存在不相等的元素，那么此节点就不是叶子节点，需要把grid分成四份，分别递归调用四次。
5导入numpy.array，来完成二维数组（即网格）的切片操作。
"""


# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


from numpy import array


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        root = Node('*', True, None, None, None, None);
        if len(grid) == 1:
            root.isLeaf = True
            root.val = True if grid[0][0] == 1 else False
        if self.allValueSame(grid):  # 所有值相等
            root.isLeaf = True
            root.val = True if grid[0][0] == 1 else False
        else:  # 并非所有值相等
            halfLength = len(grid) // 2  # 使用 // 表示整除
            root.isLeaf = False  # 如果网格中有值不相等，这个节点就不是叶子节点
            # 使用array来完成二维数组的切片
            root.topLeft = self.construct(array(grid)[:halfLength, :halfLength].tolist())
            root.topRight = self.construct(array(grid)[:halfLength, halfLength:].tolist())
            root.bottomLeft = self.construct(array(grid)[halfLength:, :halfLength].tolist())
            root.bottomRight = self.construct(array(grid)[halfLength:, halfLength:].tolist())
        return root

    def allValueSame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: boolean
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[0][0] != grid[i][j]:
                    return False
        return True
