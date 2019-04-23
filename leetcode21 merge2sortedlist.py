# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# easy
class Solution:
    # recursive
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        while l1!=None and l2!=None:
            if l1.val<=l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2

    # loop
    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        root = head = ListNode(0)
        while l1!=None and l2!=None:
            if l1.val<=l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if not l1: head.next = l2
        if not l2: head.next = l1
        return root.next