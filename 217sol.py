class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
          
        flag = False
        for key, value in dic.items():
            if value >= 2: 
                flag = True
                
        return flag
        
        