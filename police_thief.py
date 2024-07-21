def police_thief(arr, k):
  police = []
  thief = []
  caught = 0

  for i in range(len(arr)):
    if arr[i] == 'P':
      police.append(i)
    elif arr[i] == 'T':
      thief.append(i)

  i = 0
  j = 0

  while i < len(police) and j < len(thief):
    if abs(police[i] - thief[j]) <= k:
      caught += 1
      i += 1
      j += 1
    elif police[i] < thief[j]:
      i += 1
    else:
      j += 1

  return caught

arr = ['P', 'T', 'T', 'P', 'T']
k = 2
result = police_thief(arr, k)
print("Maximum thieves caught:", result)
