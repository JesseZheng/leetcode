# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# solution1
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        p = result
        carry = 0
        p1, p2 = l1, l2
        while p1 or p2:
            x = 0 if p1 == None else p1.val
            y = 0 if p2 == None else p2.val
            sum = x + y + carry
            carry = sum // 10
            p.next = ListNode(sum % 10)
            p = p.next
            p1 = p1.next if p1 != None else None
            p2 = p2.next if p2 != None else None
        if carry > 0:
            p.next = ListNode(carry)
        return result.next

# solution2
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        p = result
        carry = 0
        p1, p2 = l1, l2
        while p1 or p2:
            if p1 and p2:
                x = p1.val
                y = p2.val
                sum = (x + y + carry)
                carry = sum // 10
                p.next = ListNode(sum%10)
                p = p.next
                p1 = p1.next
                p2 = p2.next
            elif not p1:
                y = p2.val
                sum = y + carry
                carry = sum // 10
                p.next = ListNode(sum%10)
                p = p.next
                p2 = p2.next
            elif not p2:
                x = p1.val
                sum = x + carry
                carry = sum // 10
                p.next = ListNode(sum%10)
                p = p.next
                p1 = p1.next
        if carry > 0:
            p.next = ListNode(carry)
        return result.next