# Script used for WAV file conbination

import numpy as np
import os
import wave
import random

def wav2data(wavfile, data_type=np.int16):
  f = wave.open(wavfile, "rb")
  nframes = f.getnframes()
  data = f.readframes(nframes)
  f.close()
  return data

def data2wav(data, wav_file, channels=1, bits=16, sample_rate=32000):
  f = wave.open(wav_file, 'wb')
  f.setnchannels(channels)
  f.setsampwidth(bits // 8)
  f.setframerate(sample_rate)
  f.writeframes(data)
  f.close()

if __name__ == '__main__':

  WAV_DIR_CLEAN = "D:/Orka_code/clean"
  WAV_DIR_NOISY = "D:/Orka_code/noisy"
  WAV_FILE_OUT_CLEAN = "D:/Orka_code/output/clean.wav"
  WAV_FILE_OUT_NOISY = "D:/Orka_code/output/noisy.wav"

  wavfile_clean = os.listdir(WAV_DIR_CLEAN)
  data_clean = bytes()
  data_noisy = bytes()
  count = 0
  random.shuffle(wavfile_clean)
  print("合并的文件数")
  for file in wavfile_clean:
    tmp_clean = wav2data(WAV_DIR_CLEAN+"/"+file)
    tmp_noisy = wav2data(WAV_DIR_NOISY+"/"+file)
    data_clean = data_clean + tmp_clean
    data_noisy = data_noisy + tmp_noisy
    print(count)
    count += 1
  data2wav(data_clean, WAV_FILE_OUT_CLEAN, 1, 16, 32000)
  data2wav(data_noisy, WAV_FILE_OUT_NOISY)