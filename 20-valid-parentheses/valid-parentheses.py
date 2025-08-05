class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """ 
        dic = { ")":"(" , "}":"{" , "]":"[" }
        stack = []
        for ch in s:
            if ch in "{([":
                stack.append(ch)
            else:
                if not stack or stack[-1]!=dic[ch]:
                    return False
                stack.pop()
        return False if stack else True                                                 
