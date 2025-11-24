from typing import List
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        if not groupSizes:
            return []
        # Just taking the reight indexes.
        my_dict={} # O(n) 0(n)
        for index,value in enumerate(groupSizes):
            if value not in my_dict:
                my_dict[value]=[index]
            else:
                my_dict[value].append(index)
        # breakpoint()
        # Splitting my array correctly.
        return_arr=[]
        for index,values in my_dict.items():
            if len(values)>index:
                arr_aux=[]
                for j in range(len(values)):
                    arr_aux.append(values[j])
                    if (j+1)%index==0:
                        return_arr.append(arr_aux)
                        arr_aux=[]
            else:
                return_arr.append(values)

        return return_arr



def main():
    groupSizes=[]
    while True:
        num=int(input('Type here a num: '))
        if num==400:
            break
        groupSizes.append(num)
    sol=Solution()
    result=sol.groupThePeople(groupSizes=groupSizes)
    print(f"The result is: {result}")

if __name__=="__main__":
    main()