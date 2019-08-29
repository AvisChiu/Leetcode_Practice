class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # method: Dictionary 86.36%, 43.01%
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
                
        for j in t:
            if j in dic:
                dic[j] -= 1
            else:
                dic[j] = -1
                
        for items in t:
            if dic[items] == -1:
                return items