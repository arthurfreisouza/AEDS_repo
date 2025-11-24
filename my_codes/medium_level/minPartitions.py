import math
class Solution:
    def minPartitions(self, n: str) -> int:
        max_val=float('-inf')
        for val in n:
            int_val=int(val)
            if int_val>=max_val:
                max_val=int_val
        return max_val
    #     int_n=int(n)
    #     array_binary_numbers=[]
    #     for i in range(int_n):
    #         array_binary_numbers.append(int(bin(i)[2:]))

    #     counter=0
    #     while int_n>0:
    #         for val in array_binary_numbers[::-1]:
    #             if int_n-val>0:
    #                 int_n-=val
    #                 counter+=1
    #                 print(val)
    #     return counter

    # def build_bin_arr(n: str):
    #     bin_arr=[]
    #     int_n=int(n)
    #     max_divisor=int(math.log(int_n,2))
    #     while max_divisor>=0:
    #         actual=2**max_divisor
    #         if (int_n-actual>=0):
    #             int_n-=actual
    #             bin_arr.append(1)
    #         else:
    #             bin_arr.append(0)
    #         max_divisor-=1
    #     return bin_arr
def main():
    n=str(input('Type here a string: '))
    sol=Solution()
    result=sol.minPartitions(n=n)
    print(f'The result is: {result}')

if __name__=="__main__":    
    main()