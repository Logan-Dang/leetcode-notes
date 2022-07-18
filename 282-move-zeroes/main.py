class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # O(n)
        """
        Do not return anything, modify nums in-place instead.
        """
        point = 0
        for i, v in enumerate(nums):
            if v != 0:
                nums[i], nums[point] = nums[point], nums[i]
                point += 1
            
