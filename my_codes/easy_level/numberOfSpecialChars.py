class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word=sorted(list(set(word)))
        dict_={}
        for i in range(len(word)):
            if word[i].isupper() and word[i] not in dict_:
                dict_[word[i]]=0
            if word[i].islower() and word[i].upper() in dict_:
                dict_[word[i].upper()]+=1
        count=0
        for value in dict_.values():
            if value>0:
                count+=1
        return count
        
if __name__=="__main__":
    word=str(input("Type here a value to the word: "))
    sol=Solution()
    result=sol.numberOfSpecialChars(word=word)
    print(f"The result is: {result}")