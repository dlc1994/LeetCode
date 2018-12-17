# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: reverse.py
@time: 2018/11/29 16:12
'''
A = 123

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # if (x >= 0) & ((x % 10) != 0):
        #     temp = str(x)
        #     temp = temp[::-1]
        #     return int(temp)
        # else:
        #     while (x%10)==0:
        #         x = x/10
        #     x = int(x)
        #     if x<0:
        #         x = str(abs(x))
        #         x = x[::-1]
        #         return int('-' + x)
        #     else:
        #         temp = str(x)
        #         temp = temp[::-1]
        #         return int(temp)
        if (x <= (pow(2, 31)-1)) & (x >= (-pow(2, 31))):
            if x >= 0:
                return int(str(x)[::-1])
            else:
                return int('-' + str(abs(x))[::-1])
        else:
            return 0


s = Solution
print(s.reverse(s, A))