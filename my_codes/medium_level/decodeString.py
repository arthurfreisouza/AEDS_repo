class Solution:
    def decodeString(self, s: str) -> str:
        list_numbers=['0','1','2','3','4','5','6','7','8','9']
        stack=[]
        for val in s:
            if val==']':
                values=[]
                while stack and stack[-1]!='[':
                    values.append(stack.pop())
                stack.pop()
                number=[]
                while stack and stack[-1] in list_numbers:
                    number.append(stack.pop())
                number=int(''.join(number[::-1]))
                values=''.join(values[::-1])
                stack.append(number*values)
            else:
                stack.append(val)
        return ''.join(stack)
if __name__=="__main__":
    s=str(input('Type here the value of s: '))
    sol=Solution()
    result=sol.decodeString(s=s)
    print(f"The result is: {result}")