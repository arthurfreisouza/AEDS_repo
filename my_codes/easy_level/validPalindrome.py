class Solution:
    def validPalindrome(self, s: str) -> bool:
        start,end=0,len(s)-1
        if len(s)==3 and s[start]==s[end]:
            return True
        elif len(s)==3 and s[start]!=s[end]:
            return False
        else:
            count=0
            while start<=end:
                if s[start]!=s[end]:
                    count+=1
                    print(start)
                if count>1:
                    return False
                start+=1
                end-=1
            return True
        
if __name__=="__main__":
    s=str(input("Type here your string: "))
    sol=Solution()
    result=sol.validPalindrome(s=s)
    print(f"The result is: {result}")