# https://leetcode.com/problems/set-matrix-zeroes/
# BY: Hiwot Beyene
# 4th year software engineering student
# Addis Ababa Institute Of Technology~
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False
        
        #determine which rows/cols need to be zero
        for r in range(rows):
          for c in range(cols):
            if matrix[r][c] == 0:
              matrix[0][c] = 0
              if r>0:
                matrix[r][0] = 0
              else:
                rowZero = True
                
      # let's us change what needs to be zero
        for r in range(1,rows):
          for c in range(1,cols):
            if matrix[0][c] ==0 or matrix[r][0] ==0:
              matrix[r][c] = 0
              
        if matrix[0][0] == 0:
          for r in range(rows):
            matrix[r][0] = 0
            
        if rowZero:
          for c in range(cols):
            matrix[0][c] = 0
            
        return matrix
            
            
      
      
              
        