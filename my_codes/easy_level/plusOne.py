class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        arr_ = int("".join(map(str, digits)))
        arr_+=1
        arr_=str(arr_)
        result=[]
        for i in arr_:
            result.append(int(i))
        return result

def creating_number() -> list:
    try:
        value_=str(input("Type a number: "))
        list_values=[]
        for x in value_:
            list_values.append(int(x))
    except Exception as error:
        print(f"The error is happening.... {error}")
    return list_values


if __name__ == "__main__":
    digits=creating_number()
    sol = Solution()
    result=sol.plusOne(digits=digits)
    print(f"The result is: {result}")