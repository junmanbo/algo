import time

def get_prime(n, prime_numbers):
    rn = n ** 0.5
    for i in prime_numbers:
        if i > rn:
            return True
        elif n % i == 0:
            return False
    return True

n = int(input())
start_time = time.time()

prime_numbers = [2]

while n != 0:
    cnt = 0
    last_num = prime_numbers[-1]

    if n > last_num:
        for i in range(last_num, n+1):
            if get_prime(i, prime_numbers) == True:
                prime_numbers.append(i)

    # n부터 2n까지 구할 때 소수로 나눠주고 소수를 찾으면 리스트에 저장
    for i in range(n+1, 2*n+1):
        if get_prime(i, prime_numbers) == True:
            cnt += 1
            prime_numbers.append(i)
    print(cnt)
    print(f'--- {time.time() - start_time} --- seconds')
    n = int(input())
    start_time = time.time()
