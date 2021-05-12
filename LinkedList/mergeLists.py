class Solution:
    def mergeTwoLists(self, l1, l2):
        l1curr = l1
        l2curr = l2

        if l1curr and l2curr and l2.val >= l1.val:
            lHead = l1
            lTot = l1curr
            l1curr = l1curr.next
        elif l1curr and l2curr and l1.val > l2.val:
            lHead = l2
            lTot = l2curr
            l2curr = l2curr.next
        elif l1curr and not l2curr:
            return l1
        else:
            return l2

        while l1curr or l2curr:
            if l1curr and not l2curr:
                lTot.next = l1curr
                lTot = lTot.next
                l1curr = l1curr.next
            elif l2curr and not l1curr:
                lTot.next = l2curr
                lTot = lTot.next
                l2curr = l2curr.next
            elif l1curr.val > l2curr.val:
                lTot.next = l2curr
                lTot = lTot.next
                l2curr = l2curr.next
            else:
                lTot.next = l1curr
                lTot = lTot.next
                l1curr = l1curr.next

        return lHead

