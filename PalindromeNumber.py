# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: PalindromeNumber.py
@time: 2018/10/30 11:32
'''
A = -121

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return (str(x) == str(x)[::-1])

s = Solution
print(s.isPalindrome(s, A))