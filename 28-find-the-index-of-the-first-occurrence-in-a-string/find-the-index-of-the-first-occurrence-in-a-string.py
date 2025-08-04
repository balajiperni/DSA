class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        i = j = 0
        l1 = []
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                l1.append(i)
                i = i + 1
                j = j + 1
            else:
                if l1:
                    i = l1[0]+1 
                else:
                    i += 1
                l1 = []
                j = 0

        return l1[0] if j == len(needle) else -1
