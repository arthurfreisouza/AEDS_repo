class Solution:
    def getRow(self, rowIndex: int):
        if rowIndex <= 0:
            raise ValueError("Invalid value, try again...")
        elif rowIndex == 1:
            return [[1]]
        elif rowIndex == 2:
            return [[1], [1, 1]]
        else:
            list_1 = [[1], [1, 1]]
            for i in range(2, rowIndex+1):
                list_2 = [1]
                for j in range(1, i):
                    list_2.append(list_1[-1][j-1] + list_1[-1][j])
                list_2.append(1)
                list_1.append(list_2)
                if i==rowIndex:
                    return list_2
        return None

if __name__=="__main__":
    rowIndex=int(input("Type here an integer: "))
    sol=Solution()
    result=sol.getRow(rowIndex=rowIndex)
    print(f"The result is: {result}")