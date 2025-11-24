class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1 or n==7:
            return True
        if len(str(n))==1:
            return False
        lst_=[]
        while n!=1:
            for i in str(n):
                lst_.append(int(i))
            n=sum([x**2 for x in lst_])
            if n==1 or n==7:
                return True
            if len(str(n))==1:
                return False
            lst_.clear()
        
if __name__=="__main__":
    n=int(input("Type here an integer: "))
    sol=Solution()
    result=sol.isHappy(n=n)
    print(f"The result is: {result}")