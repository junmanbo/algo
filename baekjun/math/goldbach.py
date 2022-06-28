def get_prime(n):
    sn = int(n ** 0.5)
    for i in range(2, sn+1):
        if n % i == 0:
            return False
    return True


T = int(input())  # the number of test cases
for i in range(T):
    n = int(input())
    a, b = 0, 0
    for j in range(2, n//2+1):
        if get_prime(j) == True:
            diff = n - j
            if get_prime(diff) == True:
                a, b = j, diff

    print(a, b)
