def calculate_avg_waiting_time(bt):
  n = len(bt)
  bt_sorted = sorted(enumerate(bt), key=lambda x: x[1])

  waiting_time = [0] * n
  waiting_time[bt_sorted[0][0]] = 0

  for i in range(1, n):
    idx = bt_sorted[i][0]
    waiting_time[idx] = waiting_time[bt_sorted[i-1][0]] + bt_sorted[i-1][1]

  total_waiting_time = sum(waiting_time)
  avg_waiting_time = total_waiting_time // n

  return avg_waiting_time

bt = [5, 3, 8, 2, 1]
avg_waiting_time = calculate_avg_waiting_time(bt)
print("Average waiting time:", avg_waiting_time)
