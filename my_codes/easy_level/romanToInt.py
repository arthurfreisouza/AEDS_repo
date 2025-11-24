class Solution:
    def romanToInt(self, s: str) -> int:
        map_={"I":1,
              "V":5,
              "X":10,
              "L":50,
              "C":100,
              "D":500,
              "M":1000}
        counter
        for i in range(len(s)-1):
            if map_.get(s[i])<map_.get(s[i+1]):
                counter-=map_.get(s[i])
            else:
                counter+=map_.get(s[i])
        return counter

if __name__=="__main__":
    roman_number=str(input("Type here a number: "))
    sol=Solution()
    result=sol.romanToInt(s=roman_number)
    print(f"The result is: {result}")