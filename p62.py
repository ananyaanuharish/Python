import threading

counter=0
lock=threading.Lock()

def increment():
    global counter
    for _ in range(3):
        with lock:
            counter+=1

# creating threads
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
print("final Counter:", counter)