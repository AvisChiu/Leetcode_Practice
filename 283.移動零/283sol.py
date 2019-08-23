class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pin1 = 0
        pin2 = len(nums)
        
        while pin1 != pin2:
            if nums[pin1] == 0:
                nums.append(0)
                del nums[pin1]
                pin2 = pin2 - 1
            else:
                pin1 = pin1 + 1
                
        
        return nums
        