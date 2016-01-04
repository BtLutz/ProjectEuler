from pdb import set_trace

def sum_of_squares(k):
    num = 0
    for i in range(1,k+1):
        num += i*i
    return num

def square_of_sum(k):
    num = 0
    for i in range(1,k+1):
        num += i
    return num*num

if __name__ == "__main__":
   first = sum_of_squares(100)
   second = square_of_sum(100)
   print second - first
