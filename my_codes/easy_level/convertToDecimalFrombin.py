import math

class Solution:
    def convertTodecimal2(self, num: int) -> str:
        total=0
        num=list(str(num))
        num=[int(x) for x in num]
        for index,value in enumerate(reversed(num)):
            total+=value*2**index
        return total


if __name__=="__main__":
    num=int(input("Type here a value in the basis 2: "))
    sol=Solution()
    result=sol.convertTodecimal2(num=num)
    print(f"The result is: {result}")
