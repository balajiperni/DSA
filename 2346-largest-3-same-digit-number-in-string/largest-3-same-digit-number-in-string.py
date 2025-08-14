class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        max_good = ""
        
        for i in range(len(num) - 2):
            sub = num[i:i+3]
            if sub[0] == sub[1] == sub[2]:  # all same digit
                if max_good == "" or sub > max_good:
                    max_good = sub
                    
        return max_good
