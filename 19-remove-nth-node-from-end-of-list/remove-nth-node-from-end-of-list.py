class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        prev = dummy
        for _ in range(n + 1):
            temp = temp.next
        while temp:
            temp = temp.next
            prev = prev.next
        prev.next = prev.next.next
        return dummy.next
