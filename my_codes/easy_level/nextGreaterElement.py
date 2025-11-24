class Solution:
    def nextGreaterElement(self, nums1,nums2):
        array_=[]
        for val in nums1:
            index=None
            for i in range(len(nums2)):
                if nums2[i]==val:
                    index=i
                    break
            if index!=None:
                has_greater=False
                for i in range(index+1,len(nums2)):
                    if nums2[i]>val:
                        has_greater=True
                        array_.append(nums2[i])
                        break
                if has_greater==False:
                    array_.append(-1)
        return array_
if __name__=="__main__":
    nums1=[]
    while True:
        num1=int(input("Type here 1 number:"))
        if num1==400:
            break
        nums1.append(num1)
    nums2=[]
    while True:
        num2=int(input("Type here 1 number:"))
        if num2==400:
            break
        nums2.append(num2)
    sol=Solution()
    result=sol.nextGreaterElement(nums1=nums1,nums2=nums2)
    print(f"The result is: {result}")