from math import sqrt

def check_sum(a,b,c):
    return a + b + c == 1000

def check_triplet(a,b,c):
    return a**2 + b**2 == c**2

def find_triplets():
    for a in range(3, 999):
        for b in range(4, 999):
            if (a**2 + b**2) % 1 == 0:
                c = sqrt(a**2 + b**2)
                if check_sum(a,b,c):
                    return [a,b,c]
                else:
                    continue

def find_product(a,b,c):
    return a * b * c

if __name__ == "__main__":
    a, b, c = find_triplets()  
    print find_product(a,b,c) 
