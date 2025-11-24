from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict_mapping={2: 'abc',
                      3: 'def',
                      4: 'ghi',
                      5: 'jkl',
                      6: 'mno',
                      7: 'pqrs',
                      8: 'tuv',
                      9: 'wxyz'}
        
def main():
    digits=str(input('Type here the digits'))
    sol=Solution()
    result=sol.letterCombinations(digits=digits)
    print(f"The result is: {result}")

if __name__=="__main__":
    main()