from math import log
class Solution:
    def hammingWeight(self, n: int) -> int:
        max_exp=int(log(n,2))
        final_arr=[]
        breakpoint()
        while max_exp>=0:
            actual=2**max_exp
            if n-actual>=0:
                final_arr.append(1)
                n-=actual
            else:
                final_arr.append(0)
            max_exp-=1
        counter=0
        for i in final_arr:
            if i==1:
                counter+=1
        return counter
    
def main():
    n=int(input('Type here a value for n: '))
    sol=Solution()
    result=sol.hammingWeight(n=n)
    print(f"The result is: {result}")

if __name__=="__main__":
    main()