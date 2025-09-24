class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0  # Base case: f(1, k) = 0 (0-indexed)
        for i in range(2, n + 1):  # Build up from 2 to n
            winner = (winner + k) % i
        return winner + 1  # Convert to 1-indexed