# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: validParenthese.py
@time: 2018/12/19 21:26
'''
pp = "()[]{}"

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p_list = []

        for p in s:
            if p in "({[":
                p_list.append(p)
            else:
                if p_list != []:
                    left = p_list.pop()
                    if (left + p) not in ['()', '{}', '[]']:
                        return False
                else:
                    return False
        return p_list == []

s = Solution()
print(s.isValid(pp))