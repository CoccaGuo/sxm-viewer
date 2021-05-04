import numpy as np
import os
from sklearn.linear_model import RANSACRegressor, LinearRegression

ransac = RANSACRegressor(LinearRegression(),
                        max_trials=1000,
                        residual_threshold=5e-12)

path = r'C:\Users\Admin\Home\dev\python\DeepSPM\dev\stm-data\JointDataset\Train\good'
file = '00001_Default.npy'
data = np.load(os.path.join(path, file))
ransac.fit(data)