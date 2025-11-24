class Solution:
    def compress(self, chars) -> int:
        position=0
        start=0
        while start<len(chars):
            count=0
            char=chars[start]
            while start<len(chars) and chars[start]==char:
                start+=1
                count+=1
            chars[position]=char
            position+=1
            if count>1:
                for digit in str(count):
                    chars[position]=digit
                    position+=1

        while len(chars)>position:
            chars.pop()
if __name__=="__main__":
    chars=[]
    while True:
        char=str(input("Type here a char: "))
        if char=='400':
            break
        chars.append(char)
    sol=Solution()
    result=sol.compress(chars=chars)
    print(f"The result is: {result}")