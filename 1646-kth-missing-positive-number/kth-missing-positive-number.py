class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        current = 1
        missing = 0
        i = 0
        while True:
            if i < len(arr) and arr[i] == current:
                i += 1
            else:
                missing += 1
                if missing == k:
                    return current
            current += 1
        