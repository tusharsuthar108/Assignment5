def merge(intervals):
  if not intervals:
    return []

  intervals.sort(key=lambda x: x[0])
  merged_intervals = [intervals[0]]

  for i in range(1, len(intervals)):
    current_interval = intervals[i]
    previous_interval = merged_intervals[-1]

    if current_interval[0] <= previous_interval[1]:
      previous_interval[1] = max(previous_interval[1], current_interval[1])
    else:
      merged_intervals.append(current_interval)

  return merged_intervals

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merged_intervals = merge(intervals)
print(merged_intervals)
