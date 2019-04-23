# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: tree.py
@time: 2019/3/23 16:40
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def FindPath(self, root, expectNumber):
    #     print(root.val)
    #     alist = []
    #     listALL = []
    #     def FindPaht1(root, expectNumber):
    #         print(root.val)
    #         if root==None:
    #             return []
    #         alist.append(root.val)
    #         expectNumber = expectNumber - root.val
    #         isLeaf = (root.left==None and root.right==None)
    #         if expectNumber==0 and isLeaf:
    #             listALL.append(alist)
    #         FindPaht1(root.left, expectNumber)
    #         FindPaht1(root.right, expectNumber)
    #         alist.pop()
    #         return listALL
    #     FindPaht1(root, expectNumber)
    #     return listALL
    # def FindPath(self, root, expectNumber):
    #     # write code here
    #     if not root:
    #         return []
    #     if root and not root.left and not root.right and root.val == expectNumber:
    #         return [[root.val]]
    #     res = []
    #     left = self.FindPath(root.left, expectNumber-root.val)
    #     right = self.FindPath(root.right, expectNumber-root.val)
    #     for i in left+right:
    #         res.append([root.val]+i)
    #     return res
    def __init__(self):
        self.paths = []
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        self.findpath(root, expectNumber, [])
        return self.paths
    def findpath(self, root, expectNumber, path =[]):
        expectNumber-=root.val
        p = path[:]
        p.append(root.val)
        if root.left:
            self.findpath(root.left, expectNumber, p)
        if root.right:
            self.findpath(root.right, expectNumber, p)
        if not root.left and not root.right:
            if expectNumber==0:
                self.paths.append(p)
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution1:
    def __init__(self):
        self.alist = []
    def GetNext(self, pNode):
        # write code here
        if pNode == None:
            return None
        root = self.FindRoot(pNode)
        self.InOrder(root)
        for i in range(len(self.alist)):
            if self.alist[i]==pNode:
                if i!= len(self.alist)-1:
                    return self.alist[i+1]
                else:
                    return None
    def FindRoot(self, pNode):
        if pNode.next==None:
            return pNode
        return self.FindRoot(pNode.next)
    def InOrder(self, root):
        if root:
            self.InOrder(root.left)
            self.alist.append(root)
            # print(root.val)
            self.InOrder(root.right)
    def Print(self, pRoot):
        # write code here
        if pRoot==None:
            return []
        stack = []
        result = []
        stack.append(pRoot)
        index = 1
        while stack!=[]:
            tmp = []
            if index%2==0:
                for i in stack[::-1]:
                    tmp.append(i.val)
            else:
                for i in stack:
                    tmp.append(i.val)
            stackNew = []
            for i in stack:
                # print(i.val, index)
                if i.left:
                    stackNew.append(i.left)
                if i.right:
                    stackNew.append(i.right)
            result.append(tmp)
            if stackNew!=[]:
                index+=1
            stack = stackNew
        return result

    def Serialize(self, root):
        # write code here
        s = ""
        if root==None:
            s = s + "#,"
            return s
        s = s + str(root.val) + ","
        s = s + self.Serialize(root.left)
        s = s + self.Serialize(root.right)
        return s

class Solution2:
    # 返回对应节点TreeNode
    def __init__(self):
        self.index = 0

    def KthNode(self, pRoot, k):
        # write code here
        if pRoot:
            left = self.KthNode(pRoot.left, k)
            if left!=None:
                return left
            self.index += 1
            if k == self.index:
                return pRoot.val
            right = self.KthNode(pRoot.right, k)
            if right!=None:
                return right
        return None

    # def inOrder(self, root):
    #     if root:
    #         self.index+=1
    #         if root.left!=None:
    #             self.stack.append(self.preOrder(root.left))
    #         if k == self.index:
    #             return root.val
    #         if root.right!=None:
    #             self.stack.append(self.preOrder(root.right))

    # def Deserialize(self, s):
if __name__ == '__main__':
    # {8, 6, 10, 5, 7, 9, 11}, 8
    import numpy as np
    print(np.reshape([1,2,3,4], (2,2), order='F'))


    s = Solution1()
    r1 = TreeLinkNode(8)
    r1.left = TreeLinkNode(6)
    r1.right = TreeLinkNode(10)

    r1.left.left = TreeLinkNode(5)
    r1.left.right = TreeLinkNode(7)
    r1.left.next = r1

    r1.left.left.next = r1.left
    r1.left.right.next = r1.left

    r1.right.left = TreeLinkNode(9)
    r1.right.right = TreeLinkNode(11)
    r1.right.next = r1

    r1.right.left.next = r1.right
    r1.right.right.next = r1.right

    # print(s.FindRoot(s, r1).val)
    # print(s.Serialize(r1))
    # print(s.InOrder(s, r1))
    ss = Solution2()
    # print(ss.KthNode(r1, 2))

import sys

