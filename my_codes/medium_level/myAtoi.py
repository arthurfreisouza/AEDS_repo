# class Solution:
#     def myAtoi(self, s: str) -> int:
        # s = s.strip()
        # if len(s) == 0:
        #     return 0

        # signal = '+'
        # if s[0] in ['-', '+']:
        #     if s[0] == '-':
        #         signal = '-'
        #     s = s[1:]

        # max_limit = 2**31 - 1
        # min_limit = -2**31
        # total = 0

        # valid_houses = -1
        # for i in s:
        #     if not i.isdigit():
        #         break
        #     valid_houses += 1

        # if valid_houses == -1:
        #     return 0

        # counter = valid_houses
        # for index, value in enumerate(s[:valid_houses+1]):
        #     if signal == '-':
        #         total -= int(value) * 10**(counter - index)
        #         if total < min_limit:
        #             return min_limit
        #     else:
        #         total += int(value) * 10**(counter - index)
        #         if total > max_limit:
        #             return max_limit

        # return total
    

class Solution:
    def myAtoi(self, s: str) -> int:
            s = s.strip()
            if not s:
                return 0

            # 1. Handle sign
            sign = 1
            if s[0] in ['-', '+']:
                if s[0] == '-':
                    sign = -1
                s = s[1:]  # skip sign

            # 2. Convert digits
            result = 0
            for ch in s:
                if not ch.isdigit():
                    break
                result = result * 10 + int(ch)

            result *= sign

            # 3. Clamp to 32-bit signed integer range
            INT_MAX = 2**31 - 1
            INT_MIN = -2**31
            if result > INT_MAX:
                return INT_MAX
            if result < INT_MIN:
                return INT_MIN
            return result
    
if __name__=="__main__":
    s=[]
    while True:
        digit=str(input('Type here a digit to add in the string: '))
        if digit=='400':
            break
        s.append(digit)
    s=''.join(s)
    sol=Solution()
    result=sol.myAtoi(s=s)
    print(f"The result is: {result}")