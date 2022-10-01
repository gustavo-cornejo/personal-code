import numpy as np

## Common notation: 
## this source will be used following the next definitions:

## Given a matrix A, we will represent the number of rows by m, and the number of columns by n.
##

def forward_elimination(A,F):
    m,n = A.shape
    B = A.copy()
    f = F.copy()
    for col in range(n):
        u_col = 1/B[col,col]
        for row in range(col+1,m):
          u_row = u_col * B[row,col]
          B[row,:] -= u_row * B[col,:]
          f[row] -= u_row * f[col]
        f[col] = f[col]/B[col,col]
        B[col,col] = 1
    return B,f

def backward_elimination(A,F):
    m,n = A.shape
    B = A.copy()
    f = F.copy()
    for col in range(n-1,-1,-1):
        u_col = 1/B[col,col]
        for row in range(0,col):
          u_row = u_col * B[row,col]
          print(u_row)
          B[row,:] -= u_row * B[col,:]
          f[row] -= u_row * f[col]
        f[col] = f[col]/B[col,col]
        B[col,col] = 1
    return B,f