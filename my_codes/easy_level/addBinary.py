class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Mapping the list as integers and obtaining its int values.
        lst_integers_a=list(map(int,a))
        lst_integers_b=list(map(int,b))
        total_sum=0
        for index, value in enumerate(reversed(lst_integers_a)):
            total_sum+=value*2**index
        for index, value in enumerate(reversed(lst_integers_b)):
            total_sum+=value*2**index
        if total_sum == 0:
            return "0"
        if total_sum == 1:
            return "1"


        aux_var=None
        i=0
        while 2**i < total_sum:
            if 2**(i+1) > total_sum:
                aux_var=i
                break
            elif 2**(i+1) == total_sum:
                aux_var=i+1
            i+=1
        result = []
        #breakpoint()
        while aux_var > -1:
            if total_sum // 2**aux_var > 0:
                result.append(str(1))
                total_sum-=2**aux_var
            else:
                result.append(str(0))
            aux_var-=1
        result = "".join(result)
        print(f"The result is {result}")

        
        
def test_numbers(a, b):
    for i in a:
        if i!='0' and i!='1':
            raise Exception("Wrong numbers.")
    for i in b:
        if i!='0' and i!='1':
            raise Exception("Wrong numbers.")

if __name__ == "__main__":
    a=str(input("Digit the first number: "))
    b=str(input("Digit the second number: "))
    test_numbers(a,b)
    sol=Solution()
    sol.addBinary(a,b)
