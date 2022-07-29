class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 1):
            if i - 1 >= 0 and nums[i] == nums[i - 1]: continue
            s = set()
            for j in range(i + 1, len(nums)):
                if j + 1 < len(nums) and nums[j] == nums[j + 1]: 
                    s.add(nums[j])
                    continue
                
                if -(nums[i] + nums[j]) in s:
                    res.append([nums[i], nums[j], -(nums[i] + nums[j])])
                else: s.add(nums[j])
        return res
