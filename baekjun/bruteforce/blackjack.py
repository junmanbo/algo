def get_blackjack(N, M, cards):
    maxtotal = 0
    for i in range(0, N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                total = cards[i]+cards[j]+cards[k]
                if total < M:
                    if total > maxtotal:
                        maxtotal = total
                elif total == M:
                    return total
    return maxtotal


N, M = map(int, input().split())
cards = list(map(int, input().split()))

totals = []


print(get_blackjack(N, M, cards))
