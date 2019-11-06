"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


class Solution(object):
            def longestPalindrome(self, s):
                        """
                        :type s: str
                        :rtype: str
                        """
                        # 使用动态规划，用空间换时间，把问题拆分
                        # 获取字符串s的长度
                        str_length = len(s)
                        # 记录最大字符串长度
                        max_length = 0
                        # 记录位置
                        start = 0
                        # 循环遍历字符串的每一个字符
                        for i in range(str_length):
                                    # 如果当前循环次数-当前最大长度大于等于1  并  字符串[当前循环次数-当前最大长度-1:当前循环次数+1]  == 取反后字符串
                                    if i - max_length >= 1 and s[i - max_length - 1: i + 1] == s[i - max_length - 1: i + 1][::-1]:
                                                # 记录当前开始位置
                                                start = i - max_length - 1
                                                # 取字符串最小长度为2，所以+=2，s[i-max_length-1: i+1]
                                                max_length += 2
                                                continue
                                    # 如果当前循环次数-当前最大长度大于等于0  并  字符串[当前循环次数-当前最大长度:当前循环次数+1]  == 取反后字符串
                                    if i - max_length >= 0 and s[i - max_length: i + 1] == s[i - max_length: i + 1][::-1]:
                                                start = i - max_length
                                                # 取字符串最小长度为1，所以+=1，s[i-max_length: i+1]
                                                max_length += 1
                        # 返回最长回文子串
                        return s[start: start + max_length]


# manacher算法
def manacher(self):
            s = '#' + '#'.join(self.string) + '#'  # 字符串处理，用特殊字符隔离字符串，方便处理偶数子串
            lens = len(s)
            f = []  # 辅助列表：f[i]表示i作中心的最长回文子串的长度
            maxj = 0  # 记录对i右边影响最大的字符位置j
            maxl = 0  # 记录j影响范围的右边界
            maxd = 0  # 记录最长的回文子串长度
            for i in range(lens):  # 遍历字符串
                        if maxl > i:
                                    count = min(maxl - i, int(f[2 * maxj - i] / 2) + 1)  # 这里为了方便后续计算使用count，其表示当前字符到其影响范围的右边界的距离
                        else:
                                    count = 1
                        while i - count >= 0 and i + count < lens and s[i - count] == s[i + count]:  # 两边扩展
                                    count += 1
                        if (i - 1 + count) > maxl:  # 更新影响范围最大的字符j及其右边界
                                    maxl, maxj = i - 1 + count, i
                        f.append(count * 2 - 1)
                        maxd = max(maxd, f[i])  # 更新回文子串最长长度
            return int((maxd + 1) / 2) - 1  # 去除特殊字符


class Solution2(object):
            def longestPalindrome(self, s):
                        """
                        :type s: str
                        :rtype: str
                        """
                        size = len(s)
                        mx = 0
                        begin = 0

                        for i in range(size):
                                    if i - mx >= 1 and s[i - mx - 1:i + 1][::-1] == s[i - mx - 1:i + 1]:
                                                begin = i - mx - 1
                                                mx += 2
                                                continue
                                    if i - mx >= 0 and s[i - mx:i + 1][::-1] == s[i - mx:i + 1]:
                                                begin = i - mx
                                                mx += 1
                        return s[begin:begin + mx]


if __name__ == '__main__':
            s = "babad"
            # s = "cbbd"
            sl = Solution()
            print(sl.longestPalindrome(s))
            s2 = Solution2()
            print(s2.longestPalindrome(s))
