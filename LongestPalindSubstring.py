# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: reverse.py
@time: 2018/11/29 16:12
'''
A = "cbbd"

class Solution(object):
    def reverse(self, s):
        """
        :type x: string
        :rtype: int
        """
        s_new = ""
        for i in range(2*len(s)+1):
            if i%2 == 0:
                s_new = s_new + s_new.join('#')
            else:
                s_new = s_new + s_new.join(s[int((i-1)/2)])
        print(s_new)
        max_ = 0
        left_pos = 0

        for num, s_c in enumerate(s_new):
            l = num - 1
            r = num + 1
            while l>=0 and r<len(s_new):
                if (s_new[l] == s_new[r]):
                    max_1 = max(max_, (r - l + 1))
                    if max_1 > max_:
                        max_ = max_1
                        left_pos = l
                    l -= 1
                    r += 1
                else:
                    break
        print(max_)
        return s_new[left_pos:left_pos + max_].replace('#',"")

        # def longestPalindrome(self, s):
        #     res = ""
        #     for i in xrange(len(s)):
        #         # odd case, like "aba"
        #         tmp = self.helper(s, i, i)
        #         if len(tmp) > len(res):
        #             res = tmp
        #         # even case, like "abba"
        #         tmp = self.helper(s, i, i + 1)
        #         if len(tmp) > len(res):
        #             res = tmp
        #     return res
        #
        # # get the longest palindrome, l, r are the middle indexes
        # # from inner to outer
        # def helper(self, s, l, r):
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         l -= 1;
        #         r += 1
        #     return s[l + 1:r]

s = Solution
print(s.reverse(s, A))