import math

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        dict_ = {}
        is_neg = num < 0
        num = abs(num)

        while num > 0:
            max_exp = int(math.log(num, 7))  # largest exponent
            digit = num // (7 ** max_exp)    # how many times it fits
            dict_[max_exp] = digit
            num -= digit * (7 ** max_exp)

        arr_ = []
        if is_neg:
            arr_.append('-')

        # Fill from highest exponent down to 0
        end = max(dict_.keys())
        while end >= 0:
            arr_.append(str(dict_.get(end, 0)))
            end -= 1

        return "".join(arr_)


if __name__=="__main__":
    num=int(input("Type here an integer: "))
    sol=Solution()
    result=sol.convertToBase7(num=num)
    print(f"The result is: {result}")
