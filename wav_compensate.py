import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt

Fs = 32000
f = open("./female.wav", "rb")
f.seek(0)
f.read(44)
x = np.fromfile(f, dtype = np.int16)
N = len(x)
freq = np.linspace(0,Fs,N+1)
df = freq[1]
y = fft(x,N)

data = np.loadtxt("coeff.txt")   #将文件中数据加载到data数组里
print(data.shape)