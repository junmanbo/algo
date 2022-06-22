def get_prime(n, prime_numbers):
    for i in prime_numbers:
        if n % i == 0:
            return False
    prime_numbers.append(n)
    return True


n = int(input())
prime_numbers = []
while n != 0:
    cnt = 0
    for i in range(n+1, 2*n+1):
        if get_prime(i, prime_numbers) == True:
            cnt += 1
    print(cnt)
    n = int(input())
