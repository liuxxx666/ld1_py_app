from threading import Timer
import time

count = 0
def print_counter():
    global t, count
    count += 1
    print("count: " + str(count))
    
    if count < 10:
        t = Timer(1, print_counter)
        t.start()

t = Timer(1, print_counter)
t.start()
time.sleep(5)
t.cancel()