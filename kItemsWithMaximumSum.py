def kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k):
  sum = 0
  if k <= numOnes:
    sum += k
    return sum

  sum += numOnes
  k -= numOnes

  if k <= numZeros:
    return sum

  k -= numZeros
  sum -= k

  return sum

numOnes = 3
numZeros = 2
numNegOnes = 0
k = 2
max_sum = kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k)
print("Maximum possible sum:", max_sum)
