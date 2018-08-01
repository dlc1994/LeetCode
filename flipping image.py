# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: flipping image.py
@time: 2018/7/31 16:48
'''
A = [[1,1,0],[1,0,1],[0,0,0]]

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # B = []
        # for i in A:
        #     temp = [1 if ii==0 else 0 for ii in i[::-1]]
        #     B.append(temp)
        # return B
        return [[1 if ii==0 else 0 for ii in i[::-1]] for i in A]

s = Solution
print(s.flipAndInvertImage(s, A))