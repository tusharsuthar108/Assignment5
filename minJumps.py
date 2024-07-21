def minJumps(seats):
  occupied_positions = [i for i, seat in enumerate(seats) if seat == 'x']
  n = len(occupied_positions)
  if n == 0:
    return 0

  median_position = occupied_positions[n // 2]
  total_jumps = 0

  for i in range(n):
    target_position = median_position - (n // 2) + i
    total_jumps += abs(occupied_positions[i] - target_position)

  return total_jumps

seats = "....x..xx...x.."
result = minJumps(seats)
print(result)
