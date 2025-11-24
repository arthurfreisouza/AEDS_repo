from typing import List

# I think this is Easiest Medium problems .
# no need to think about anything extra , just put it into stack and when ever operator occurs pop two values and do operation accordingly and push res into stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        list_val=['+','-','*','/']
        stack=[]
        # breakpoint()
        for val in tokens:
            if val in list_val:
                num2=stack.pop()
                num1=stack.pop()
                if val=='+':
                    stack.append(int(num2)+int(num1))
                elif val=='-':
                    stack.append(int(num2)-int(num1))
                elif val=='*':
                    stack.append(int(num2)*int(num1))
                elif val=='/':
                    stack.append(int(num2)//int(num1))
            else:
                stack.append(val)
        return stack[0]
if __name__=="__main__":
    tokens=[]
    while True:
        token=str(input('Type here a single value for the token'))
        if token=='400':
            break
        tokens.append(token)
    sol=Solution()
    result=sol.evalRPN(tokens=tokens)
    print(f"The result is: {result}")