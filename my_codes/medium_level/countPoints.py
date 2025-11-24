from typing import List
import math
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        arr_result=[]
        for query in queries:
            couter_points=0
            x_centre=query[0]
            y_centre=query[1]
            radius=query[2]
            for point in points:
                p_x=point[0]
                p_y=point[1]
                distance=math.sqrt((p_x-x_centre)**2 + (p_y-y_centre)**2)
                if distance<=radius:
                    couter_points+=1
            arr_result.append(couter_points)
        return arr_result


def main():
    points=[[1,1],[2,2],[3,3],[4,4],[5,5]]
    queries=[[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
    sol=Solution()
    result=sol.countPoints(points=points,queries=queries)
    print(f"The result is: {result}")

if __name__=="__main__":
    main()