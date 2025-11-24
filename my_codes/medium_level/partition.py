class Solution:
    def partition(self, s: str) -> list:
        result_=[]
        for i in range(len(s)):
            odd=self.find_palindromes(s,i,i)
            even=self.find_palindromes(s,i,i+1)
            result_.extend(odd)
            result_.extend(even)
        return list(dict.fromkeys(result_))
    def find_palindromes(self,s,left,right):
        arr_=[]
        while left>=0 and right<len(s) and s[left]==s[right]:
            arr_.append(s[left:right+1])
            left-=1
            right+=1
        return arr_

if __name__=="__main__":
    s=str(input("Type here an input str: "))
    sol=Solution()
    result=sol.partition(s=s)
    print(f"The result is: {result}")