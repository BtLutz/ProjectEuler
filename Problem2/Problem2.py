sum = 2
firstTerm = 1
secondTerm = 2
thirdTerm = 0

while thirdTerm < 4000000:
    thirdTerm = firstTerm + secondTerm
    firstTerm = secondTerm
    print "%s | %s | %s " % (firstTerm,secondTerm,thirdTerm)
    secondTerm = thirdTerm
    if thirdTerm % 2 == 0:
        sum += thirdTerm

print sum
