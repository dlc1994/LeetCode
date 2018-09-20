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


> Description of Problem:
> You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
>
> The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".
> Example 1:
>```
 Input: J = "aA", S = "aAAbbbb"
 Output: 3
>```
> Example 2:
> ```
Input: J = "z", S = "ZZ"
Output: 0
> ```
> Note:
>
> - S and J will consist of letters and have length at most 50.
> - The characters in J are distinct.

**Approach 1: Python Dict**
```python
class Solution:
    def JewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dict={}
        for j in range(len(J)):
            if J[j] not in dict:
                dict[J[j]]=0
        for s in range(len(S)):
            if S[s] in dict:
                dict[S[s]]+=1
        return sum(dict.values())
```
Running time is a bit long, therefore I improve it.
**Approach 2: **
```python
class Solution:
    def JewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        cnt = 0
        for j in J:
            cnt+=S.count(j)
        return cnt
```
More simplicity, one line is OK.
```python
class Solution:
    def JewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
		return sum([S.count(j) for j in J])
```
Running time: 40ms
