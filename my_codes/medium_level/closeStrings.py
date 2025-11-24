class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        dict1={}
        for val in word1:
            if val not in dict1:
                dict1[val]=1
            else:
                dict1[val]+=1
        dict2={}
        for val in word2:
            if val not in dict2:
                dict2[val]=1
            else:
                dict2[val]+=1
        if len(arr1) != len(arr2):
            return False
        it_=0
        arr1=sorted(dict1.keys())
        arr2=sorted(dict2.keys())
        while it_<len(arr1):
            if arr1[it_]!=arr2[it_]:
                return False
            it_+=1
        arr11=sorted(dict1.values())
        arr22=sorted(dict2.values())
        it_=0   
        while it_<len(arr11):
            if arr11[it_]!=arr22[it_]:
                return False
            it_+=1
        return True
if __name__=="__main__":
    word1=str(input('Type a value here for word1'))
    word2=str(input('Type a value here for word2'))
    sol=Solution()
    result=sol.closeStrings(word1=word1,word2=word2)
    print(f"The result is: {result}")