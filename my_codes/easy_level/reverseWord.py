class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(' ') # Breaking in words
        if len(s)<1:
            raise Exception("Value error.")
        arr_=[]
        for i in s:#Iterating over each word.
            aux_lst=list(i) # Transforming in a list.
            pointer_i,pointer_j=0,len(aux_lst)-1
            while pointer_i<=pointer_j:
                aux_lst[pointer_i], aux_lst[pointer_j] = aux_lst[pointer_j], aux_lst[pointer_i]
                pointer_i+=1
                pointer_j-=1
            s="".join(aux_lst) # Merging the words
            arr_.append(s)
        s=" ".join(arr_)# Merging the phrase
        return s
        

if __name__=="__main__":
    s=str(input("Type here your string: "))
    sol=Solution()
    sol.reverseWords(s=s)
    result=sol.reverseWords(s=s)
    print(f"The output is: {result}")