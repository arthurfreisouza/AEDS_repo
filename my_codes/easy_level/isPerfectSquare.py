class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left,right=0,num
        while left<=right:
            mid=(left+right)//2
            if mid**2==num:
                return True
            if mid**2<num:
                left=mid+1
            else:
                right=mid-1
        return False

if __name__=="__main__":
    num=int(input("Type here a number n: "))
    sol=Solution()
    result=sol.isPerfectSquare(num)
    print(f"The result is: {result}")