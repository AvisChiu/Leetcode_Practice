class Solution(object):
    def searchInsert(self, nums, target):
       
        # method 1 defeat 96.94%, 25.59%
#         if target in nums:
#             return nums.index(target)
        
#         else:
#             nums.append(target)
#             nums.sort()
#             if target in nums:
#                 return nums.index(target)
            
        # method 2 defeat 51.12%, 21.29%
#         for i in range(len(nums)):
#             if nums[i] >= target:
#                 return i

#         return len(nums)

        # method 3: binary serach
        # defeat 8.18%, 33.55%
        
        left = 0
        right = len(nums)-1
        
        
        while left <= right:
            
            mid = (right+left)//2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1 
            else:
                return mid
            
        return left