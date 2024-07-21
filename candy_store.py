def candy_store(prices, N, K):
  prices.sort()
  min_cost = 0
  max_cost = 0
  i = 0
  j = N - 1

  while i <= j:
    min_cost += prices[i]
    i += 1
    j -= K

  i = 0
  j = N - 1

  while i <= j:
    max_cost += prices[j]
    j -= 1
    i += K

  return min_cost, max_cost

prices = [3, 2, 1, 4]
N = len(prices)
K = 2
min_cost, max_cost = candy_store(prices, N, K)
print("Minimum cost to buy all candies:", min_cost)
print("Maximum cost to buy all candies:", max_cost)
