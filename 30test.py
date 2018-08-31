"""编译器版本: Python 2.7.6
请使用标准输出(sys.stdout)；已禁用图形、文件、网络、系统相关的操作，如Process , httplib , os；缩进可以使用tab、4个空格或2个空格，但是只能任选其中一种，不能多种混用；如果使用sys.stdin.readline，因为默认会带换行符，所以要strip(' ')进行截取；建议使用raw_input()
时间限制: 3S (C/C++以外的语言为: 5 S)   内存限制: 128M (C/C++以外的语言为: 640 M)
输入:
输入范例 例如下面表示总共3个节点和：
3    (表示N=3)
2    (M=2)
下面是N*N的矩阵（此处是一个3*3的矩阵）
3 3
0 2 3
2 0 1
3 1 0
输出:
输出是一个N*N的矩阵（此处根据输入得到是一个3*3的矩阵）
4 4 3
4 2 5
3 5 2
输入范例:
3
2
3 3
0 2 3
2 0 1
3 1 0
输出范例:
4 4 3
4 2 5
3 5 2
编程说明 ▲"""

n = raw_input("Enter N:")
m = raw_input("Enter M:")
a, b = raw_input("Enter matrix shape:").split()
matrix_in = []
for i in range(n):
    matrix_in.append(raw_input("Enter matrix, line: ")).split()
result = []
result_line = []
for i in range(1, n+1):
    for j in range(1, n+1):
        result_line.append(min())



