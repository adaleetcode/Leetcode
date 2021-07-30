class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        rem = []
        for i in range(len(s)):
            if not s[i].isalpha():
                if len(rem) and s[rem[-1]]=='(' and s[i]==')':
                    rem.pop()
                else:
                    rem.append(i)
                
        start = 0
        req = ''
        for i in range(len(s)):
            if start!=len(rem) and i==rem[start]:
                start+=1
            else:
                req+=s[i]
        return req