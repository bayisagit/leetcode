class Solution:
    def reverseWords(self, s: str) -> str:
        spit = s.split()
        finres = []
        for i in spit:
            rvew = i[::-1]
            finres.append(rvew)
        return " ".join(finres)
