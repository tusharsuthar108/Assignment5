def find_min_platforms(arrival, departure):
  arrival.sort()
  departure.sort()

  platforms_needed = 0
  max_platforms = 0
  i = 0
  j = 0

  while i < len(arrival) and j < len(departure):
    if arrival[i] <= departure[j]:
      platforms_needed += 1
      i += 1
    elif arrival[i] > departure[j]:
      platforms_needed -= 1
      j += 1

    max_platforms = max(max_platforms, platforms_needed)

  return max_platforms

arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
min_platforms = find_min_platforms(arrival, departure)
print("Minimum platforms required:", min_platforms)
