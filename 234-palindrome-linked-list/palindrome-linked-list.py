class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        stack = []
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next
        temp = head
        while temp:
            if temp.val != stack.pop():
                return False
            temp = temp.next

        return True
