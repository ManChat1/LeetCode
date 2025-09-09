class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
This exercise is meant to simulate how multidigit numbers can be added
with Linked Lists.
'''

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode(0)
        res.next = 0
        cur = res # the point of this is to set a pointer for each digit to keep track of
        carry = 0
        while l1 or l2 or carry:     
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next

            total = v1 + v2 + carry
            carry = 1 if total // 10 else 0 # utilize integer division to determine if the number exceeds 9.
            total = total % 10 if carry else total # only do it carry is available - not needed, but better for performance marginally

            '''
            carry, total = divmod(
                (l1.val if l1 else 0) +
                (l2.val if l2 else 0) + (carry),
                10
            )
            The divmod function can also be used, however it proves to be significantly slower.
            divmod(dividend, divisor)
            '''

            cur.next = ListNode(total) # Add this digit to the result
            cur = cur.next # Move to the next digit to add
        return res.next