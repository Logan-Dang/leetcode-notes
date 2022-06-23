# O(n) solution
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        candidate, sum = nums[0], nums[0]
        for n in nums[1:]:
            if n > sum:
                sum = n if sum < 0 else sum + n
            else:
                candidate = max(candidate, sum)
                sum += n
        return max(candidate, sum)