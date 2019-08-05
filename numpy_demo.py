import numpy as np

data = np.cos(np.arange(20)).reshape(5,4)
print(data)
print(np.argmax(data,axis=0))
print(np.argsort(data,axis=0))
print(np.sort(data,axis=0))
