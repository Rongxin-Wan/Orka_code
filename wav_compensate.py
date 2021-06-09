# wav_compensate: mutiple a Gain to .wav file and rewrite original file
# wav_compensate_infile: mutiple a Gain to .wav file in a directory and rewrite

import numpy as np
from scipy.io import wavfile
import os

def wav_compensate(file, gain):
  sample_rate, data = wavfile.read(file)
  # print(data[0])
  # print(type(data[0]))
  data = data * gain
  data = np.array(data, dtype=np.int16)
  # print(data[0])
  # print(type(data[0]))
  wavfile.write(file, sample_rate, data)

def wav_compensate_infile(FILE_PATH, gain):
  files = os.listdir(FILE_PATH)
  count = 0
  for file in files:
    wav_compensate(FILE_PATH+"/"+file, gain)
    count += 1
    print(count)

path = "/mnt/d/Code_review/Voice_data/DNS_noisy_gener/generated_noise_32k_new"
wav_compensate_infile(path,0.5)
# file = "/mnt/d/Code_review/Voice_data/DNS_noisy_gener/generated_noise_32k/aaa.wav"
# wav_compensate(file, 0.5)