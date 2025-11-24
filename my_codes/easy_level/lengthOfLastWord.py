class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.split(" ")
        for i in reversed(s):
            if i!="":
                return len(i)
        

if __name__ == "__main__":
    s=str(input("Type the value of the string s: "))
    sol=Solution()
    result=sol.lengthOfLastWord(s)
    print(result)