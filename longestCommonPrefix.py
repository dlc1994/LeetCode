# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: longestCommonPrefix.py
@time: 2018/12/19 11:25
'''
s = ["agower","elow","blights"]

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        mins=min((strs))#按字母排列
        maxs=max((strs))
        pre=""
        for i in range(min(len(mins),len(maxs))):
            if(mins[i]==maxs[i]):
                pre=pre+mins[i]
            else:
                break
        return pre
        ## my solution
        # if strs == []:
        #     return ""
        # pre = ""
        # flag = True
        # count = 0
        # strs_len = [len(str) for str in strs]
        # for num in range(min(strs_len)):
        #     temp = strs[0][num]
        #     for str in strs[1:]:
        #         if str[num] == temp:
        #             continue
        #         else:
        #             return pre
        #     pre = pre + temp
        # return pre



ss = Solution()
print(ss.longestCommonPrefix(s))