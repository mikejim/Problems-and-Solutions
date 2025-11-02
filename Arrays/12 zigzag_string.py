class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        else:
            counter = 0
            act = prev = 0
            strLen = len(s)
            # Create a 2D array filled with zeros
            matrix = [['-' for _ in range(strLen)] for _ in range(numRows)]
            r = len(matrix)
            c = len(matrix[0]) # Assumes matrix_2d is not empty
            print(r, c)
            col = 0
            salida = ""
            for c in s:
                #print(counter, act, col)#, matrix[act][col])
                matrix[act][col] = c 
                prevAct = act
                if act == numRows-1:
                    act, col = act-1, col+1
                elif act == 0:
                    act+=1
                elif act < numRows and prev < act:
                    act+=1
                elif act < numRows and prev > act:
                    act, col = act-1, col+1
                prev = prevAct
                counter+=1
            for x in range(0,len(matrix)):
                row = matrix[x]
                for y in row:
                    if y <> '-': salida+=y
            #print(salida)
            return salida

