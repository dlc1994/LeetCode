# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: selfdividing.py
@time: 2018/8/4 17:12
'''
left = 1
right = 22
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ll = []
        for i in range(left, right+1):
            if '0' not in str(i):
                digits = []
                for digit in str(i):
                    digits.append(i % int(digit))
                if '0' not in digits:
                    ll.append(i)
        return ll

s = Solution
print(s.selfDividingNumbers(s, left, right))