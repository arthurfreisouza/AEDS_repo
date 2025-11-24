class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        left,right=0,len(s)-1
        while left<=right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return " ".join(s)
if __name__=="__main__":
    s=str(input("Type here a value for s: "))
    sol=Solution()
    result=sol.reverseWords(s=s)
    print(f"The result is: {result}")