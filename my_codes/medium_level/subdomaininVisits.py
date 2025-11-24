from typing import List
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        solution_={}
        for value in cpdomains:
            splitted_val=value.split(' ') # Splitting into count and domain
            domain=splitted_val[1]
            count=int(splitted_val[0])
            arr_=[]
            for it_ in domain.split('.')[::-1]:
                arr_.append(it_)
                joined_arr='.'.join(arr_[::-1])
                if joined_arr not in solution_:
                    solution_[joined_arr]=int(count)
                else:
                    solution_[joined_arr]+=int(count)

        # Formatting the solution.
        arr_solution=[]
        for domain,count in solution_.items():
            arr_solution.append(f'{count} {domain}')

        return arr_solution
def main():
    cpdomains=["9001 discuss.leetcode.com"]
    # while True:
    #     num=int(input('Type here a num: '))
    #     if num==400:
    #         break
        # cpdomains.append(num)
    sol=Solution()
    result=sol.subdomainVisits(cpdomains=cpdomains)
    print(f"The result is: {result}")

if __name__=="__main__":
    main()