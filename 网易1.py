# 为了找到自己满意的工作，牛牛收集了每种工作的难度和报酬。牛牛选工作的标准是在难度不超过自身能力值的情况下，牛牛选择报酬最高的工作。在牛牛选定了
# 自己的工作后，牛牛的小伙伴们来找牛牛帮忙选工作，牛牛依然使用自己的标准来帮助小伙伴们。牛牛的小伙伴太多了，于是他只好把这个任务交给了你。
# 输入描述:
# 每个输入包含一个测试用例。
# 每个测试用例的第一行包含两个正整数，分别表示工作的数量N(N<=100000)和小伙伴的数量M(M<=100000)。
# 接下来的N行每行包含两个正整数，分别表示该项工作的难度Di(Di<=1000000000)和报酬Pi(Pi<=1000000000)。
# 接下来的一行包含M个正整数，分别表示M个小伙伴的能力值Ai(Ai<=1000000000)。
# 保证不存在两项工作的报酬相同。
#
#
# 输出描述:
# 对于每个小伙伴，在单独的一行输出一个正整数表示他能得到的最高报酬。一个工作可以被多个人选择。
#
# 输入例子1:
# 3 3
# 1 100
# 10 1000
# 1000000000 1001
# 9 10 1000000000
#
# 输出例子1:
# 100
# 1000
# 1001
import sys
line = sys.stdin.readline().strip()
# 把每一行的数字分隔后转化成int列表
values = list(map(int, line.split()))
N = values[0]
M = values[1]
dic = {}
for i in range(N):
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    if values[0] not in dic:
        dic[values[0]] = values[1]
    else:
        dic[values[0]] = max(values[1], dic[values[0]])
capability = sorted(list(dic.keys()))
line = sys.stdin.readline().strip()
people = list(map(int, line.split()))

money = []
can_job = []
for i in range(len(people)):
    for c in range(len(capability)):
        if people[i] >= capability[c]:
            can_job.append(dic[capability[c]])
        else:
            continue
    if len(can_job) == 0:
        print(0)
    else:
        print(max(can_job))






#
# def search(people, capab):
#     s = 0
#     e = len(capab) - 1
#     while s <= e:
#         mid = len(capab) // 2
#     if people == capab[mid]:
#         return capab[mid]
#     elif people < capab[mid]:
#         e = mid - 1
#     else:
#
