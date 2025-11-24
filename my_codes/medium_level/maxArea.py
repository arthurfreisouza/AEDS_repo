class Solution:
    def maxArea(self, height) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            max_area = max((right - left) * min(height[left], height[right]), max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == "__main__":
    heights = []
    while True:
        num = int(input("Type an int to add in the array (400 to stop): "))
        if num == 400:
            break
        heights.append(num)

    sol = Solution()
    result = sol.maxArea(heights)
    print(f"The result (maxArea) is: {result}")
