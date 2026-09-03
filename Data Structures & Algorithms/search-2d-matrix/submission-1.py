class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix),len(matrix[0])

        l, r = 0, m-1
        res = -1
        while l <= r:
            mid = l +(r-l)//2
            if matrix[mid][0] <= target:
                res = mid
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1

        if res == -1:
            return False
        
        l, r = 0, n-1

        while l <= r:
            mid = l +(r-l)//2
            if matrix[res][mid] < target:
                l = mid + 1
            elif matrix[res][mid] > target:
                r = mid - 1
            else:
                return True

        return False