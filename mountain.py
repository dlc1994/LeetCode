# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: mountain.py
@time: 2018/8/4 16:49
'''

A = [1,2,0]

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # return (A.index(max(A)))

        i = 0
        while (A[i] < A[i + 1]):
            max_ind = i + 1
            i += 1

        return (max_ind)

s = Solution
print(s.peakIndexInMountainArray(s, A))