class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ch = ""
        string = ":;,._=+*/-@#$%&!{]}['"" "
        for char in s:
            if char.lower() not in string and char.isalnum():
                ch = ch + char.lower()
        return ch == ch[::-1]        


        