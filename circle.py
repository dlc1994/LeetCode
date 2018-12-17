# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: circle.py
@time: 2018/7/31 17:27
'''
moves = "UD"


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # origin_x = 0
        # origin_y = 0
        # for move in moves:
        #     if move == 'U':
        #         origin_y += 1
        #     elif move == 'D':
        #         origin_y -= 1
        #     elif move == 'L':
        #         origin_x -= 1
        #     elif move == 'R':
        #         origin_x += 1
        # return ([origin_x, origin_y] == [0, 0])

        # return ((moves.count('U') == moves.count('D')) & (moves.count('L') == moves.count('R')))

        # return not sum(map(1j.__pow__, map('RUL'.find, moves)))

        return not sum(1j ** 'RUL'.find(m) for m in moves)

s = Solution
print(s.judgeCircle(s, moves))