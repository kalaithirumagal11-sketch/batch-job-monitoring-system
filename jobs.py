import random
import time

def job1():
    time.sleep(1)
    return "SUCCESS"

def job2():
    time.sleep(1)
    return random.choice(["SUCCESS", "FAILED"])

def job3():
    time.sleep(1)
    return "SUCCESS"
