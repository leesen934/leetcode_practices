# 请编写一个函数，其功能是将输入的字符串反转过来。
#
# 示例：
#
# 输入：s = "hello"
# 返回："olleh"
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1 ========================================================
        return s[::-1]
        # 2 ========================================================
        # 实际上我们可以for循环”一半”数据长度。将首位字符交换即可。

        # 此时时间复杂度为o(n/2).
        #
        # public static String reverseString4(String s) {
        #         char[] ch = s.toCharArray();
        #         int halfLength = s.length() / 2;
        #         char temp;
        #         for (int i = 0; i < halfLength; i++) {
        #             temp = ch[s.length() - 1 - i];
        #             ch[s.length() - 1 - i] = ch[i];
        #             ch[i] = temp;
        #         }
        #         return new String(ch);
        #     }

        # ========================================================
        # 通过递归的方式来做。
        #
        # public static String reverseString7(String s) {
        #         int length = s.length();
        #         if (length <= 1) {
        #             return s;
        #         }
        #         String leftStr = s.substring(0, length / 2);
        #         String rightStr = s.substring(length / 2, length);
        #         return reverseString7(rightStr) + reverseString7(leftStr);
        #     }