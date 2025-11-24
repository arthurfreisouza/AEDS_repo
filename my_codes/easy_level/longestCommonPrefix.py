class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix=strs[0]
        for i in range(1,len(strs)):
            while not strs[i].startswith(prefix):
                prefix=prefix[:-1]
        if len(prefix)==0:
            return ""
        return prefix
if __name__=="__main__":
    strs_=[]
    while True:
        str_=str(input("Type here a string: "))
        if str_=='400':
            break
        strs_.append(str_)
    sol=Solution()
    result=sol.longestCommonPrefix(strs=strs_)
    print(f"The result is: {result}")