class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]

def main():
    a=str(input('Type here the value for a: '))
    b=str(input('Type here the value for b: '))
    sol=Solution()
    result=sol.addBinary(a=a,b=b)
    print(f"The result is: {result}")
if __name__=="__main__":
    main()