# class Solution:
#     def findAndReplacePattern(self, words, pattern: str):
#         # Mapping the words of 'pattern'
#         pattern_dict={}
#         for i in range(len(pattern)):
#             if pattern[i] not in pattern_dict:
#                 pattern_dict[pattern[i]]=1
#             else:
#                 pattern_dict[pattern[i]]+=1
#         result_list=[]
#         for i in range(len(words)):
#             mapped_words={}
#             j1,j2=0,0
#             while j1<len(words[i]) and j2<len(pattern):
#                 if words[i][j1] not in mapped_words:
#                     # breakpoint()
#                     # mapped_words[words[i][j1]]=pattern[j2]
#                     mapped_words[pattern[j2]]=words[i][j1]
#                 j1+=1
#                 j2+=1

#             for j in range(len(words[i])):
#                 if len(pattern)!=len(words[i]):
#                     break
#                 is_mapped=True
#                 if words[i][j]!=mapped_words[words[i][j]]:
#                     is_mapped=False
#                     break
#             if is_mapped==True:
#                 result_list.append(words[i])
#         return result_list
# if __name__=="__main__":
#     words=[]
#     while True:
#         word=str(input("Type here a value to add i the array of integers: "))
#         if word=='400':
#             break
#         words.append(word)
#     pattern=str(input("Type here a string to be used as a pattern: "))
#     sol=Solution()
#     result=sol.findAndReplacePattern(words=words,pattern=pattern)
#     print(f"The result is: {result}")

class Solution:
    def findAndReplacePattern(self, words, pattern: str):
        result_list = []

        for i in range(len(words)):
            if len(words[i]) != len(pattern):  # must be same length
                continue

            mapped_words = {}
            is_mapped = True

            # Build mapping pattern -> word
            for j in range(len(pattern)):
                if pattern[j] not in mapped_words:
                    mapped_words[pattern[j]] = words[i][j]
                else:
                    if mapped_words[pattern[j]] != words[i][j]:
                        is_mapped = False
                        break

            # Extra check: reverse mapping must also be unique
            if len(set(mapped_words.values())) != len(mapped_words.values()):
                is_mapped = False

            if is_mapped:
                result_list.append(words[i])

        return result_list


if __name__ == "__main__":
    words = []
    while True:
        word = str(input("Type here a value to add in the array of strings: "))
        if word == '400':
            break
        words.append(word)

    pattern = str(input("Type here a string to be used as a pattern: "))
    sol = Solution()
    result = sol.findAndReplacePattern(words=words, pattern=pattern)
    print(f"The result is: {result}")
