class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current = nums[0]
        count = 0
        for n in nums:
            if n == current:
                count += 1
            else:
                count -= 1
                if count == 0: 
                    current = n
                    count += 1
        return current
