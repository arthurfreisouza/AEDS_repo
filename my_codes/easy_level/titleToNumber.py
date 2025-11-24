class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        columnTitle=columnTitle.lower()
        letters=['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']
        dict_={}
        for index, value in enumerate(letters,start=1):
            dict_[value]=index
        if len(columnTitle) == 1:
            result=dict_[columnTitle]
        else:
            result=0
            for index, value in enumerate(reversed(columnTitle)):
                result+=(26**index)*dict_[value]
        return result

if __name__=="__main__":
    sol=Solution()
    result=sol.titleToNumber("ZY")
    print(result)