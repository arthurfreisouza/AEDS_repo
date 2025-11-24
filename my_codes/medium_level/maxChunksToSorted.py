from typing import List 

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # if not arr:
        #     return False
        # arr_sum=[0]*len(arr)
        # arr_sum[0]=arr[0]
        # values_=[(i*(i+1)/2) for i in range(len(arr))]
        # for index in range(1,len(arr)):
        #     arr_sum[index]=arr[index]+arr_sum[index-1]
        # counter=0
        # for i in range(len(arr_sum)):
        #     if arr_sum[i]==values_[i]:
        #         counter+=1
        # return counter
        stack=[]
        for num in arr:
            if not stack or num>=stack[-1]: # Always get the maximum of each chunk
                stack.append(num)
            else:
                max_val=stack.pop()
                while stack and stack[-1]>num:
                    stack.pop()
                stack.append(max_val)
        return len(stack)

if __name__=="__main__":
    arr=[]
    while True:
        val=int(input('Type here a value: '))
        if val==400:
            break
        arr.append(val)
    sol=Solution()
    result=sol.maxChunksToSorted(arr=arr)