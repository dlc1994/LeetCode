# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: hamming.py
@time: 2018/7/31 16:20
'''

x = 1
y = 4
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # count=0
        # x_b = '{:031b}'.format(x)
        # y_b = '{:031b}'.format(y)
        # for i in range(len(x_b)):
        #     if x_b[i] != y_b[i]:
        #         count+=1
        # return count

        return  bin((x^y)).count('1')

s = Solution
print(s.hammingDistance(s, x, y))