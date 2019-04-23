# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: leetcode22 generateParentheses.py
@time: 2019/4/23 11:39
'''
# medium backtrack

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(S="", left=0, right=0):
            if len(S) == 2 * n:
                result.append(S)
                return

            if left > 0:  backtrack(S + '(', left - 1, right + 1)
            if right > 0: backtrack(S + ')', left, right - 1)

        backtrack("", n, 0)
        return result