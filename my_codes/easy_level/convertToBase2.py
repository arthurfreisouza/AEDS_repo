import math

class Solution:
    def convertToBase2(self, num: int) -> str:
        is_neg = num<0
        dict_={}
        num=abs(num)
        while num>0:
            max_exp=int(math.log(num,2)) # Take the maximum index
            digits=num//2**max_exp
            dict_[max_exp]=digits
            num-=digits*2**max_exp
        arr_=[]
        if is_neg:
            arr_.append('-')
        end=max(dict_.keys())
        while end >= 0:
            arr_.append(str(dict_.get(end, 0)))
            end -= 1

        return "".join(arr_)
if __name__=="__main__":
    num=int(input("Type here an integer: "))
    sol=Solution()
    result=sol.convertToBase2(num=num)
    print(f"The result is: {result}")