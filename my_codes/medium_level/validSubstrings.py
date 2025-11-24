class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        counter=0
        it_=0
        aux=word1
        while it_<len(word1):
            if word2 in aux:
                counter+=1
                aux=word1[:len(word1)-it_]
            it_+=1
        while it_<len(word1):
            if word2 in aux:
                counter+=1
                aux=word1[len(word1)-it_:]
            it_+=1
        return it_
if __name__=="__main__":
    word1=str(input("Type here the first word: "))
    word2=str(input("Type here the first word: "))
    sol=Solution()
    result=sol.validSubstringCount(word1=word1,word2=word2)
    print(f"The result is: {word2}")