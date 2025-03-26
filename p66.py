# daemon thread
import threading
import time
import os
os.system('cls')
def background_daemon_thread():
    while True:
        print("Running backrgound task...")
        time.sleep(2)

# Creating demon thread
daemon_thread = threading.Thread(target=background_daemon_thread, daemon=True)

time.sleep(5)
print("Main thread completed")