class Solution:
    def sumCounts(self, nums) -> int:
        total_sum = 0
        n = len(nums)
        breakpoint()
        for i in range(n):
            distinct_elements = set()
            
            for j in range(i, n):
                
                distinct_elements.add(nums[j])
                
                distinct_count = len(distinct_elements)
                
                total_sum += distinct_count ** 2
                
        return total_sum

if __name__ == "__main__":
    nums = []
    while True:
        num = int(input("Type here an array (400 to stop): "))
        if num == 400:
            break
        nums.append(num)

    sol = Solution()
    result = sol.sumCounts(nums=nums)
    print(f"The result is: {result}")
