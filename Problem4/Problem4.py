palindromes = []

for i in range(999,100, -1):
    for j in range(999,100,-1):
        num = i * j
        tempI = str(num)
        reverseI = tempI[::-1]
        if tempI == reverseI:
            print "%s * %s = %s" % (i, j, num)
            palindromes.append(num)

print max(palindromes)

