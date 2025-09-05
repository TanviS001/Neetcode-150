class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={')':'(',']':'[','}':'{'}

        for i in s:
            if i in dic.values():
                stack.append(i)
            if i in dic:
                if stack and stack[-1]==dic[i]:
                    stack.pop()
                else:
                    return False
            
        if stack:
            return False
        else:
            return True
