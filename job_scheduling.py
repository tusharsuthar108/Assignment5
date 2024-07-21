def job_scheduling(jobs):
  jobs.sort(key=lambda x: x[1])

  max_deadline = max(jobs, key=lambda x: x[1])[1]
  schedule = [-1] * (max_deadline + 1)
  num_jobs = 0
  total_profit = 0

  for job_id, deadline, profit in jobs:
    for i in range(deadline, 0, -1):
      if schedule[i] == -1:
        schedule[i] = job_id
        num_jobs += 1
        total_profit += profit
        break

  return num_jobs, total_profit

jobs = [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]
num_jobs, total_profit = job_scheduling(jobs)
print("Number of jobs done:", num_jobs)
print("Maximum profit:", total_profit)
