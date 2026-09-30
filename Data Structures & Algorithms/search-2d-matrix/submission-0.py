class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        print(m,n)

        targetRow = 0
        for i in range(m):
            if target ==  matrix[i][0] or target == matrix[i][-1]:
                return True
            elif matrix[i][0] < target < matrix[i][-1]:
                targetRow = i

        beginingIndex = 0 
        endIndex = n -1

        while(beginingIndex <= endIndex):
            midpoint = (beginingIndex + endIndex) // 2
            midVal = matrix[targetRow][midpoint]
            if midVal == target:
                return True
            elif midVal > target:
                endIndex = midpoint - 1
            else:
                beginingIndex = midpoint + 1
        return False