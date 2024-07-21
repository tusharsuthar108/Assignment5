def insert(intervals, newInterval):
  result = []
  i = 0
  n = len(intervals)

  while i < n and intervals[i][1] < newInterval[0]:
    result.append(intervals[i])
    i += 1
  merge_start = newInterval[0]
  merge_end = newInterval[1]
  while i < n and intervals[i][0] <= newInterval[1]:
    merge_start = min(merge_start, intervals[i][0])
    merge_end = max(merge_end, intervals[i][1])
    i += 1
  result.append([merge_start, merge_end])

  while i < n:
    result.append(intervals[i])
    i += 1

  return result

intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
result = insert(intervals, newInterval)
print(result)
