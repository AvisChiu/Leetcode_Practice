
class Solution(object):
    def removeElement(self, nums, val):
         
        pin = 0
        
        if len(nums) == 1 and nums[0] != val:
            return 1
        if len(nums) == 1 and nums[0] == val:
            return 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pin] = nums[i]
                pin = pin + 1
                
        return pin 