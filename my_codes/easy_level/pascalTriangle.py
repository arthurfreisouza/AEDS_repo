class Solution:
    def generate(self, numRows: int):
        if numRows <= 0:
            raise ValueError("Invalid value, try again...")
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            list_1 = [[1], [1, 1]]
            for i in range(2, numRows):
                list_2 = [1]  # first element is always 1
                for j in range(1, i):
                    list_2.append(list_1[-1][j-1] + list_1[-1][j])
                list_2.append(1)  # last element is always 1
                list_1.append(list_2)
        return list_1

if __name__=="__main__":
    numRows=int(input("Type here an integer: "))
    sol=Solution()
    result=sol.generate(numRows=numRows)
    print(f"The result is: {result}")