def prastevila(n):
    count = 0
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            count += 1
    return count