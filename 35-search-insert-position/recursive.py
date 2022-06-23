class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        '''O(lg n) divide-and-conquer (binary search)'''
        first = 0
        last = len(nums) # Use pointers for array
        return self.searchRecurse(nums, target, first, last)
    def searchRecurse(self, nums, target, first, last):
        mid = (first + last) // 2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            if mid == len(nums) - 1 or target < nums[mid + 1]:
                return mid + 1
            return self.searchRecurse(nums, target, mid + 1, last)
        if target < nums[mid]:
            if mid == 0 or target > nums[mid - 1]:
                return mid
            return self.searchRecurse(nums, target, first, mid - 1)
        
