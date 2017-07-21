#该函数检查输入数组accuracy的最后EARLY_STOPPING个数：
#若它们均小于accuracy中的最大值，则eraly stop，返回1
#否则，不early stop，返回0
import numpy as np

def early_stopping(accuracy,EARLY_STOPPING):
        stop_cnt=0
        stop_max = np.argmax(accuracy)
        stop_len = len(accuracy)
        for i in range(stop_len-1,max(stop_max,stop_len-1-EARLY_STOPPING),-1):
            if accuracy[i]<accuracy[stop_max]:
                stop_cnt=stop_cnt+1
        if stop_cnt>=EARLY_STOPPING:
            return 1
        else:
            return 0