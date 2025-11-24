class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title=title.lower().split(" ")
        for i in range(len(title)):
            if len(title[i])<=2:
                continue
            else:
                title[i]=list(title[i])
                title[i][0]=title[i][0].upper()
                title[i]="".join(title[i])
        return " ".join(title)
if __name__=="__main__":
    title=str(input("Type here a value for the title: "))
    sol=Solution()
    result=sol.capitalizeTitle(title=title)
    print(f"The result is: {result}")