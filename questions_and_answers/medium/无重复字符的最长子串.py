"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


@Adrian的回答:
本质上,首先通过字典记录所有出现过的不同字符, 其次, 对每个出现的字符, 这个字典记录的东西是字符串中, 这个字符出现,一直到
它再一次在字符串上遇到自己前走过的字符数,这即是不同字符的字串长度

"""



class Solution:
            @classmethod
            def lengthOfLongestSubstring(cls, s: str) -> int:
                        st = {}
                        i, ans = 0, 0
                        for j in range(len(s)):
                                    if s[j] in st:
                                                i = max(st[s[j]], i)

                                    ans = max(ans, j - i + 1)  # 只找最大的子串

                                    st[s[j]] = j + 1

                        return ans


if __name__ == '__main__':
            inputs = "pwwkew"
            output = Solution.lengthOfLongestSubstring(inputs)
            print(output)
