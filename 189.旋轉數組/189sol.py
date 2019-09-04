class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
       
        # method 1: 5.07%, 18.07%
        for i in range(k):
            tmp = nums.pop()
            nums.insert(0,tmp)
        
        
        # method 2: 
        
        # n = len(nums)
        # k %= n
        # nums[:] = nums[::-1]
        # print(nums)
        # nums[:k] = nums[:k][::-1]
        # print(nums)
        # nums[k:] = nums[k:][::-1]
        # print(nums)
        
        