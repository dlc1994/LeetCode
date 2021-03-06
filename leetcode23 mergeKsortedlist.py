# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: leetcode23 mergeKsortedlist.py
@time: 2019/4/23 11:03
'''
# hard
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        while l1 and l2:
            if l1.val <= l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2

    # 两两合并，超时 O(nk)
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists == [] or lists[0] == []:
            return None
        if len(lists) == 1:
            return lists[0]

        def helper(a):
            l = self.mergeTwoLists(a[0], a[1])
            return helper([l] + a[2:])

        root = helper(lists)
        return root
    # 类似归并排序，复杂度O(nlogk)
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        amount = len(lists)
        gap = 1
        while gap < amount:
            for i in range(0, amount-gap, gap*2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i+gap])
            gap *= 2
        return lists[0] if amount>0 else lists