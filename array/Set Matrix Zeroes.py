class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        lc=[]

        for i in range(len(matrix)):
          for j in range(len(matrix[i])):
            if matrix[i][j]==0:
              lc.append(j)
        for i in range(len(matrix)):
          if 0 in matrix[i]:
            for ii in range(len(matrix[i])):
              matrix[i][ii]=0
          else:
            for _ in lc:
              matrix[i][_]=0
        return matrix




        
