n = int(input())
cards = list(map(int, input().split()))
if n & 1:
    cards.append(0)
cards.sort(reverse = True)
print(sum(cards[i] - cards[i + 1] for i in range(0, n, 2)))