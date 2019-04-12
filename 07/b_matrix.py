#!/usr/bin/env python3
"""
Matrix
"""



class Matrix():
    """
    Class representing matrix
    """
    def __init__(self,values):
        self._values = values
        
    
    def __getitem__(self,i):
        return self._values[i]
        
    
    def __add__(self, other):
        suma = []
        for i in range(len(self._values)):
            row = []
            for j in range(len(self._values[0])):
                row.append(self[i][j]+other[i][j])
            suma.append(row)
        return Matrix(suma)


    def mult(self, other):
        suma = []
        for i in range(len(self._values)):
            row = []
            for j in range(len(self._values[0])):
                hodnota = 0
                for k in range(len(self._values)):
                    hodnota+=self[i][k]*other[k][j]
                row.append(hodnota)
            suma.append(row)
        return Matrix(suma)



    def __repr__(self):
        return self._values.__repr__()


        
if __name__ == "__main__":
    m1 = Matrix([[1,2],[3,2]])
    m2 = Matrix([[1,1],[1,1]])
    print(m1+m2)
    print(m1.mult(m2))
