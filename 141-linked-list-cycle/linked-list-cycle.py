# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        result = set()
        temp = head
        if not head:
            return False
        else:
            while temp.next != None:
                if temp.next not in result:
                    result.add(temp.next)
                    temp = temp.next
                else:
                    return True
        return False                    