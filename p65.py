import os
os.system('cls')
import threading
import time
def print_numbers():
    for i in range(1,11):
        time.sleep(1)
        print(f"Numbers: {i}")

def print_letters():
    for letters in "Hello World":
        time.sleep(1)
        print(f"Letter: {letters}")

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t1.join()

t2.start()
t2.join()