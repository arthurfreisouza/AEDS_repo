class Solution:
    def findWords(self, words):
        rows_mapped=["qwertyuiop","asdfghjkl","zxcvbnm"] # Mapping my words correctly
        lst_return=[]
        for index,value in enumerate(words):# Iterating over each word of my array.
            # breakpoint()
            for map_ in rows_mapped: # Iterating over each row of my keyboard.
                aux=True
                for i in range(len(value)):
                    if value[i].lower() not in map_:
                        aux=False
                        break
                if aux:
                    lst_return.append(words[index])
        return lst_return
            
if __name__=="__main__":
    words=[]
    s=str(input("Type here a string to check if it's within a unique keyboard's row: "))
    while s!='False':
        words.append(s)
        s=str(input("Type here the string to check if it's a palindrome: "))
    sol=Solution()
    result=sol.findWords(words=words)
    print(f"The result is: {result}")