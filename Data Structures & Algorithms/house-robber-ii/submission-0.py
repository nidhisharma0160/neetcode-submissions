class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):

            prev2, prev1 = 0,0

            for x in arr:
                cur = max(prev1, x+prev2)
                prev2 = prev1 
                prev1 = cur

            return prev1
        
        if len(nums) == 1: return nums[0]

    
        return max(
            helper(nums[:-1]), 
            helper(nums[1:])
        )
