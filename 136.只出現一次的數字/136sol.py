class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        method : List 5.50% , 30.26%
        empty_ = []
        for items in nums:
            if items not in empty_:
                empty_.append(items)
            else:
                empty_.remove(items)
        
        return (empty_[0])
             
        
        method 2: Dictionary:
        dic = {}
        for items in nums:
            try:
                dic.pop(items)
            except:
                dic[items] = 1         
        # print(type(dic.popitem()))
        return dic.popitem()[0]