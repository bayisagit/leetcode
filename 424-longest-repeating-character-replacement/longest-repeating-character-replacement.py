class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxval = 0
        result = 0
        substrin = {}
        l = 0
        for r in range(len(s)):
            righchar = s[r]
            substrin[righchar] = substrin.get(righchar,0) + 1
            maxval = max(maxval,substrin[righchar])
            while (r - l + 1) - maxval > k:
                substrin[s[l]] -= 1
                l+=1
            result = max(result,r-l+1)

        return result