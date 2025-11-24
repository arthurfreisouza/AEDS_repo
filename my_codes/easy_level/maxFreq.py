class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        char_set=set()
        start=0
        max_length=0
        for end in range(len(s)):
            while s[end] in char_set or len(char_set) > maxLetters:
                char_set.remove(s[start])
                start+=1
        char_set.add(s[end])
        max_length=max(max_length,end-start+1)
        if minSize < max_length < maxSize:
            return max_length
if __name__=="__main__":
    str_=str(input("Type here your string: "))
    maxLetters=int(input("Type here the maximum of letters: "))
    minSize=int(input("Type here the minimum size: "))
    maxSize=int(input("Type here the maximum size: "))
    sol=Solution()
    result=sol.maxFreq(str_,maxLetters,minSize,maxSize)
    print(f"The result is: {result}")