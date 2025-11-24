class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        len_s = len(s)
        
        first_group = len_s % k
        aux_ = []
        breakpoint()
        
        if first_group > 0:
            aux_.append(s[:first_group])

        for i in range(first_group, len_s, k):
            if aux_:
                aux_.append('-')
            aux_.append(s[i:i+k])
        
        return "".join(aux_)
if __name__=="__main__":
    s=str(input("Type here a value to s: "))
    k=int(input("Type here a value to k: "))
    sol=Solution()
    result=sol.licenseKeyFormatting(s=s,k=k) 
    print(f"The result is: {result}")