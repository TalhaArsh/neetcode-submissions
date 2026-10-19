class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        result = []

        while left < right and top < bottom:
            # Left to right
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            # Top to bottom
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            # Stop if no rows or columns remain
            if top >= bottom or left >= right:
                break

            # Right to left
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1

            # Bottom to top
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        return result