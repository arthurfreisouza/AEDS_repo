class Solution:
    def firstUniqChar(self, s: str) -> int:
        s = list(s)
        left = 0
        
        while left < len(s): # Staring and iterating until the end
            is_unique = True
            i = 0
            while i < len(s): # Iterating ove the entire loop   
                if i != left and s[i] == s[left]:
                    is_unique = False
                    break
                i += 1
            if is_unique:
                return left
            left += 1
        return -1


if __name__=="__main__":
    s=str(input("Type here your input: "))
    sol=Solution()
    result=sol.firstUniqChar(s=s)
    print(f"The result is: {result}")