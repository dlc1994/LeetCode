# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: lookqi.py
@time: 2019/3/10 10:40
'''
stack =[]
n = int(input())
a =[0]
ans =[0]
for i in range(n):
    a.append(int(input()))
for i in range(n, 0, -1):
    print(i)
    while len(stack) and a[stack[-1]]<=a[i]:
        stack.pop()
    if stack==[]:
        ans[i] = 0
    else:
        ans[i] = stack[-1]
    stack.append(i)
print(len(a), len(ans))
for i in range(1, n+1):
    print(ans[i])