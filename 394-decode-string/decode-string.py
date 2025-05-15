class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        res = ""
        num = 0
        for i in s:
            if i.isdigit():
                num = (num * 10 )+ int(i)
            elif i == "[":
                st.append((res,num))
                num = 0
                res = ""
            elif i == "]":
                prev,n = st.pop()
                res = prev + res * n
            else:
                res += i
        return res

        