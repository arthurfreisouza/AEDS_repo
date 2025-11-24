class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")  # handle uppercase too
        s = list(s)  # convert string to list for easy swapping
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] not in vowels:
                i += 1
                continue
            if s[j] not in vowels:
                j -= 1
                continue
            # Swap vowels
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        return "".join(s)


if __name__ == "__main__":
    s = str(input("Type here a string s: "))
    sol = Solution()
    result = sol.reverseVowels(s)
    print(f"The result is: {result}")
