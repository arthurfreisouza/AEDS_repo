class Solution:
    def getEncryptedString(s: str, k: int) -> str:
        n = len(s)
        res = [''] * n
        for i in range(n):
            res[(i+k) % n] = s[i]
        return ''.join(res)

if __name__=="__main__":
    s=str(input("Type here a string: "))
    k=int(input("Type here a value for k: "))
    sol=Solution()
    result=sol.getEncryptedString(s=s,k=k)
    print(f"The result is: {result}")