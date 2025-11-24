class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            raise ValueError("Wrong value")
        elif numRows==1:
            return [[1]]
        elif numRows==2:
            pass
        arr_1=[[1],[1,1]]
        for i in range(2,numRows):
            arr_2=[1]
            aux=arr_1[-1]
            for j in range(len(aux)-1):
                arr_2.append(aux[j]+aux[j+1])
            arr_2.append(aux[-1])
            arr_1.append(arr_2)
        return arr_1


if __name__=="__main__":
    numRows=int(input("Type here numRows: "))
    sol=Solution()
    result=sol.generate(numRows=numRows)
    print(f"The result is {result}")