class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        return grid[0][1]*grid[0][0]
if __name__=="__main__":
    s1=Solution
    print(s1.onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]]))
