class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        tempA, tempB = headA, headB

        while tempA != tempB:
            tempA = tempA.next if tempA else headB
            tempB = tempB.next if tempB else headA

        return tempA 
