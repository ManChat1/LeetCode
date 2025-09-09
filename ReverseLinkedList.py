# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = None
        while head:
            next = head.next # Save everything past the tail
            head.next = res # The next value should be the previous value (iniitally None, then the following values.)
            res = head # The value is set to the current value of the head
            head = next # Restore the head with next
        return res
