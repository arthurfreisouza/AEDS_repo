import itertools

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permutations_=[''.join(p) for p in itertools.permutations(s1)]
        for end in range(len(s2)):
            for i in permutations_:
                if i in s1[:end]:
                    return True
        return False
if __name__=="__main__":
    s1=str(input("Type here a value for the first string: "))
    s2=str(input("Type here a value for the second string: "))
    sol=Solution()
    result=sol.checkInclusion(s1=s1,s2=s2)
    print(f"The result is: {result}")