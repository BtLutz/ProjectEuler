import pdb
import math
num = 600851475143 
primeFactors = []
k = 2

while num > 1:
    if num % k == 0:
        print k
        while num % k == 0:
            num = num / k
    k += 1

# First version
for i in range(2, int(math.sqrt(num))):
    print i
    prime = True
    for j in range(2,i/2):
        if i % j == 0:
            prime = False
            break 
    if prime == True:
        if num % i == 0:
            primeFactors.append(i)
            print primeFactors
print primeFactors
