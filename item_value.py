class Item:
  def __init__(self, value, weight):
    self.value = value
    self.weight = weight

def fractional_knapsack(w, arr):
  arr.sort(key=lambda x: (x.value / x.weight), reverse=True)

  total_value = 0.0
  current_weight = 0

  for item in arr:
    if current_weight + item.weight <= w:
      total_value += item.value
      current_weight += item.weight
    else:
      remaining_weight = w - current_weight
      total_value += (item.value / item.weight) * remaining_weight
      break

  return total_value

w = 50
arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
max_value = fractional_knapsack(w, arr)
print("Maximum value in knapsack:", max_value)
