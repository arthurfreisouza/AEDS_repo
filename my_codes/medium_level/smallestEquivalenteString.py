class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        arr_=[]
        for i in range(len(s1)):
            exists=False
            for j in arr_:
                if s1[i] in j or s2[i] in j or baseStr[i] in j:
                    exists=True
                    j.append(s1[i])
                    j.append(s2[i])
                    j.append(baseStr[i])
                    break
            if exists==False:
                aux=[s1[i],s1[i],baseStr[i]]
                arr_.append(aux)
        result=[]
        for i in arr_:
            i=list(set(i))
            i.sort()
        for i in range(len(s1)):
            for j in arr_:
                if s1[i] in j:
                    result.append(j[0])
        return result
            
if __name__=="__main__":
    s1=str(input("Type here the first string: "))
    s2=str(input("Type here the second string: "))
    baseStr=str(input("Type here the baseStr string: "))
    sol=Solution()
    result=sol.smallestEquivalentString(s1=s1,s2=s2,baseStr=baseStr)
    print(f"The result is: {result}")

