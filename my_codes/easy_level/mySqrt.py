class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left,right=1,x//2
        while left<=right:
            mid=(left+right)//2
            squared_=mid*mid
            if squared_==x:
                return mid
            elif squared_<x:
                left=mid+1
            else:
                right=mid-1
        return right

if __name__=="__main__":
    x=int(input("Type here an integer: "))
    sol=Solution()
    result=sol.mySqrt(x=x)
    print(f"The result is: {result}")