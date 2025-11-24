from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # for index,value in enumerate(intervals):
        #     intervals[index]=sorted(value)
        breakpoint()
        intervals.sort(key=lambda x: x[0]) # Sorting our list of elements based in the first index.
        arr_=[intervals[0]]
        for i in intervals[1:]:
            if arr_[-1][1]>= i[0]:
                arr_[-1][1]=max(arr_[-1][1], i[1])
            else:
                arr_.append(i)
        return arr_

def main():
    intervals=[]
    while True:
        interval1=int(input('Type here the values for i1: '))
        interval2=int(input('Type here the values for i2: '))
        if interval1==400 and interval2==400:
            break
        intervals.append([interval1,interval2])
    sol=Solution()
    result=sol.merge(intervals=intervals)
    print(f"The result is: {result}")
if __name__=="__main__":
    main()