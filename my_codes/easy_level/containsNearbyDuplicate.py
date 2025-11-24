class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        # for i in range(len(nums)-1):
        #     for j in range(1,len(nums)):
        #         if nums[i]==nums[j] and abs(i-j)<=k and i!=j:
        #             return True
        # return False
        set_=set()
        for end in range(len(nums)):
            if nums[end] in set_:
                return True
            set_.add(nums[end])
            if len(set_)>k:
                set_.remove(nums[end-k])
        return False

if __name__=="__main__":
    nums=[0,1,2,3,2,5]
    k=int(input("Type here a value to k: "))
    sol=Solution()
    result=sol.containsNearbyDuplicate(nums=nums,k=k)
    print(f"The result is: {result}")