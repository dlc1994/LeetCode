# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = l1
        str1=""
        flag1 = True
        while flag1:
            str1 = str1 + "".join(str(temp.val))
            # print(str1)
            if temp.next != None:
                temp = temp.next
            else:
                flag1 = False
        # print('1', temp)
        # print('str1', str1)
        val1 = int(str1[::-1])
        # print('val1', val1)
        
        temp = l2
        str2=""
        flag2 = True
        while flag2:
            str2 = str2 + "".join(str(temp.val))
            if temp.next!=None:
                temp = temp.next
            else:
                flag2 = False
        # print('2', temp)
        # print(str2)
        val2 = int(str2[::-1])
        val = val1 + val2
        val = str(val)
        
        val = val[::-1]
        print(val)
        first_node = ListNode(int(val[0]))
        # first_node.val = int(val[0])
        num = 1
        temp = first_node
        while num < len(val):
            print(num)
            listnode_temp = ListNode(int(val[num]))
            # listnode_temp.val = int(val[num])
            listnode_temp.next = temp
            temp = listnode_temp
            num = num + 1

        return temp

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        carry = 0
        pre_l1 = None
        head = l1
        while (l1 != None and l2 != None): #两个链表长度相同部分用l1的空间存储值
            tmp_sum = l1.val + l2.val + carry
            carry = int((tmp_sum)/10)
            l1.val = (tmp_sum)%10
            
            pre_l1 = l1
            l1, l2 = l1.next, l2.next
        
        if l2 != None: #l2比l1长的部分
            pre_l1.next = l2
            l1 = pre_l1.next
            
        while l1 != None and carry == 1: #l1比l2长并且有进位
            tmp_sum = l1.val+carry
            l1.val = (tmp_sum)%10
            carry = int((tmp_sum)/10)
            pre_l1, l1 = l1, l1.next

        if carry == 1:
            pre_l1.next = ListNode(1)
            
        return head

def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            l1 = stringToListNode(line)
            line = lines.next()
            l2 = stringToListNode(line)
            
            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()