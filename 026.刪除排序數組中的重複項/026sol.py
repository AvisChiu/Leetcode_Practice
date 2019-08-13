
class Solution(object):
	
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        pin = "xxxx"
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = pin         
        # print(nums)           
        while pin in nums:
            nums.remove(pin)       
        # print(nums)