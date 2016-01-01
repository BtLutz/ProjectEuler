from numpy import mod, add, count_nonzero
from pdb import set_trace
def factors(n):    
    return set(reduce(list.__add__, 
                    ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

x = range(1,20)
#x = [11,13,14,16,17,18,19,20] 
def find_solution(step):
    for num in xrange(step, 999999999, step):
        if all(num % n == 0 for n in x):
            return num
    return None
    
# First attempt
def while_implementation(step):
    num = step 
    divisible = False 
    while not divisible:
        if not all(num % n == 0 for n in x):
            num += step 
        elif all(num % n == 0 for n in x):
            divisible = True
    return num

if __name__ == '__main__':
    solution = find_solution(2520)
    print "For loop: %s" % solution
    solution_2 = while_implementation(2520)
    print "While loop: %s" % solution_2

# Assemble list of prime #s under 20 (2,3,5,7,11,13,17,19)
# Then, do elementwise modulo for current number value
# e.g. 23 % [2 3 5 7 11 13 17 19]
# If the array is all zeros, the number is divisible by all values and should be returned.
