class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1==0 or num2==0:
            return 0
        counter=0
        while num1!=0 and num2!=0:
            # breakpoint()
            if num1>=num2:
                num1=num1-num2
            else:
                num2=num2-num1
            counter+=1
        return counter
if __name__=="__main__":
    num1=int(input('Type here num1: '))
    num2=int(input('Type here num2: '))
    sol=Solution()
    result=sol.countOperations(num1=num1,num2=num2)
    print(f"The result is: {result}")