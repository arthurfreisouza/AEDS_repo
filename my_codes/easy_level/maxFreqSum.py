class Solution:
    def maxFreqSum(self, s: str) -> int:
        # my_dict={}
        # for i in range(len(s)):
        #     if s[i] not in my_dict:
        #         my_dict[s[i]]=1
        #     else:
        #         my_dict[s[i]]+=1
        # vowels='aeiou'
        # consonants='bcdfghjklmnpqrstvwxyz'
        # max_vowels=0
        # max_consonants=0
        # for index,value in my_dict.items():
        #     # breakpoint()
        #     if index in vowels and value > max_vowels:
        #         max_vowels=value
        #     elif index in consonants and value > max_consonants:
        #         max_consonants=value
        # return max_consonants+max_vowels
        vowels='aeiou'
        consonants='bcdfghjklmnpqrstvwxyz'
        my_dict_vowels={}
        my_dict_consonants={}
        for i in range(len(s)):
            if s[i] in vowels and s[i] not in my_dict_vowels:
                my_dict_vowels[s[i]]=1
            elif s[i] in vowels and s[i] in my_dict_vowels:
                my_dict_vowels[s[i]]+=1
            if s[i] in consonants and s[i] not in my_dict_consonants:
                my_dict_consonants[s[i]]=1
            elif s[i] in consonants and s[i] in my_dict_consonants:
                my_dict_consonants[s[i]]+=1
        max_vowel=0
        max_consonant=0
        for value in my_dict_vowels.values():
            if value>max_vowel:
                max_vowel=value
        for value in my_dict_consonants.values():
            if value>max_consonant:
                max_consonant=value
        return max_consonant+max_vowel
if __name__=="__main__":
    s=str(input("Type here a string: "))
    sol=Solution()
    result=sol.maxFreqSum(s=s)
    print(f"The result is: {result}")