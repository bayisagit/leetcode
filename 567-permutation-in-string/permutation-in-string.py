class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        base = ord('a')

        for ch in s1:
            cnt1[ord(ch) - base] += 1

       
        for i in range(n1):
            cnt2[ord(s2[i]) - base] += 1

        if cnt1 == cnt2:
            return True

        
        for i in range(n1, n2):
            
            cnt2[ord(s2[i]) - base] += 1
            
            cnt2[ord(s2[i - n1]) - base] -= 1
            if cnt1 == cnt2:
                return True

        return False
