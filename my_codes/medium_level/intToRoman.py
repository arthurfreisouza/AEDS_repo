class Solution:
    def intToRoman(self, num: int) -> str:
        map_ = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }

        # Sort items by value descending (important!)
        items = sorted(map_.items(), key=lambda x: x[1], reverse=True)

        final_result = []
        while num > 0:
            for symbol, value in items:
                if num // value > 0:   # check how many times this symbol fits
                    n_times = num // value
                    num -= n_times * value
                    for _ in range(n_times):
                        final_result.append(symbol)
        return "".join(final_result)


if __name__=="__main__":
    num=int(input("Type here an integer: "))
    sol=Solution()
    result=sol.intToRoman(num=num)
    print(f"The result is: {result}")