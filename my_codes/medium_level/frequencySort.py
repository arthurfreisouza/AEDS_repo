class Solution:
    def frequencySort(self, s: str) -> str:
        # Just savig the words and their frequency in the dict,
        dict_frequency={}
        for letter in s:
            # breakpoint()
            if letter not in dict_frequency:
                dict_frequency[letter]=1
            else:
                dict_frequency[letter]+=1

        # Sorting everything and creating the word.
        word_=[]
        sorted_by_value_desc = sorted(dict_frequency.items(), key=lambda item: item[1], reverse=True)
        for letter,count in sorted_by_value_desc:
            while count>0:
                word_.append(letter)
                count-=1
        return ''.join(word_)
my_dict = {'apple': 3, 'banana': 1, 'orange': 2}
sorted_by_value_desc = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
print(sorted_by_value_desc)
# Output: [('apple', 3), ('orange', 2), ('banana', 1)]
def main():
    s=str(input('Type here a string: '))
    sol=Solution()
    result=sol.frequencySort(s=s)
    print(f"The result is: {result}")
if __name__=="__main__":
    main()