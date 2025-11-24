class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            # count+=self.n_binary_substrings(s,i,i)
            count+=self.n_binary_substrings(s,i,i+1)
        return count
    def n_binary_substrings(self,s,left,right):
        count=0
        while left>=0 and right<len(s):
            if s[left]!=s[right]:
                count+=1
            left-=1
            right+=1
        return count
if __name__=="__main__":
    s=str(input("Type here your string: "))
    sol=Solution()
    result=sol.countBinarySubstrings(s=s)
    print(f"The result is: {result}")