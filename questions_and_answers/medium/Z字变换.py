"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""




class Solution:
            @classmethod
            def convert(cls, s, num_rows):
                        if num_rows == 1:
                                    return s
                        L = [''] * num_rows
                        index, step = 0, 1
                        for x in s:
                                    # print('index: {}, step: {}, L:{}'.format(index, step, L))

                                    L[index] += x
                                    if index == 0:
                                                step = 1
                                    elif index == num_rows - 1:
                                                step = -1
                                    index += step

                                    # print('AFTER = index: {}, step: {}, L:{}'.format(index, step, L))
                        return ''.join(L)


if __name__ == '__main__':
            s = "LEETCODEISHIRING"
            numRows = 3

            answer = Solution.convert(s, numRows)


            """
            index: 0, step: 1, L:['', '', '']
            AFTER = index: 1, step: 1, L:['L', '', '']
            
            index: 1, step: 1, L:['L', '', '']
            AFTER = index: 2, step: 1, L:['L', 'E', '']
            
            index: 2, step: 1, L:['L', 'E', '']
            AFTER = index: 1, step: -1, L:['L', 'E', 'E']
            
            index: 1, step: -1, L:['L', 'E', 'E']
            AFTER = index: 0, step: -1, L:['L', 'ET', 'E']
            
            index: 0, step: -1, L:['L', 'ET', 'E']
            AFTER = index: 1, step: 1, L:['LC', 'ET', 'E']
            
            index: 1, step: 1, L:['LC', 'ET', 'E']
            AFTER = index: 2, step: 1, L:['LC', 'ETO', 'E']
            
            index: 2, step: 1, L:['LC', 'ETO', 'E']
            AFTER = index: 1, step: -1, L:['LC', 'ETO', 'ED']
            
            index: 1, step: -1, L:['LC', 'ETO', 'ED']
            AFTER = index: 0, step: -1, L:['LC', 'ETOE', 'ED']
            
            index: 0, step: -1, L:['LC', 'ETOE', 'ED']
            AFTER = index: 1, step: 1, L:['LCI', 'ETOE', 'ED']
            
            index: 1, step: 1, L:['LCI', 'ETOE', 'ED']
            AFTER = index: 2, step: 1, L:['LCI', 'ETOES', 'ED']
            
            index: 2, step: 1, L:['LCI', 'ETOES', 'ED']
            AFTER = index: 1, step: -1, L:['LCI', 'ETOES', 'EDH']
            
            index: 1, step: -1, L:['LCI', 'ETOES', 'EDH']
            AFTER = index: 0, step: -1, L:['LCI', 'ETOESI', 'EDH']
            
            index: 0, step: -1, L:['LCI', 'ETOESI', 'EDH']
            AFTER = index: 1, step: 1, L:['LCIR', 'ETOESI', 'EDH']
            
            index: 1, step: 1, L:['LCIR', 'ETOESI', 'EDH']
            AFTER = index: 2, step: 1, L:['LCIR', 'ETOESII', 'EDH']
            
            index: 2, step: 1, L:['LCIR', 'ETOESII', 'EDH']
            AFTER = index: 1, step: -1, L:['LCIR', 'ETOESII', 'EDHN']
            
            index: 1, step: -1, L:['LCIR', 'ETOESII', 'EDHN']
            AFTER = index: 0, step: -1, L:['LCIR', 'ETOESIIG', 'EDHN']
            
            
            answer:
            TYPE : <class 'str'>     LEN : 16 
            VALUE : 'LCIRETOESIIGEDHN'

            """
