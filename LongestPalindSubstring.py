# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: reverse.py
@time: 2018/11/29 16:12
'''
A = 'aabcbcbaacbaasd'

class Solution(object):
    def reverse(self, s):
        """
        :type x: string
        :rtype: int
        """
        max_ = 0

        for num, s_c in enumerate(s):
            l = num - 1
            r = num + 1
            while l>=0 and r<len(s):
                if (s[l] == s[r]):
                    max_ = max(max_, (r - l + 1))
                    l -= 1
                    r += 1
                else:
                    break
        return max_



s = Solution
print(s.reverse(s, A))