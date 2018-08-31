def getNext(p):
    j = 0
    k = -1  # next[j]的值（也就是k）表示，当P[j] != T[i]时，j指针的下一步移动位置。
    next_p = [-1] * len(p)
    while j < len(p) - 1:
        print("p[k]: " + p[k] + ", p[j]: " + p[j])
        if k == -1 or p[k] == p[j]:
            j += 1
            k += 1
            if p[j] == p[k]:  # 当两个字符相等时要跳过
                next_p[j] = next_p[k]
            else:
                next_p[j] = k
        else:
            k = next_p[k]
    print(next_p)
    return next_p


def KMP(s, p):
    i = 0  # 主串位置
    j = 0  # 模式串位置
    next_p =getNext(p)
    while i < len(s) and j < len(p):
        if j == -1 or s[i] == p[j]:  # 当j为-1时，要移动的是i，当然j也要归0
            i += 1
            j += 1
        else:
            j = next_p[j]
    if j == len(p):
        return i - j
    else:
        return -1

if __name__ == "__main__":
    s = "abcabcabcabcabxabc"
    p = "abcabx"
    p = "abbcabcaabbcaa"
    print(KMP(s, p))