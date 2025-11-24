class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        s=list(s)
        current_str=""
        for char in s:
            if char=='(':
                stack.append(current_str)
                current_str=""
            elif char==')':
                reversed_inner=current_str[::-1]
                prefix=stack.pop()
                current_str=prefix+reversed_inner
            else:
                current_str+=char
        return current_str

if __name__=="__main__":
    s=str(input('Type here a string s: '))
    sol=Solution()
    result=sol.reverseParentheses(s=s)
    print(f"The result is: {result}")