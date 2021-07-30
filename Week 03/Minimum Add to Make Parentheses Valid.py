from collections import deque
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
            stack=deque()
            top=-1
            ans=0
            for i in range(len(s)):
                if s[i]=="(":
                    stack.append(s[i]) 
                    top+=1
                else:
                    if top==-1:
                        ans+=1
                    else:
                        stack.pop()
                        top-=1
            ans+=len(stack)
            return ans