class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) < 2:
            return nums[0]
        
        n = len(nums)
        dp = [0] * n 
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[n-1]










"""
    #brute force approach time complexity: O(2^n)
    def rob(self, nums: List[int]) -> int:
        return self.helper(nums,0,0)
    
    def helper(self, nums, idx, robbings):
        #base case
        if idx >= len(nums):
            return robbings
        
        #choose to rob the house
        case1 = self.helper(nums, idx+2, robbings+nums[idx])

        #not choose to rob the house

        case2 = self.helper(nums, idx+1, robbings)


        return max(case1, case2)     

        """   