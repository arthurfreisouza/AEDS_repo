class Solution:
    def fizzBuzz(self, n: int):
        lst_=[]
        for i in range(1,n+1):
            breakpoint()
            if i%3==0 and i%5==0:
                lst_.append("FizzBuzz")
            elif i%3==0 and i%5!=0:
                lst_.append("Fizz")
            elif i%5==0 and i%3!=0:
                lst_.append("Buzz")
            else:
                lst_.append(str(i))
        return lst_
if __name__=="__main__":
    n=int(input("Type here an integer: "))
    sol=Solution()
    result=sol.fizzBuzz(n=n)
    print(f"The result is: {result}")