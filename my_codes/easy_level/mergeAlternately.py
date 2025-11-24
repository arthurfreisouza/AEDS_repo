class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        max_size=int([len(word1) if len(word1)>len(word2) else len(word2)][0])
        result=[]
        for i in range(max_size):
            if i<=len(word1)-1:
                result.append(word1[i])
            if i<=len(word2)-1:
                result.append(word2[i])
        return "".join(result)

if __name__=="__main__":
    word1=str(input("Type here the first word: "))
    word1 = "".join(x for x in word1 if x.isalnum())
    word2=str(input("Type here the second word: "))
    word2 = "".join(x for x in word2 if x.isalnum())
    sol=Solution()
    result=sol.mergeAlternately(word1,word2)
    print(f"The result is: {result}")