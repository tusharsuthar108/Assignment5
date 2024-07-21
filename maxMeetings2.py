def maxMeetings(S, F):
  n = len(S)
  meetings = [(S[i], F[i], i + 1) for i in range(n)]

  meetings.sort(key=lambda x: x[1])

  result = []
  result.append(meetings[0][2])
  prev_end = meetings[0][1]

  for i in range(1, n):
    if meetings[i][0] > prev_end:
      result.append(meetings[i][2])
      prev_end = meetings[i][1]

  return result

S = [1, 3, 0, 5, 8, 5]
F = [2, 4, 6, 7, 9, 9]
result = maxMeetings(S, F)
print("The order of meetings is:", result)
