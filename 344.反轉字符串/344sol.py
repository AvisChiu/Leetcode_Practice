class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        pin2 = len(s) - 1
    
        for i in range(len(s)/2):
            tmp = ""
            tmp = s[i] 
            s[i] = s[pin2]
            s[pin2] = tmp
            pin2 = pin2 - 1