import numpy as np
data = [0,1,2,3,6,5,5,6,4,3,2,1,2,3]
EARLY_STOPPING=3
stop_accuracy=[]

for total_correct in data:
    print(str(total_correct)+' ')
    stop_cnt=0
    stop_accuracy.append(total_correct)
    stop_max = np.argmax(stop_accuracy)
    stop_len = len(stop_accuracy)
    for i in range(stop_len-1,max(stop_max,stop_len-1-EARLY_STOPPING),-1):
        if stop_accuracy[i]<stop_accuracy[stop_max]:
            stop_cnt=stop_cnt+1
    if stop_cnt>=EARLY_STOPPING:
        break
#    print(stop_cnt)