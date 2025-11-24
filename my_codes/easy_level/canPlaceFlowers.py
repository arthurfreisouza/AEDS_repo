class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        total_flowers = sum(flowerbed)
        L = len(flowerbed)

        # Case 1: No flowers
        if total_flowers == 0:
            sum_places = (L + 1) // 2

        # Case 2: One flower
        elif total_flowers == 1:
            it1 = flowerbed.index(1)
            sum_places = (it1 // 2) + ((L - it1 - 1) // 2)

        # Case 3: More than one flower
        else:
            indices = [i for i, x in enumerate(flowerbed) if x == 1]
            sum_places = 0

            # Left edge
            sum_places += indices[0] // 2

            # Between flowers
            for i in range(1, len(indices)):
                gap = indices[i] - indices[i-1] - 1
                if gap > 0:
                    sum_places += (gap - 1) // 2

            # Right edge
            sum_places += (L - 1 - indices[-1]) // 2

        return n <= sum_places

if __name__=="__main__":
    flowerbed=[]
    while True:
        flower_pos=int(input("Type here a flower: "))
        if flower_pos==400:
            break
        flowerbed.append(flower_pos)
    n=int(input("Type here a value for n: "))
    sol=Solution()
    result=sol.canPlaceFlowers(flowerbed=flowerbed,n=n)
    print(f"The result is: {result}")