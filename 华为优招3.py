# 输入为两部分，共两行：
# 第一行是一堆typedef定义，标准C++语句，以分号结束，这里不用考虑struct/union这类，只需要考虑基本类型和指针。
# 第二行是制定某个自定义type
# 输出为该自定义type的最终形态
# 如输入：
# typedef int INT; typedef INT** INTP;
# INTP
# 则输出：int * *
# 注意，如果有指针类型，则指针表达的*和前面的类型中间间隔一个空格，和编译器的输出保持一致；另外，如果第一行输入的语句是编译不过的，或者第二行选择的type在第一行中没有定义，则输出none
# 输入描述:
# typedef的一堆自定义类型，并制定最终需要看的类型名
# 输出描述:
# 该类型名的完整名字，和编译器输出保持一致
# 示例1
# 输入
# 复制
# typedef int INT; typedef INT** INTP;
# INTP
# 输出
# 复制
# int * *
# 备注:
# 如果有指针类型，则指针表达的*和前面的类型中间间隔一个空格
# import sys
# line = sys.stdin.readline().strip()
line = "typedef int INT; typedef IiNT** INTP;"
list = list(map(str, line.split(";")))
# print(list)
sys_type = "int char float double bool void * **"
# for i in range(len(list)):
#     if len(list[i]) != 0:
#         cus_type = list[i].split()
#         # print(cus_type)
#         for j in cus_type:
#             if j in sys_type:

if list[0].split()[1] not in sys_type:
    print("none")

if len(list) > 1 and list[1].split()[1] not in list[0]:
    print("none")


# line = sys.stdin.readline().strip()
# weight = list(map(int, line.split(",")))