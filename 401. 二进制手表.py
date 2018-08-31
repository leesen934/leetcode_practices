# 二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。
#
# 每个 LED 代表一个 0 或 1，最低位在右侧。
# 例如，上面的二进制手表读取 “3: 25”。
#
# 给定一个非负整数
# n
# 代表当前
# LED
# 亮着的数量，返回所有可能的时间。
#
# 案例:
#
# 输入: n = 1
# 返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
#
# 注意事项:
#
# 输出的顺序没有要求。
# 小时不会以零开头，比如 “01: 00” 是不允许的，应为 “1: 00”。
# 分钟必须由两位数组成，可能会以零开头，比如 “10: 2” 是无效的，应为 “10: 02”。
class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        res = []
        for hour in range(12):
            for minute in range(60):
                if (bin(hour)+bin(minute)).count('1') == num:  # 统计hour与minute的二进制1有多少，即表示亮灯有多少
                    res.extend(["%d:%02d" % (hour, minute)])  # 二进制+ 是直接拼接
        return res
        # 一、看不懂 -----------------------------------------------------
        res = []
        stack = [(num, 0, 0, 0)]
        while (stack):
            tup = stack.pop()
            n, hour, minute, idx = tup[0], tup[1], tup[2], tup[3]
            if (hour >= 12 or minute > 59):
                continue
            if (n == 0):
                s = str(hour) + ':' + '0' * (minute < 10) + str(minute)
                res.append(s)
                continue
            for i in range(idx, 10):
                if (i < 4):
                    stack.append((n - 1, hour | (1 << (i)), minute, i + 1))
                else:
                    stack.append((n - 1, hour, minute | (1 << (i - 4)), i + 1))

        return res
        # 二、 看不懂----------------------------------------------
        def findHour(k, idx):
            if k == 0: return ['0']
            ret = []
            hour = [8, 4, 2, 1]
            for i in range(idx, 4):
                tmp = findHour(k - 1, i + 1)
                for item in tmp:
                    val = int(item)
                    if val + hour[i] <= 11: ret.append(str(val + hour[i]))
            return ret

        def findMinute(k, idx):
            if k == 0: return ['00']
            ret = []
            minute = [32, 16, 8, 4, 2, 1]
            for i in range(idx, 6):
                tmp = findMinute(k - 1, i + 1)
                for item in tmp:
                    val = int(item)
                    if val + minute[i] <= 59:
                        if val + minute[i] >= 10:
                            ret.append(str(val + minute[i]))
                        else:
                            ret.append('0' + str(val + minute[i]))
            return ret

        ret = []
        for i in range(num + 1):
            if i >= 4: break
            hour = findHour(i, 0)
            minute = findMinute(num - i, 0)
            for item1 in hour:
                for item2 in minute:
                    ret.append(item1 + ':' + item2)
        return ret
s = Solution()
print(s.readBinaryWatch(1))
