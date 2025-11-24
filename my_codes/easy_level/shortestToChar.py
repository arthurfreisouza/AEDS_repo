class Solution:
    def shortestToChar(self, s: str, c: str):
        n = len(s)
        # result array initialized large; will store distances
        res = [0] * n

        # Left to right: distance from the most recent c on the left
        prev = -10**9  # a very small number so positions before first c become large
        for i in range(n):
            if s[i] == c:
                prev = i
            res[i] = i - prev

        # Right to left: distance to the next c on the right; take min with left pass
        prev = 10**9  # a very large number so positions after last c become large
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            # choose the nearest of left-seen and right-seen distances
            res[i] = min(res[i], prev - i)

        return res

if __name__=="__main__":
    s=str(input("Type here your string: "))
    c=str(input("Type here your character: "))
    sol=Solution()
    result=sol.shortestToChar(s=s,c=c)
    print(f"The result is: {result}")