class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Just converting the patterns to individual words/letters.
        s=s.split()
        set_pattern = sorted(list(set(pattern)), key=pattern.index)
        set_s = sorted(list(set(s)), key=s.index)
        if len(set_pattern)!=len(set_s):
            return False

        # Mapping the patterns:
        dict_patterns={}
        counter=0
        for i in set_pattern:
            dict_patterns[i]=set_s[counter]
            counter+=1
        breakpoint()
        # Checking if they are unique
        counter=0
        for letter in pattern:
            if dict_patterns[letter]!=s[counter]:
                print(dict_patterns[letter],s[counter])
                breakpoint()
                return False
            counter+=1

        return True
def main():
    pattern=str(input('Type here a pattern: '))
    s=str(input('Type here a s: '))
    sol=Solution()
    result=sol.wordPattern(pattern=pattern,s=s)
    print(f"The result is: {result}")
if __name__=="__main__":
    main()