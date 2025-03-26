import os
os.system('cls')
from concurrent.futures import ThreadPoolExecutor
import time

def work(n):
    time.sleep(1)
    print(f"Taks {n} completed")

# using thread pool
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(work,range(5))

print("all tasks completed")