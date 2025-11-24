class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle=list(needle)
        size_window=len(needle)
        sliding_window=list(haystack)
        for i in range(size_window,len(haystack)+1):
            if needle==sliding_window[(i-size_window):i]:
                return i-size_window
        return -1
#         size_=len(needle)
#         for i in range(len(haystack)-size_+1):
#             if haystack[i:i+size_] == needle:
#                 return i
#         return -1


if __name__ == "__main__":
    haystack=str(input("Type here the haystack: "))
    needle=str(input("Type here the needle: "))
    sol=Solution()
    result=sol.strStr(haystack,needle)
    print(result)