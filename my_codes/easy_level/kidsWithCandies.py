class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        max_value=0
        for i in candies:
            if i>max_value:
                max_value=i
        arr_bool=[]
        for i in candies:
            if i+extraCandies>=max_value:
                arr_bool.append(True)
            else:
                arr_bool.append(False)        
        return arr_bool
if __name__=="__main__":
    candies=[]
    while True:
        candie=int(input("Type here the number of candies:"))
        if candie==400:
            break
        candies.append(candie)
    extraCandies=int(input("Type here a value for extra candies: "))
    sol=Solution()
    result=sol.kidsWithCandies(candies=candies,extraCandies=extraCandies)
    print(f"The result is: {result}")