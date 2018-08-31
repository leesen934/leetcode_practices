# -*- coding: utf-8 -*-
#
# 在柠檬水摊上，每一杯柠檬水的售价为5美元。顾客排队购买你的产品，（按账单bills支付的顺序）一次购买一杯。每位顾客只买一杯柠檬水，然后向你付5
# 美元、10美元或20美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付5美元。注意，一开始你手头没有任何零钱。如果你能给每位顾客正
# 确找零，返回true ，否则返回false 。
#
# 示例
# 1：
# 输入：[5, 5, 5, 10, 20]
# 输出：true

#
# 2：
# 输入：[5, 5, 10]
# 输出：true
#
# 3：
# 输入：[10, 10]
# 输出：false
#
# 4：
# 输入：[5, 5, 10, 10, 20]
# 输出：false
#
# 提示：
# 0 <= bills.length <= 10000
# bills[i]不是5就是10或是20
class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = ten = 0
        for num in bills:
            if num == 5:
                five += 1
            elif num == 10 and five:
                ten += 1
                five -= 1
            elif num == 20 and ten and five:
                ten -= 1
                five -= 1
            elif num == 20 and five >= 3:
                five -= 3
            else:
                return False
        return True

        # answer two -----------------------------

        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True

s = Solution()
test = [5, 5, 5, 10, 20]
test2 = [5, 5, 10, 10, 20]
print(s.lemonadeChange(test2))