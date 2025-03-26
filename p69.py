import threading
import time
import os
os.system('cls')

def download_file():
    print(f"Download is starting..")
    time.sleep(1)
    print(f"Download is being completed")

def processing_data():
    print(f"the data is processing")
    time.sleep(1)
    print(f"Data Processing is being completed")

def saving_result():
    print(f"saving the result")
    time.sleep(1)
    print("Results are being saved")

d1 = threading.Thread(target=download_file)
p1 = threading.Thread(target=processing_data)
s1 = threading.Thread(target=saving_result)

d1.start()
d1.join()

p1.start()
p1.join()

s1.start()
s1.join()