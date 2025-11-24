class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s==" ":
            return True
        bool_=True
        for i in range(len(s) // 2):
            if s[i] != s[(len(s)- 1) - i]:
                bool_=False
                break
        return bool_
        
def pre_process(phrase: str):
    processed_phrase = "".join(char for char in phrase if char.isalnum())
    return processed_phrase.lower()
if __name__=="__main__":
    sol=Solution()
    phrase=str(input("Type here a phrase: "))
    processed_phrase=pre_process(phrase=phrase)
    result=sol.isPalindrome(processed_phrase)
    print(f"The phrase is: {processed_phrase} and is palindrome: {result}")
