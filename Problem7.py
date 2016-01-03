from pdb import set_trace

def factors(n):
    return set(reduce(list.__add__,
                        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
def find_prime_number(k):
    primes = []
    num = 3
    i = 0
    while i < k-1:
       if factors(num) == set([1,num]):
            primes.append(num)
            i += 1
       num += 2
    return primes[-1]

if __name__ == "__main__":
    print find_prime_number(10)

