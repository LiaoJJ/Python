import numpy as np
from early_stopping import *
data = [0,1,2,3,6,5,5,6,4,3,2,4,7,3]

print('stopping:'+str(early_stopping(data,3)))
