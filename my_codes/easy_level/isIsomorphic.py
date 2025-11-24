class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict_1={}
        dict_2={}
        for i in range(len(s)):
            # For the first dict:
            if s[i] not in dict_1:
                dict_1[s[i]]=t[i]
            else:
                if dict_1[s[i]]!=t[i]:
                    return False
            # For the second dict:
            if t[i] not in dict_2:
                dict_2[t[i]]=s[i]
            else:
                if dict_2[t[i]]!=s[i]:
                    return False
        return True
if __name__=="__main__":
    s=str(input("Type here your string: "))
    t=str(input("Type here your string: "))
    sol=Solution()
    result=sol.isIsomorphic(s=s,t=t)
    print(f"The result is: {result}")