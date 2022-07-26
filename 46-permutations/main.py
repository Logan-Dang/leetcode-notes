class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        queue = [[]]
        for i in nums: # O(n)
            n = []
            while queue: # [1, 1, 2, 6, 24] O(??
                subset = queue.pop(0)
                for j in range(len(subset) + 1): # [1, 2, 3, 4] O(n)
                    l = subset[:]
                    l.insert(j, i)
                    n.append(l)
            queue = n
        return queue
