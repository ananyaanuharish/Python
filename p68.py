# Thread Communication using queue.Queue
import queue
import time
import threading
import os
os.system('cls')

q = queue.Queue()

def producer():
    for i in range(5):
        time.sleep(2)
        q.put(i)
        print(f"Produced: {i}")

def consumer():
    while not q.empty():
        item = q.get()
        print(f"Consumed : {item}")
        q.task_done()

# creaing threads
p1 = threading.Thread(target=producer)
c1 = threading.Thread(target=consumer)

p1.start()
p1.join()

c1.start()
c1.join()