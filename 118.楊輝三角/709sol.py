class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        
        
        # method 1:
        
        return str.lower()
            
            
        # method 2:
        
        # ls = list(str)
        # for temp in ls:
        #     if 65<=ord(temp) and ord(temp)<=90:
        #         ls[ls.index(temp)] = chr(ord(temp)+32)
        # return "".join(ls)
        
        
        