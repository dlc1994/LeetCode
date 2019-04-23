# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: leetcode13 roman2integer.py
@time: 2018/12/19 10:19
'''
ss = "III"

class Solution:
    # def romanToInt(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     #实际一个dict就ok
    #     romandict = {'I': 0, 'V': 1, 'X': 2, 'L': 3, 'C': 4, 'D': 5, 'M': 6}
    #     numdict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #     savelist = []
    #     sum = 0
    #
    #     while s != "":
    #         if len(s) >= 2:
    #             if romandict[s[0]] >= romandict[s[1]]:
    #                 savelist.append(s[0])
    #                 s = s[1:]
    #             else:
    #                 savelist.append(s[0:2])
    #                 s = s[2:]
    #         else:
    #             savelist.append(s[0])
    #             s = ""
    #     for roman_c in savelist:
    #         if len(roman_c) == 1:
    #             sum = sum + int(numdict[roman_c])
    #         else:
    #             sum = sum + (int(numdict[roman_c[1]]) - int(numdict[roman_c[0]]))
    #     return sum



    def romanToInt(self, s):
        d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        res, p = 0, 'I'
        for c in s[::-1]:
            res, p = res - d[c] if d[c] < d[p] else res + d[c], c
        return res

s = Solution()
print(s.romanToInt(ss))