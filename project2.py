#countdown
import time
time_ti = int(input("enter time"))
for i in range(1,time_ti):
    sec = i%60
    min =int(i//60)%60
    hour = i//3600
    print(f"{hour}:{min}:{sec}")
    time.sleep(1)
print("time up!")