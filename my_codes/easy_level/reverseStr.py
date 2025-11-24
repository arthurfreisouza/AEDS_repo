class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        count=0
        while count < k:
            if count*2*k>=len(s):
                raise ValueError("The index is out of range.")
            if (count+1)//(2*k)==0:
                pointer_i,pointer_j=0,k-1
                while pointer_i<=pointer_j:
                    s[pointer_i], s[pointer_j] = s[pointer_j], s[pointer_i]
                    pointer_i+=1
                    pointer_j-=1
                count+=1
        remained_numbers=len(s)-count*2*k
        if k < remained_numbers:
            pointer_i,pointer_j=remained_numbers,len(s)-1
            while pointer_i<=pointer_j:
                s[pointer_i], s[pointer_j] = s[pointer_j], s[pointer_i]
                pointer_i+=1
                pointer_j-=1
        elif k<=remained_numbers<2*k:
            pointer_i,pointer_j=remained_numbers, remained_numbers+k
            while pointer_i<=pointer_j:
                s[pointer_i], s[pointer_j] = s[pointer_j], s[pointer_i]
                pointer_i+=1
                pointer_j-=1
        return s
        
if __name__=="__main__":
    s=str(input("Type here your string: "))
    sol=Solution()
    # sol.reverseStr(s=s,k=2)
    result=sol.reverseStr(s=s,k=2)
    print(f"The output is: {result}")