class Solution:
    def numSub(self, s: str) -> int:
        Mod = 10 ** 9 + 7
        count = 0
        result = 0
        for k in s:
            if k == '1':
                count += 1
            else:
                result += count * (count + 1) // 2 % Mod
                count = 0
        result += count * (count + 1) // 2 % Mod
        return result
        