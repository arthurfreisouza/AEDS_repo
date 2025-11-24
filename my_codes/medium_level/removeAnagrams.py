from collections import Counter
from typing import List
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        arr_=[]
        for word in words:
            if not arr_:
                arr_.append(word)
            else:
                if Counter(word)!=Counter(arr_[-1]):
                    arr_.append(word)
        return arr_
if __name__=="__main__":
    words=[]
    while True:
        word=str(input("Type here a word: "))
        if word=='400':
            break
        words.append(word)
    sol=Solution()
    result=sol.removeAnagrams(words=words)
    print(f"The result is: {result}")