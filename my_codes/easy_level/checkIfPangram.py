class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        str_alphabet="abcdefghijklmnopqrstuvwxyz"
        alphabet_={}
        for i in str_alphabet:
            alphabet_[i]=1
        for i in range(len(sentence)):
            if sentence[i] in alphabet_ and alphabet_[sentence[i]]==1:
                alphabet_[sentence[i]]-=1
        for i in alphabet_.values():
            if i!=0:
                return False
        return True
if __name__=="__main__":
    sentence=str(input("Type here a sentence: "))
    sol=Solution()
    result=sol.checkIfPangram(sentence=sentence)
    print(f"The result is: {result}")