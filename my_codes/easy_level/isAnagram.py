class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1:

        # if len(s)!=len(t):
        #     return False
        # s=list(s)
        # t=list(t)
        # s.sort()
        # t.sort()
        # for i in range(len(s)):
        #     if s[i]!=t[i]:
        #         return False
        # return True

        # Solution 2:
        my_dict={}
        for i in range(len(s)):
            if s[i] not in my_dict:
                my_dict[s[i]]=1
            else:
                my_dict[s[i]]+=1

        for i in range(len(t)):
            if t[i] in my_dict:
                my_dict[t[i]]-=1
            else:
                return False
        breakpoint()
        for i in my_dict.values():
            if i!=0:
                return False
        return True

if __name__=="__main__":
    s=str(input("Type here a value for s"))
    t=str(input("Type here a value for t"))
    sol=Solution()
    result=sol.isAnagram(s=s,t=t)
    print(f"The result is: {result}")