def primelist(number):
    if number < 2:
        return []
    numlist = list(range(2, number+1))
    primelist = []
    for i in range(2, number+1):
        if i in numlist:
            primelist.append(i)
        for x in range(i, number+1, i):
            if x in numlist:
                numlist.remove(x)
    return primelist