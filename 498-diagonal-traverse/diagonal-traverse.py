class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        for d in range(m + n - 1):
            row = 0 if d < n else d - n + 1
            col = d if d < n else n - 1
            intermidiate = []
            while row < m and col >= 0:
                intermidiate.append(mat[row][col])
                row += 1
                col -= 1
            if d % 2 == 0:
                result.extend(intermidiate[::-1])
            else:
                result.extend(intermidiate)
        return result
        