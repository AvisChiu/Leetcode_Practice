class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dic = {}
        
        for items in J:
            dic[items] = 1
        
        count = 0
        for i in range(len(S)):
            if S[i] in dic:
                count = count + 1
                
        return count