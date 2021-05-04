import numpy as np
import matplotlib.pyplot as plt
import os, sys

p = r'C:\Users\Admin\Home\dev\python\DeepSPM\dev\stm-data\JointDataset\Train\good'
f1 = r'00003_Default.npy'
f2 = r'00003_Ransac.npy'

f2 = os.path.join(p, f2)
f1 = os.path.join(p, f1)

d1 = np.load(f1)
d2 = np.load(f2)

print(np.max(d1))
print(np.max(d2))

plt.subplot(121), plt.imshow(d1)
plt.subplot(122), plt.imshow(d2)
plt.show()


