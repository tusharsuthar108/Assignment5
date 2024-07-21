def survival(S, N, M):
  if (N * 6) >= (M * 7):
    total_food_needed = S * M
    days_to_buy_food = (total_food_needed + N - 1) // N
    return days_to_buy_food
  else:
    return -1

S = 10
N = 16
M = 2
result = survival(S, N, M)
if result != -1:
  print("Minimum days to buy food:", result)
else:
  print("It's not possible to survive.")
