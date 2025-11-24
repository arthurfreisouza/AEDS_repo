from math import log
class Solution:
    def reverseBits(self, n: int) -> int:
        if n==0:
            return 0
        final_arr=[]
        max_exp=int(log(n,2))
        # while max_exp>=0:
        for max_exp in range(31,-1,-1):
            actual_val=2**max_exp
            if n-actual_val>=0:
               final_arr.append('1')
               n-=actual_val
            else:
                final_arr.append('0')
            # max_exp-=1
        # Inverting the number
        # left,right=0,len(final_arr)-1
        # while left<right:
        #     final_arr[left],final_arr[right]=final_arr[right],final_arr[left]
        #     left+=1
        #     right-=1
        # Transforming the inverted
        counter=0
        for index,value in enumerate(final_arr):
            counter+=int(value)*2**index
        return counter


def main():
    n=int(input("Type here a value: "))
    sol=Solution()
    result=sol.reverseBits(n=n)
    print(f"The result is: {result}")
if __name__=="__main__":
    main()