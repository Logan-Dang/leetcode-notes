class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Notes for next run, only 1 loop
        first, last = 0, len(matrix) - 1
        while first <= last:
            mid = (first + last) // 2
            if target < matrix[mid][0]:
                last = mid - 1
            elif target > matrix[mid][-1]:
                first = mid + 1
            else:
                break
        else: return False
        row = matrix[mid]
        first, last = 0, len(row) - 1
        while first <= last:
            mid = (first + last) // 2
            if target > row[mid]:
                first = mid + 1
            elif target < row[mid]:
                last = mid - 1
            else: return True
        return False
