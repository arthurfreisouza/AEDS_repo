class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_window = 0
        start = 0
        counter = 0  # number of zeros in current window

        for end in range(len(nums)):
            if nums[end] == 0:
                counter += 1

            while counter > k:
                if nums[start] == 0:
                    counter -= 1
                start += 1  # shrink window

            max_window = max(max_window, end - start + 1)

        return max_window

if __name__=="__main__":
    nums=[]
    while True:
        num=int(input("Type here a value to num: "))
        if num==400:
            break
        nums.append(num)
    k=int(input("Type here a value to k: "))
    sol=Solution()
    result=sol.longestOnes(nums=nums,k=k)
    print(f"The result is: {result}")