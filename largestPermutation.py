def largestPermutation(arr, k):
  n = len(arr)
  index_map = {v: i for i, v in enumerate(arr)}

  for i in range(n):
    if k == 0:
      break
    if arr[i] != n - i:
      largest_index = index_map[n - i]
      arr[i], arr[largest_index] = arr[largest_index], arr[i]
      index_map[arr[i]] = i
      index_map[arr[largest_index]] = largest_index
      k -= 1

  return arr

arr = [4, 2, 3, 5, 1]
k = 3
result = largestPermutation(arr, k)
print(result)
