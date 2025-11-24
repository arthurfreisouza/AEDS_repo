import math

class Solution:
    def convertTodecimal7(self, num: int) -> str:
        total=0
        num=list(str(num))
        num=[int(x) for x in num]
        for index,value in enumerate(reversed(num)):
            total+=value*7**index
        return total


if __name__=="__main__":
    num=int(input("Type here a value in the basis 7: "))
    sol=Solution()
    result=sol.convertTodecimal7(num=num)
    print(f"The result is: {result}")
