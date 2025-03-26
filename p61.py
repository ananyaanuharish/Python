# Multiple thread

import threading
import time

def task(name):
    print(f"thread {name} starting")
    time.sleep(5)
    print(f"thread {name} finished")

threads = []
for i in range(5):
    t = threading.Thread(target=task, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads completed")
