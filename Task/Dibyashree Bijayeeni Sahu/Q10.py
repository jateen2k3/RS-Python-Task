import cv2 as cv
import numpy as np

def transmatrix(matrix):
    matrix1=np.array(matrix)
    transposedmatrix= cv.transpose(matrix1)
    transposedmatrix=transposedmatrix.tolist()
    print('transposed matrix:',transposedmatrix)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
l= print(transmatrix(matrix))
