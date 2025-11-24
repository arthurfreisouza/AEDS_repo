class Solution:
    def countSegments(self, s: str) -> int:
        if s == "":
            return 0
        s = s.split()
        count = 0
        for i in range(len(s)):
            if s[i] != "":
                count += 1
        return count

if __name__=="__main__":
    s=str(input("Type here a value to s: "))
    sol=Solution()
    result=sol.countSegments(s=s)
    print(f"The result is: {result}")