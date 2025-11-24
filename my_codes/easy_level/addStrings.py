class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = Solution.convert_numbers(num1, num2)
        end_ = len(num1) - 1
        final_result = []
        next_sum = 0

        while end_ >= 0:
            sum_ = num1[end_] + num2[end_] + next_sum
            final_result.append(sum_ % 10)
            next_sum = sum_ // 10
            end_ -= 1

        if next_sum:  # carry left over
            final_result.append(next_sum)

        # reverse and convert to string
        return "".join(map(str, reversed(final_result)))

    def convert_numbers(num1: str, num2: str):
        num1 = [int(x) for x in num1]
        num2 = [int(x) for x in num2]
        diff = len(num1) - len(num2)

        if diff > 0:
            num2 = [0] * diff + num2
        elif diff < 0:
            num1 = [0] * (-diff) + num1

        return num1, num2

        
if __name__=="__main__":
    num1=str(input("Type here a value to num1: "))
    num2=str(input("Type here a value to num2: "))
    sol=Solution()
    result=sol.addStrings(num1=num1,num2=num2)
    print(f"The result is: {result}")