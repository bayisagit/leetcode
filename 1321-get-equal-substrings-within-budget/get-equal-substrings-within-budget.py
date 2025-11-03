class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l=0
        maxlen=0
        totcost=0
        for r in range(len(t)):
            totcost += abs(ord(s[r])-ord(t[r]))
            if totcost > maxCost:
                totcost -= abs(ord(s[l]) - ord(t[l]))
                l+=1
            maxlen = max(maxlen,r-l+1)
        return maxlen