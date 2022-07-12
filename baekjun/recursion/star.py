def create_star(n, star):
    if n == 3 or n == 6:
        return create_star(n-1, star) + star + '\n'
    elif n == 9:
        return create_star(n-1, star) + star
    elif n == 5:
        return create_star(n-1, star) + ' '
    elif n == 1:
        return star

    return create_star(n-1, star) + star


n = int(input())
temp = n
cnt = 0
n *= n
stars = ['*']

while temp != 1:
    temp //= 3
    cnt += 1

for i in range(cnt):
    stars.append(create_star(9, stars[i]))

print(stars)
#  print(stars[1])
