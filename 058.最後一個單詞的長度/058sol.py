class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # method 1: 81.23%, 23.57
        # tmp = s.split()
        # if len(tmp) == 0:
        #     return 0
        # return(len(tmp[-1]))
    
       
        # method 2: 
        end = len(s) - 1
        while end >= 0 and s[end] == " ":
            end -= 1
        if end == -1: return 0
        start = end
        while start >= 0 and s[start] != " ":
            start -= 1
        return end - start


            