from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue

                if val in rows[i]:
                    return False
                rows[i].add(val)

                if val in cols[j]:
                    return False
                cols[j].add(val)

                box_index = (i // 3) * 3 + (j // 3)
                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)

        return True
