class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start,end=0,0
        for i in range(len(s)):
            len_even=self.max_sub(s,i,i+1)
            len_odd=self.max_sub(s,i,i)
            max_=max(len_even,len_odd)
            if max_>(end-start):
                start=i-(max_-1)//2
                end=i+max_//2
        return s[start:end+1]
        
    def max_sub(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return right-left-1
if __name__=="__main__":
    s=str(input("Type here the string to check if it's a palindrome: "))
    sol=Solution()
    result=sol.longestPalindrome(s=s)
    print(f"The result is: {result}")