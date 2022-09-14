class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = one = two = 0
        while two < len(nums):
            if nums[two] == 0:
                nums[two], nums[one] = nums[one], nums[two]
                nums[zero], nums[one] = nums[one], nums[zero]
                zero += 1
                one += 1
            elif nums[two] == 1:
                nums[two], nums[one] = nums[one], nums[two]
                one += 1
            two += 1
