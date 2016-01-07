from numpy import matrix
from numpy import ndarray
from numpy import loadtxt
from pdb import set_trace

def product_right(m):
    # returns product matrix cascading to right
    # i.e. 2,3,4 becomes 6,12,1
    product = ndarray([len(m), len(m[0])])
    product = ndarray([len(matrix), len(matrix[0])])

    for i in range(0,len(m)-1):
        for j in range(0,len(m[i])-1):
            product[i][j] = m[i][j] * m[i][j+1]
    product[len(m)-1] = 1
    return product

def product_left(m):
    # returns product matrix cascading to left
    # i.e. 2,3,4 becomes 1,6,12
    return None
def product_up(m):
    # returns product matrix cascading upw one row
    # i.e. 2,3,4 becomes 10,18,21 
    #      5,6,7         40,54, 7
    #      8,9,1          1, 1, 1
    return None
def product_down(m):
    # returns product matrix cascading down one row
    return None
def product_downright(m):
    # returns product matrix cascading down one row and to right
    return None
def product_downleft(m):
    # returns product matrix cascading down one row and to left
    return None
def product_upright(m):
    # returns product matrix cascading up one row and to right
    return None
def product_upleft(m):
    # returns product matrx cascading up one row and to left
    return None
def find_max_value(m):
    # returns a scalar value c
    return None
def produce_final_matrix(a,b,c,d,e,f,g,h):
    return None
if __name__ == "__main__":
    # matrix_raw = open("matrix.txt").read()

    # matrix_raw = matrix_raw.replace('\n', '; ')
    # matrix_raw = matrix_raw.replace(' 0', ' ')
    # matrix_clean = matrix_raw.replace('08', '8')
    # print matrix_clean 
    # matrix = matrix(matrix_clean)
    
    ## Maybe this will work instead?
    matrix = loadtxt('matrix.txt') # Yeah, it does.

    up = product_up(matrix)
    up_right = product_upright(matrix)
    right = product_right(matrix)
    down_right = product_downright(matrix)
    down = product_down(matrix)
    down_left = product_downleft(matrix)
    left = product_downleft(matrix)
    up_left = product_upleft(matrix)
    set_trace()
    final_product = up * up_right * right * down_right * down * down_left * left * up_left

# find all sums of matrix. Multiply sums together to find the final product matrix. Search this matrix to find the maximum value. 
