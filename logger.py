from datetime import datetime

def log(job_name, status):
    with open("job_log.txt", "a") as f:
        f.write(f"{datetime.now()} - {job_name}: {status}\n")
