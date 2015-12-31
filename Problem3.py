import pdb
import math
num = 600851475143 
primeFactors = []
for i in range(2, int(math.sqrt(num))):
    print i
    prime = True
    for j in range(2,i/2):
        if i % j == 0:
            prime = False
            break 
    if prime == True:
        if num % i == 0:
            num = num / i
            primeFactors.append(i)
            print primeFactors
print primeFactors
