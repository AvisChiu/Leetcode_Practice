class Solution(object):
    def plusOne(self, digits):
        
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            return [1]
        
        tmp = 0
        for i in range(len(digits)):
            s = digits[i]*(10**(len(digits)-i-1))
            tmp = tmp + s  
        result = tmp + 1
        
        trans = str(result)
        resList = []
        for j in range(len(trans)):
            resList.append(trans[j])
        
        return resList
        
       
                
            
          
            
       

            