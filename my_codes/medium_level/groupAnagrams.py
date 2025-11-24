class Solution:
    def groupAnagrams(self, strs:list):
        my_dict={}
        for value in strs:
            sorted_value=tuple(sorted(value))
            if sorted_value not in my_dict:
                my_dict[sorted_value]=[value]
            else:
                my_dict[sorted_value].append(value)
        return list(my_dict.values())
if __name__=="__main__":
    strs=["eat","tea","tan","ate","nat","bat"]
    # while True:
    #     str_=str(input("Type here a sentence: "))
    #     if str_=="400":
    #         break
    #     strs.append(str_)
    sol=Solution()
    result=sol.groupAnagrams(strs=strs)
    print(f"The result is: {result}")   