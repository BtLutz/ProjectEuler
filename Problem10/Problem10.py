from sys import argv

# def factors(n):
    # # Deprecated
    # return set(reduce(list.__add__,
                            # ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


# def is_prime(x):
    # # Deprecated
   # return factors(x) == set([1, x])
   
def find_primes_to(k):
    
    prime_set = set()
    for i in range(2, k+1):
        if i not in prime_set:
            yield i
            prime_set.update(range(i**2, k+1, i))
    

    ##### First Attempt #####
    #sum = 2
    #for i in range(3,k,+2):
    #   print i
    #   if is_prime(i):
    #       sum += i
    #return sum

if __name__ == "__main__":
    print sum(list(find_primes_to(int(argv[1]))))

