class Solution:
    def countSubstrings(self, s: str) -> int:
        counter=0
        for i in range(len(s)):
            counter+=self.return_n_palindromes(s,i,i)
            counter+=self.return_n_palindromes(s,i,i+1)
        return counter
    def return_n_palindromes(self,str_,left,right)->int:
        n_palindromes=0
        while left>=0 and right<len(str_) and str_[left]==str_[right]:
            n_palindromes+=1
            left-=1
            right+=1
        return n_palindromes

if __name__=="__main__":
    s=str(input("Type here a string: "))
    sol=Solution()
    result=sol.countSubstrings(s=s)
    print(f"The number of palindromes is: {result}")