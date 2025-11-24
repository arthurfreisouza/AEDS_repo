class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        nums1=list(set(sorted(nums1)))
        nums2=list(set(sorted(nums2)))
        nums3=list(set(sorted(nums3)))
        dict_={}
        arr_=[]
        for i in range(len(nums1)):
            # breakpoint()
            dict_[nums1[i]]=True
        for i in range(len(nums2)):
            if nums2[i] not in dict_:
                dict_[nums2[i]]=True
            else:
                arr_.append(nums2[i])
        for i in range(len(nums3)):
            if nums3[i] not in dict_:
                dict_[nums3[i]]=True
            else:
                arr_.append(nums3[i])
        return list(set(arr_))
if __name__=="__main__":
    nums1=[]
    while True:
        num=int(input("Type here a num: "))
        if num==400:
            break
        nums1.append(num)
    nums2=[]
    while True:
        num=int(input("Type here a num: "))
        if num==400:
            break
        nums2.append(num)
    nums3=[]
    while True:
        num=int(input("Type here a num: "))
        if num==400:
            break
        nums3.append(num)
    sol=Solution()
    result=sol.twoOutOfThree(nums1=nums1,nums2=nums2,nums3=nums3)
    print(f"The solution is: {result}")