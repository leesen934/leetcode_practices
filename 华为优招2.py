# 小偷来到了一个神秘的王宫，突然眼前一亮，发现5个宝贝，每个宝贝的价值都不一样，且重量也不一样，但是小偷的背包携带重量
# 有限，所以他不得不在宝贝中做出选择，才能使偷到的财富最大，请你帮助小偷计算一下。
# 输入描述:
# 宝贝价值：6,3,5,4,6
# 宝贝重量：2,2,6,5,4
# 小偷背包容量：10
# 输出描述:
# 偷到宝贝的总价值：15

# 输入
# 6,3,5,4,6
# 2,2,6,5,4
# 10
# 输出
# 15
# value = [6,3,5,4,6]
# weight = [2,2,6,5,4]
# max_bag = 10
import sys
line = sys.stdin.readline().strip()
value = list(map(int, line.split(",")))
line = sys.stdin.readline().strip()
weight = list(map(int, line.split(",")))
max_bag = int(sys.stdin.readline().strip())

num = len(value)
table = [[0 for i in range(max_bag + 1)] for j in range(num+ 1)]

for i in range(1, num + 1):
    for j in range(1, max_bag + 1):
        if weight[i-1] <= j:
            table[i][j] = max(table[i - 1][j - weight[i - 1]] + value[i-1], table[i - 1][j])
        else:
            table[i][j] = table[i - 1][j]
print(table[-1][-1])
