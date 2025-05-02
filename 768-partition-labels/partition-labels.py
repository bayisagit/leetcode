class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i , char in enumerate(s):
            last[char] = i
        outp=[]
        st = end = 0
        for i , char in enumerate(s):
            end = max (end , last[char])
            if i == end:
                outp.append(end - st + 1)
                st = i + 1
        return outp
        