# for line in sys.stdin:
#     a,b = line.strip().split('-')
#     a, b = list(a), list(b)
#     result = ""
#     aend = -1
#     for i in range(-1, -(len(b)+1), -1):
#         if int(a[i])>=int(b[i]):
#             result = str(int(a[i])-int(b[i])) + result
#         else:
#             result = str(int(a[i])+10-int(b[i])) + result
#             pos = i-1
#             while pos>-len(a)-1:
#                 if int(a[pos])> 0:
#                     a[pos] = str(int(a[pos])-1)
#                     break
#                 else:
#                     a[pos] = '9'
#                     pos-=1
#             aend = pos
#         aend = i
#     print("".join(a[-len(a):aend])+result)
#     eval()




    # root, left1, right1 = TreeNode, TreeNode, TreeNode
    # root.left = left1
    # root.right = right1
    # root.val = 1
    # left1.val = 2
    # right1.val = 3
    # s = Solution
    # print(s.FindPath(s, root, 3))
    # s = "I am a student."
    # a = s.split(" ")
    #
    # result = ""
    #
    # for i in a[::-1]:
    #     result = result+i+" "
    # print(result[:-1])
    # def IsContinuous(numbers):
    #     # write code here
    #     dict = {'A':1, 'J':11, 'Q':12, 'K':13}
    #     num = []
    #     zeros = []
    #     for i in numbers:
    #         if i in dict:
    #             num.append(dict[i])
    #         elif i==0:
    #             zeros.append(i)
    #         else:
    #             num.append(i)
    #     if len(zeros)>4:
    #         print('false')
    #         return
    #     for i in range(len(num)-1):
    #         if num.count(num[i])>1:
    #             print('false')
    #             return
    #         for j in range(i+1, len(num)):
    #             if abs(num[i]-num[j])>4:
    #                 print('false')
    #                 return
    #     print('true')
    #     return
    #
    # alist = [1, 3, 2, 5, 4]
    # IsContinuous(alist)

    # def LastRemaining_Solution(n, m):
    #     # write code here
    #     if n==0 or m==0:
    #         return 0
    #     kids = list(range(n))
    #     index = 0
    #     while len(kids)>1:
    #         index = index+m-1
    #         while index>=len(kids):
    #             index = index - len(kids)
    #         kids.pop(index)
    #     return kids[0]
    #
    # n = 5
    # m = 3
    # print(LastRemaining_Solution(n, m))
    #
    # def StrToInt(s):
    #     # write code here
    #     if s=="":
    #         return 0
    #     INT_MAX = 2**32-1
    #     INT_min = -2**32
    #     str2num={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
    #     num = []
    #     sign = ""
    #     for i in range(len(s)):
    #         if i==0:
    #             if s[i]=="+" or s[i]=="-":
    #                 sign = s[i]
    #                 break
    #         if s[i] not in '0123456789':
    #             return 0
    #         num.append(str2num[s[i]])
    #     sum = 0
    #     for j in range(len(num)):
    #         sum = sum + num[j]*(10**(len(num)-j-1))
    #     if sign=="+" or len(sign)==0:
    #         return min(2**32-1, sum)
    #     if sign=="-":
    #         return max(-2**32, sum)
    #
    # s = "+123"
    # print(StrToInt(s))

    # def duplicate(numbers, duplication):
    #     # write code here
    #     if len(numbers)==0:
    #         return False
    #     for i in numbers:
    #         if numbers.count(i) > 1:
    #             duplication.append(i)
    #             return True
    #     return False
    #
    # num = [2,1,3,1,4]
    # du = []
    # print(duplicate(num, du))
    # print(du)
    # def match(s, pattern):
    #     # write code here
    #     if len(s)==0 and len(pattern)==0:
    #         return True
    #     s_split = pattern.split("*")
    #     if len(s)!=0 :
    #         i = 0
    #         for i in range(len(s)):
    #             if s[i] in s_split[i] or '.' in s_split[i]:
    #                 continue
    #         if s_split[len(s)]=="":
    #             return True
    #         else:
    #             return False
    #     if len(s)==0 and len(s_split)==2:
    #         if len(s_split[1]) == 0:
    #             return True
    #     if len(s)==len(pattern):
    #         for i in range(len(s)):
    #             if s[i]==pattern[i] or pattern[i]=='.':
    #                 continue
    #         return True
    #     else:
    #         return False
    #
    # s1 = "a"
    # s2 = "a."
    # print(match(s1, s2))

    # def isNumeric(s):
    #     # write code here
    #     if len(s) == 0:
    #         return False
    #     sign = ['-', '+', '.', 'e']
    #     sign_val = [0, 0, 0, 0]
    #     if s[0] in "+-":
    #         for i in range(1, len(s)):
    #             if s[i]=='-' or s[i]=='+':
    #                 return False
    #             elif s[i]=='e' or s[i]=='E':
    #                 sign_val[3]+=1
    #             elif s[i]=='.':
    #                 sign_val[2]+=1
    #             elif s[i] in '1234567890':
    #                 continue
    #             else:
    #                 return False
    #         if sign_val[2]>1 or sign_val[3]>1:
    #             return False
    #         return True
    #     elif s[0] in "12345678":
    #         for i in range(1, len(s)):
    #             if s[i]=='-' or s[i]=='+':
    #                 return False
    #             elif s[i]=='e' or s[i]=='E':
    #                 sign_val[3]+=1
    #             elif s[i]=='.':
    #                 sign_val[2]+=1
    #             elif s[i] in '1234567890':
    #                 continue
    #             else:
    #                 return False
    #         if sign_val[2]>1 or sign_val[3]>1:
    #             return False
    #         return True
    #     elif s[0]=='0':
    #         if s[1]!='.':
    #             return False
    #     else:
    #         return False
    #
    #
    # s = '123.45e+6'
    # print(isNumeric(s))

    # def Insert(char):
    #     dict = {}
    #     for i in range(len(char)):
    #         if char[i] not in dict:
    #             dict[char[i]] = 1
    #         else:
    #             dict[char[i]] += 1
    #     for i in range(len(char)):
    #         if dict[char[i]] == 1:
    #             return char[i]
    #
    # s = 'google'
    # print(Insert(s))