class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        first, last = 0, len(nums) # Use pointers for array
        while (first != last):
            mid = (first + last) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                if mid == len(nums) - 1 or target < nums[mid + 1]:
                    return mid + 1
                first = mid + 1
            if target < nums[mid]:
                if mid == 0 or target > nums[mid - 1]:
                    return mid
                last = mid - 1
        return first