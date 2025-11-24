class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[:]=sorted(nums1[:m]+nums2[:n])
        nums1=[int(x) for x in nums1]
        diff=(m+n)-len(nums1)
        if diff>0:
            for i in range(len(nums1)-1, len(nums1)-1+diff):
                nums1.append(0)
        return nums1

if __name__=="__main__":
    nums1=str(input("Type a value nums1: ")).strip("[]").split(",")
    nums=list(map(int,nums1))
    m=int(input("Type a value for m: "))
    nums2=str(input("Type a value nums2: ")).strip("[]").split(",")
    nums=list(map(int,nums2))
    n=int(input("Type a value for n: "))
    sol=Solution()
    result=sol.merge(nums1,m,nums2,n)
    print(result)