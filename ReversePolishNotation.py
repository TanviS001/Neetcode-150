# o(n) space and time

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for token in tokens:
            if token in {'+','-','/','*'}:
                b=int(stack.pop())
                a=int(stack.pop())

                if token=="+":
                    ans=a+b
                elif token=="*":
                    ans=a*b
                elif token=="-":
                    ans=a-b
                elif token=="/":
                    ans=int(a/b)
                
                stack.append(ans)
            else:
                stack.append(int(token))

        return stack[0]
