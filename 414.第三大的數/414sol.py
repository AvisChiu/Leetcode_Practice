class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        nums[:] = nums[::-1]
        flag = 0
        
        for i in range(len(nums)-1):
            if nums[i] >  nums[i+1]:
                flag += 1
                if flag == 2:
                    return nums[i+1]
            
        
        return nums[0]