def min_diff_chocolate(arr, m):
  if m == 0 or len(arr) == 0:
    return 0

  arr.sort()
  n = len(arr)

  if n < m:
    return -1

  min_diff = float('inf')

  for i in range(n - m + 1):
    diff = arr[i + m - 1] - arr[i]
    min_diff = min(min_diff, diff)

  return min_diff

arr = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5
result = min_diff_chocolate(arr, m)
print("Minimum difference is:", result)
