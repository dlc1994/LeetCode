# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: JewerAndStones.py
@time: 2018/7/30 11:43
'''
J = "aA"
S = "aAAbbbb"
#return 3

class Solution:
    def JewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # dict={}
        # for j in range(len(J)):
        #     if J[j] not in dict:
        #         dict[J[j]]=0
        # for s in range(len(S)):
        #     if S[s] in dict:
        #         dict[S[s]]+=1
        # print(sum(dict.values()))
        # cnt=0
        # for j in J:
        #     cnt+=S.count(j)
        return sum([S.count(j) for j in J])
            # print(S.count(j))
s = Solution
print(s.JewelsInStones(s, J, S))