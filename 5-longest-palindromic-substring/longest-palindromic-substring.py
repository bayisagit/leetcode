class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        def expand(s,left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
            return right - left - 1


        start = 0 
        end = 0
        for i in range(len(s)):
            odd = expand(s,i,i)
            even = expand(s,i,i+1)
            maxlen=max(odd,even)
            if maxlen > end - start:
                start = i - (maxlen-1) // 2
                end = i + (maxlen) // 2
        return s[start:end+1]
                 


        