class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count=sum([1 for x in word if x.isupper()==True])
        if count==len(word) or count==0:
            return True
        elif count==1 and word[0].isupper()==True:
            return True
        else:
            return False

if __name__=="__main__":
    word=str(input("Type here a word: "))
    sol=Solution()
    result=sol.detectCapitalUse(word=word)
    print(f"The result is: {result}")