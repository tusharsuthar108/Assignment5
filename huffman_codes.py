def huffman_codes(S, f):
  n = len(S)
  heap = [[f[i], S[i]] for i in range(n)]
  heapq.heapify(heap)

  codes = {}

  while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)

    for char in left[1]:
      codes[char] = '0' + (codes.get(char, ''))
    for char in right[1]:
      codes[char] = '1' + (codes.get(char, ''))

    heapq.heappush(heap, [left[0] + right[0], left[1] + right[1]])
  def print_codes(code, prefix):
    if len(code) == 1:
      print(code[0], prefix)
    else:
      print_codes(code[:len(code)//2], prefix + '0')
      print_codes(code[len(code)//2:], prefix + '1')

  root = heapq.heappop(heap)[1]
  print_codes(root, '')

S = ['a', 'b', 'c', 'd', 'e', 'f']
f = [5, 9, 12, 13, 16, 45]
huffman_codes(S, f)
