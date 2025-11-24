class Solution:
    def reorderLogFiles(self, logs):
        arr_letters=[]
        arr_digits=[]
        for i in logs:
            if i[:3]=='let':
                arr_letters.append(i)
            else:
                arr_digits.append(i)
        left,right=0,len(arr_letters)-1
        while left<right:
            left_arr=arr_letters[left].strip()
            identifier1=left_arr[0]
            right_arr=arr_letters[right].strip()
            identifier2=left_arr[0]
            it1=1
            is_equal=True
            while it1<len(left_arr) and it1<len(right_arr):
                if left_arr[it1]>right_arr[it1]:
                    is_equal=False
                    arr_letters[left],arr_letters[right]=arr_letters[right],arr_letters[left] # Replacing them.
                    break
            if is_equal:
                if identifier1>identifier2:
                    arr_letters[left],arr_letters[right]=arr_letters[right],arr_letters[left] # Replacing them.
            left+=1
            right-=1
        left,right=0,len(arr_digits)-1
        while left<right:
            if arr_digits[left][:3]>arr_digits[right][:3]:
                arr_digits[left],arr_digits[right]=arr_digits[right],arr_digits[left] # Replacing them.
        return arr_letters+arr_digits

if __name__=="__main__":
    logs=["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    sol=Solution()
    result=sol.reorderLogFiles(logs=logs)
    print(f"The result is: {logs}")