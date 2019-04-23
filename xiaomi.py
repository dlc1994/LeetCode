# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: xiaomi.py
@time: 2019/3/28 10:35
'''
import sys
# for line in sys.stdin:
#     line = list(map(int, line.strip().split(',')))
#     nums = set(line)
#     best = 0
#     for x in nums:
#         if x - 1 not in nums:
#             y = x + 1
#             while y in nums:
#                 y += 1
#             best = max(best, y - x)
#     print(best)

# for line in sys.stdin:
#     line = list(map(int, line.strip().split(',')))
#     line.sort()
#     print(line[len(line)//2])

# for line in sys.stdin:
#     s1, s2, s3 = line.strip().split(',')
#     i,j,k=0,0,0
#     if len(s3)!=len(s1)+len(s2):
#         print('false')
#         break
#     while k<len(s3) and i<len(s1) and j<len(s2):
#         if s3[k]==s1[i]:
#             k+=1
#             i+=1
#         elif s3[k]==s2[j]:
#             k+=1
#             j+=1
#         else:
#             print('false')
#             break
#     if i<len(s1):
#         if s1[i:]==s3[k:]:
#             print('true')
#         else:
#             print('false')
#     if j<len(s2):
#         if s2[j:]==s3[k:]:
#             print('true')
#         else:
#             print('false')

# def Is(s1, s2, s3):
#     if len(s3)!=len(s1)+len(s2):
#         return False
#     if len(s1)==0:
#         if s2==s3:
#             return True
#     if len(s2)==0:
#         if s1==s3:
#             return True
#     dp = [[0]*(len(s2)+1) for i in range(len(s1)+1)]
#     dp[0][0] = 1
#     for i in range(1, len(s1)+1):
#         if s1[i-1] == s3[i-1]:
#             dp[i][0] = 1
#     for j in range(1, len(s2)+1):
#         if s2[j-1] == s3[j-1]:
#             dp[0][j] = 1
#     for i in range(1, len(s1)+1):
#         for j in range(1, len(s2)+1):
#             k = i+j
#             if s1[i-1]==s3[k-1]:
#                 dp[i][j] = dp[i-1][j] or dp[i][j]
#             if s2[j-1] == s3[k-1]:
#                 dp[i][j] = dp[i][j-1] or dp[i][j]
#     if dp[len(s1)][len(s2)]==1:
#         return True
#     return False
#
#
# for line in sys.stdin:
#     s1, s2, s3 = line.strip().split(',')
#     if Is(s1,s2,s3):
#         print('true')
#     else:
#         print('false')

# for line in sys.stdin:
#     line = list(map(int, line.strip().split(',')))
#     nums = set(line)
#     maxV = max(nums)
#     for x in range(1, max(maxV+2, 2)):
#         if x not in nums:
#             print(x)
#             break

# def Fac(n):
#     print(n)
#     if n==0:
#         return 0
#     if n==1:
#         return 2
#     if n==2:
#         return 2
#     return Fac(n-1)+Fac(n-2)


# for line in sys.stdin:
#     s1, s2 = line.strip().split()
#     s2 = list(s2)
#     flag = True
#     for s in s1:
#         if s not in s2:
#             print('false')
#             flag = False
#             break
#         s2.remove(s)
#     if flag:
#         print('true')

# for line in sys.stdin:
#     nums, target = line.strip().split()
#     nums = list(map(int, nums.split(',')))
#     target = int(target)
#     print(nums, target)
#     if target in nums:
#         print(nums.index(target))
#     else:
#         print(-1)

# for line in sys.stdin:
#     line = int(line.strip())
#     num = str(bin(line))[2:][::-1]
#     while len(num)<32:
#         num = num+ "0"
#     print(num)
#     print(int(num,2))
import sys

for line in sys.stdin:
    a, b, c, d, e = list(map(int, line.strip().split()))
    print(a,b,c,d,e)
    nums = 0
    for x1 in range(-50, 51):
        if x1!=0:
            for x2 in range(-50, 51):
                if x2!=0:
                    for x3 in range(-50, 51):
                        if x3 != 0 :
                            for x4 in range(-50, 51):
                                if x4 != 0 :
                                    for x5 in range(-50, 51):
                                        if x5!=0:
                                            if a*(x1**3) + b*(x2**3) + c*(x3**3) == d*(x4**3) + e*(x5**3):
                                                nums+=1
                                                print(nums)
    print(nums)



