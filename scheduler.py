from jobs import job1, job2, job3
from logger import log

job_status = {}

print("Running job1...")
result1 = job1()
log("job1", result1)
job_status["job1"] = result1

if result1 == "SUCCESS":
    print("Running job2...")
    result2 = job2()
    log("job2", result2)
    job_status["job2"] = result2
else:
    print("job2 skipped")
    job_status["job2"] = "SKIPPED"

if job_status["job2"] == "SUCCESS":
    print("Running job3...")
    result3 = job3()
    log("job3", result3)
    job_status["job3"] = result3
else:
    print("job3 skipped")
    job_status["job3"] = "SKIPPED"

print("\nFinal Status:")
for job, status in job_status.items():
    print(job, "→", status)
