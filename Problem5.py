from numpy import mod, add, count_nonzero

primes = range(1,11)
num = 1
divisible = False 
while not divisible:
    if count_nonzero(mod(num, primes)) != 0:
        print "%s is not! got to %s" % (num, mod(num,primes))
        num += 1
    elif count_nonzero(mod(num, primes)) == 0:
        print num
        divisible = True

# Assemble list of prime #s under 20 (2,3,5,7,11,13,17,19)
# Then, do elementwise modulo for current number value
# e.g. 23 % [2 3 5 7 11 13 17 19]
# If the array is all zeros, the number is divisible by all values and should be returned.
