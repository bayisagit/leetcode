from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        wall_set = {(r, c) for r, c in walls}
        guard_set = {(r, c) for r, c in guards}
        guarded = set()

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r, c in guards:
            for dr, dc in directions:
                x, y = r + dr, c + dc
                while 0 <= x < m and 0 <= y < n and (x, y) not in wall_set and (x, y) not in guard_set:
                    if (x, y) not in guarded:
                        guarded.add((x, y))
                    x += dr
                    y += dc

        # Count unguarded and unoccupied cells
        total = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in wall_set and (i, j) not in guard_set and (i, j) not in guarded:
                    total += 1

        return total
