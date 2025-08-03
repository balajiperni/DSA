class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]i
        """
        dic = {}
        for char in strs:
            key = ''.join(sorted(char))
            if key in dic:
                dic[key].append(char)
            else:
                dic[key] = [char]
        return list(dic.values())            
         
        