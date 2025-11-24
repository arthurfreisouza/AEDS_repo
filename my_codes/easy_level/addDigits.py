class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num))==1:
            return num
        while True:
            sum_=0
            num=str(num)
            for i in num:
                sum_+=int(i)
            # breakpoint()
            if len(str(sum_))==1:
                return sum_
            num=sum_  
if __name__=="__main__":
    num=int(input("Type here a value to num"))
    sol=Solution()
    result=sol.addDigits(num=num)
    print(f"The result is: {result}")