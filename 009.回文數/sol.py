class Solution(object):
    
    def isPalindrome(self, x):
        
        if x < 0 or (x%10 == 0 and x !=0):
            return False
        
        else:
            revertedNumber = 0
            while(x > revertedNumber): 
                revertedNumber = revertedNumber * 10 + x % 10
                x /= 10
                
            if revertedNumber == x or revertedNumber/10 ==x :
                return True
        