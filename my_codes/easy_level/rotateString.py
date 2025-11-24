class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s=list(s)
        arr_=[]
        for i in range(len(s)):
            arr_.append("".join(s))
            a=s[0]
            s=s[1:]
            s.append(a)
        if goal in arr_:
            return True
        return False
if __name__=="__main__":
    s=str(input("Type here a value for the string s: "))
    goal=str(input("Type here a value for the string goal: "))
    sol=Solution()
    result=sol.rotateString(s=s,goal=goal)
    print(f"The result is: {result}")