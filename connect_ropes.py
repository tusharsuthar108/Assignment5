import heapq

def min_cost_connect_ropes(arr):
  heapq.heapify(arr)
  total_cost = 0

  while len(arr) > 1:
    rope1 = heapq.heappop(arr)
    rope2 = heapq.heappop(arr)
    cost = rope1 + rope2
    total_cost += cost
    heapq.heappush(arr, cost)

  return total_cost

arr = [4, 3, 2, 6]
min_cost = min_cost_connect_ropes(arr)
print("Minimum cost to connect ropes:", min_cost)
