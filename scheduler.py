from jobs import job1, job2, job3
from logger import log

jobs = [job1, job2, job3]
job_status = {}

for job in jobs:
    print(f"Running {job.__name__}...")

    result = job()
    log(job.__name__, result)

    retries = 0
    while result == "FAILED" and retries < 2:
        print(f"{job.__name__} failed. Restarting...")
        result = job()
        log(job.__name__, result)
        retries += 1

    job_status[job.__name__] = result

print("\nFinal Status:")
for job, status in job_status.items():
    print(f"{job} → {status}")
