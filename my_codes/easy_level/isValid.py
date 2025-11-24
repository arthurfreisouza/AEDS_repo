class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict_={"(": ")",
               "[": "]",
               "{": "}"}
        if len(s)==1:
            return False
        list_=[]
        # breakpoint()
        for value in s:
            if value=="(" or value=="[" or value=="{":
                list_.append(value)
            else:
                if len(list_)>0:
                    if value!=dict_[list_[(len(list_)-1)]]:
                        return False
                    else:
                        list_.pop()
                else:
                    list_.append(value)
        return len(list_)<1

        
if __name__=="__main__":
    str_=str(input("Type here a string: "))
    print(f"Your string is: {str_}")
    sol=Solution()
    result=sol.isValid(str_)
    print(f"The result is: {result}")