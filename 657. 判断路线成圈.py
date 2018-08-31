# 初始位置 (0, 0) 处有一个机器人。给出它的一系列动作，判断这个机器人的移动路线是否形成一个圆圈，换言之就是判断它是否会移回到原来的位置。
#
# 移动顺序由一个字符串表示。每一个动作都是由一个字符来表示的。机器人有效的动作有 R（右），L（左），U（上）和 D（下）。输出应为 true 或 false，表示机器人移动路线是否成圈。
#
# 示例 1:
#
# 输入: "UD"
# 输出: true
# 示例 2:
#
# 输入: "LL"
# 输出: false
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        v = 0
        h = 0
        for i in range(len(moves)):
            if moves[i] == "R":
                v += 1
            elif moves[i] == "L":
                v -= 1
            elif moves[i] == "U":
                h += 1
            elif moves[i] == "D":
                h -= 1
        if v == 0 and h == 0:
            return True
        return False
        # 答案之一： 好聪明。判断L和R，U和D是不是成对存在，也就是个数是否相等
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
        # 答案之一 ：延展性比较好，用了二维坐标
        origin = [0, 0]
        mappings = {'U': [0, 1], 'D': [0, -1], 'L': [-1, 0], 'R': [1, 0]}
        for move in moves:
            origin[0] += mappings[move][0]
            origin[1] += mappings[move][1]
        return origin == [0, 0]

s = Solution()
test = "UD"
test2 = "LL"
print(s.judgeCircle('U'))