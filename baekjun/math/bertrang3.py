import time

def get_prime(n):
    rn = int(n ** 0.5)
    for i in range(2, rn+1):
        if n % i == 0:
            return False
    return True

n = int(input())
start_time = time.time()

while n != 0:
    cnt = 0
    for i in range(n+1, 2*n+1):
        if get_prime(i) == True:
            cnt += 1
    print(cnt)
    print(f'--- {time.time() - start_time} --- seconds')
    n = int(input())
    start_time = time.time()
