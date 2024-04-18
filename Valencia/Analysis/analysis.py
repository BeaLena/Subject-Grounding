import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import time
import os

temperature = 293
lnaGain = 45
bw = 50*1e3 # Hz
johnson = np.sqrt(2 * 50 * temperature * bw * 1.38e-23) * 10 ** (lnaGain / 20) * 1e6  # uV
print('\nExpected by Johnson: %0.5f uV\n' % johnson)

pwd = os.path.abspath(os.path.dirname(__file__))
dataPath = os.path.join(pwd, '..', 'Data')
for rawName in os.listdir(dataPath):
    if 'Noise' not in rawName:
        continue
    path = os.path.join(dataPath, rawName)
    rawData = sio.loadmat(path)
    data = rawData['data']
    noiserms = np.std(data)*1e3 # uV
    print(rawName.split('_')[0])
    print('rms noise: %0.5f uV\n' % noiserms)
