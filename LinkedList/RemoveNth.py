# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        current = head
        nBack = head
        nBackPrev = None

        if n == 0 or current == None:
            return head

        while current.next:
            current = current.next

            if n > 1:
                n = n - 1
            else:   # n ==1
                nBackPrev = nBack
                nBack = nBack.next

        if n > 1:
            return None
        else:       # removal of nBack node
            if nBackPrev == None and nBack.next:
                tmpHead = nBack.next
                nBack.next = None
                return tmpHead
            elif nBackPrev == None:
                return None
            else:
                nBackPrev.next = nBack.next
                nBack.next = None
                return head