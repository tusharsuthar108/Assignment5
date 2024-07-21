def disjointIntervals(intervals):
  intervals.sort(key=lambda x: x[0])

  result = []
  current_interval = intervals[0]
  for next_interval in intervals[1:]:
    if current_interval[1] < next_interval[0]:
      result.append(current_interval)
      current_interval = next_interval
    else:
      current_interval = [current_interval[0], max(current_interval[1], next_interval[1])]

  result.append(current_interval)
  return result

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
disjoint_intervals = disjointIntervals(intervals)
print(disjoint_intervals)
