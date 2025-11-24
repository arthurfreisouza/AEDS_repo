class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left,right=0,len(letters)-1
        if letters[0]==target:
            for i in range(len(letters)):
                if letters[i]!=target:
                    return letters[i]
        while left<=right:
            mid=(left+right)//2
            if letters[mid]<=target:
                left=mid+1
            else:
                right=mid-1
        breakpoint()
        return letters[left] if left < len(letters) else letters[0]

if __name__=="__main__":
    letters=["x","x","y","y"]
    target=str(input("Type here a value: "))
    sol=Solution()
    result=sol.nextGreatestLetter(letters=letters,target=target)
    print(f"The result is: {result}")