# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: LIS.py
@time: 2019/4/12 16:45
'''
a = list(map(int, input().split()))
dp = [1]*len(a)

for i in range(1, len(a)):
    dp[i] = 1
    for j in range(i):
        if a[i]>a[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(dp)