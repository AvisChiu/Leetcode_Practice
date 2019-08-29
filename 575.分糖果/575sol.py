class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        
        dic = {}
        for i in candies:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        
        average = len(candies) / 2 
        cata = len(dic.keys())
        
        if average < cata:
            return average
        else:
            return cata