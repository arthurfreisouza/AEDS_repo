from typing import List
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score,key=lambda item: item[k],reverse=True)

def main():
    score=[]
    k=int(input('Type here a value for k: '))
    sol=Solution()
    result=sol.sortTheStudents(score=score,k=k)
    print(f"The result is: {result}")

if __name__=="__main__":
    main()