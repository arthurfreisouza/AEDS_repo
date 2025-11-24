class Solution:
    def partitionString(self, s: str) -> int:
        s=list(s)
        arr_=[]
        counter=1
        for i in s:
            if i in arr_:
                arr_.clear()
                arr_.append(i)
                counter+=1
            else:
                arr_.append(i)
        return counter

def main():
    sol=Solution()
    s=str(input('Type here a string: '))
    result=sol.partitionString(s=s)
    print(f"The result is: {result}")
if __name__=="__main__":
    main()