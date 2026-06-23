class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lef = 0
        rig = (len(matrix) * len(matrix[0])) - 1

        while lef <= rig:
            mid = (lef+rig) // 2

            row = mid % len(matrix[0])
            col= mid // len(matrix[0])

            if (matrix[col][row]<target):
                lef = mid + 1
            elif (matrix[col][row]>target):
                rig =  mid - 1
            else:
                return True
        
        return False
