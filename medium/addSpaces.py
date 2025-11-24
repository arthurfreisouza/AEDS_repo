from typing import List
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        if not s or not spaces:
            return None
        s=list(s)
        size_s=len(s)
        for i in range(size_s):
            if i in spaces:
                print(f'We are insetir space in the positions {i}, before is: {s[i-1]} and after: {s[i+1]}')
                s.insert(i,' ')
        return ''.join(s)


def main():
    s=str(input('Type here a string: '))
    spaces=[8,13,15]
    sol=Solution()
    result=sol.addSpaces(s=s,spaces=spaces)
    print(f"The result is: {result}")

if __name__=="__main__":
    main()

