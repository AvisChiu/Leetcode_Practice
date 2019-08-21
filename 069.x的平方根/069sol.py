class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
         
        left = 1 
        right = x//2 
       
        while left < right:
            
            mid = (left + right + 1) //2 
            square = mid*mid
            
            if square > x:
                right = mid - 1
            else:
                left = mid
                
        return left
       
                
            
          
            
       

            