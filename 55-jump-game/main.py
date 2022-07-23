class Solution:
    def canJump(self, nums: List[int]) -> bool:        
        i = len(nums) - 2
        pointer = len(nums) - 1
        while i >= 0:
            if nums[i] + i >= pointer:
                pointer = i
            i -= 1
        return pointer == 0
