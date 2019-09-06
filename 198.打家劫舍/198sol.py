class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        
        pin = 3
        dp = [nums[0]] + [nums[1]] + [nums[0] + nums[2]] + [0] * (n-3)
        
        while pin < n:
            dp[pin] = max(dp[pin-2]+nums[pin], dp[pin-3]+nums[pin])
            pin += 1
            
        return max(dp)