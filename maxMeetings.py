def maxMeetings(start, end):

  n = len(start)
  meetings = [(start[i], end[i], i) for i in range(n)]

  meetings.sort(key=lambda x: x[1])  # Sort by end times

  count = 1
  prev_end = meetings[0][1]

  for i in range(1, n):
    if meetings[i][0] > prev_end:
      count += 1
      prev_end = meetings[i][1]

  return count

start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
max_meetings = maxMeetings(start, end)
print("Maximum meetings:", max_meetings)
