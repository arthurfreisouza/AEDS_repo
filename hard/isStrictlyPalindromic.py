import math
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # 1- Converting to binary.
        for i in range(2,n):
            bin_arr=[]
            max_exp=math.log(n,i)
            while max_exp>=0:
                actual_divisor=i**max_exp
                if n>=actual_divisor:
                    bin_arr.append(1)
                    n-=actual_divisor
                else:
                    bin_arr.append(0)
                max_exp-=1
            left,right=0,len(bin_arr)-1
            while left<right:
                if bin_arr[left]!=bin_arr[right]:
                    return False
                left+=1
                right-=1
            return True
# import math
# class Solution:
#     def minimumOneBitOperations(self, n: int) -> int:
#         # Converting to binary (MSB -> LSB)
#         arr_=[]
#         counter_ret=0
#         max_exp=n.bit_length()-1
#         while max_exp>=0:
#             actual_divisor=2**max_exp
#             if n>=actual_divisor:
#                 arr_.append(1)
#                 n-=actual_divisor
#             else:
#                 arr_.append(0)
#             max_exp-=1

#         # When we flip at index i (MSB->LSB), we must toggle bits i..end (include current bit)
#         for i in range(len(arr_)):
#             if arr_[i]==0:
#                 continue
#             counter_ret += 1
#             for j in range(i, len(arr_)):      # include current bit
#                 arr_[j] = 1 - arr_[j]         # toggle

        # return counter_ret
if __name__=="__main__":
    n=int(input('Type here a value for n: '))
    sol=Solution()
    result=sol.isStrictlyPalindromic(n=n)
    print(f"The result is: {result}")