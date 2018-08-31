# 机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：
#
# -2：向左转 90 度
# -1：向右转 90 度
# 1 <= x <= 9：向前移动 x 个单位长度
# 在网格上有一些格子被视为障碍物。
#
# 第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])
#
# 如果机器人试图走到障碍物上方，那么它将停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。
#
# 返回从原点到机器人的最大欧式距离的平方。
#
#
#
# 示例 1：
#
# 输入: commands = [4,-1,3], obstacles = []
# 输出: 25
# 解释: 机器人将会到达 (3, 4)
# 示例 2：
#
# 输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# 输出: 65
# 解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
#
#
# 提示：
#
# 0 <= commands.length <= 10000
# 0 <= obstacles.length <= 10000
# -30000 <= obstacle[i][0] <= 30000
# -30000 <= obstacle[i][1] <= 30000
# 答案保证小于 2 ^ 31
#

# 理解本题的题意很关键，机器人在（0，0）点开始行走，如果（0，0）点有障碍怎么办，这种情况是不管它，开始下一步行走，一旦机器人离开（0，0）点，
# 这个点的障碍物才生效，后面如果回到此点则不能跨过此障碍。也就是说我们需要先走一步，再去判断这一步是否有效，有效则更新坐标，否则原地不动，
# 继续下一次动作。至于右转和左转实际就是改变机器人的朝向，起初机器人向北，右转则朝向东，左转则朝向西。不同的朝向，意味着向前一步改变的坐标形式
# 不一样，如果朝北，则x不动，y递增；如果朝南，则x不动，y递减；如果朝西，则x递减，y不动；如果朝东，则x递增，y不动；也就是在每次实施除了左转右
# 转的动作（调整朝向）之外的移动操作时，需要知道机器人的朝向。知道了朝向就往前走呗，遇到了前方障碍物则不要往前，结束此次动作，开始下一次动作。
# 方法二，优化方向的表示，如果用坐标来表示方向不仅可以很好的确定方向之间的关系，而且还能确定此方向上的增量。考虑[0,1]，[1,0]，[0,-1]，[-1,0]
# 分别代表北、东，南，西。可以看到每个坐标的左边就是它的左转方向，右边的就是它的右边方向，也就是说，给一个方向i(方向向量的索引)，则左转的方向
# 是i-1，右转的方向是i+1。等等，那两头呢，开始的位置不能减1，末端的位置不能加1。把首和尾连接器起来就好了，因此要进行取余操作，长度为4。当然了
# (0-1)%4没意义,因此改写成（（0-1）+4）%4,即左转为（i+3）%4，这样对中间位置和起始位置都适用。方向确定好了。那坐标增量呢，注意到某一方向上行
# 进一步的增量恰好就是该方向的坐标。以北为例，y方向增量是1，x方向增量是0，也就是（0，1）。这种方法可以大大减少代码量

class Solution(object):
    def robotSim(self, commands, obstacles):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obst = set(map(tuple, obstacles))  # 必须注意使用 集合 Set 作为对障碍物使用的数据结构，以便我们可以有效地检查下
        # 一步是否受阻。如果不这样做，我们检查 该点是障碍点吗 可能会慢大约 10000 倍。
        maxdis = 0
        for cd in commands:
            if cd == -2:
                di = (di - 1) % 4
            elif cd == -1:
                di = (di + 1) % 4
            else:
                for i in range(cd):
                    if (x+dx[di], y+dy[di]) not in obst:
                        x += dx[di]
                        y += dy[di]
                        maxdis = max(maxdis, x*x + y*y)
                    else:
                        break
        return maxdis

        # 答案2 ------------------------------------------------
        # 用组合起来的xy坐标作为方向
        # directions = ['N', 'E', 'S', 'W']
        # 0 - N, 1 - E, 2 - S, 3 - W
        # position_offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # obstacles = set(map(tuple, obstacles))  # set:{...}
        # x, y, direction, max_distance = 0, 0, 0, 0
        # for command in commands:
        #     if command == -2:
        #         direction = (direction - 1) % 4
        #     elif command == -1:
        #         direction = (direction + 1) % 4
        #     else:
        #         x_off, y_off = position_offset[direction][0], position_offset[direction][1]
        #         while command > 0:
        #             if (x+x_off, y+y_off) not in obstacles:
        #                 x += x_off
        #                 y += y_off
        #             command -= 1
        #             max_distance = max(max_distance, x**2 + y**2)
        # return max_distance


s = Solution()
commands = [4, -1, 4, -2, 4]
obstacles = [[2, 4]]
print(s.robotSim(commands, obstacles))