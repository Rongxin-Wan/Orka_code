# wav_joint: combine 2 WAV files to the first WAV file
# wav_joint_infile: combine all WAV files to a new file output.wav

from posix import listdir
import wave
import os
import random


def wav_joint(file1, file2):
  data= []
  f1 = wave.open(file1, 'rb')
  data.append( [f1.getparams(), f1.readframes(f1.getnframes())] )
  f1.close()
  f2 = wave.open(file2, 'rb')
  data.append( [f2.getparams(), f2.readframes(f2.getnframes())] )
  f2.close()
  out = wave.open(file1, 'wb')
  out.setparams(data[0][0])
  out.writeframes(data[0][1])
  out.writeframes(data[1][1])
  out.close()

def wav_joint_infile(FILE_PATH, ifshuffle=False):
  files = os.listdir(FILE_PATH)
  if (ifshuffle):
    random.shuffle(files)
  os.system("cp "+FILE_PATH+"/"+files.pop(0)+" "+FILE_PATH+"/output.wav")
  data = []
  f1 = wave.open(FILE_PATH+"/output.wav", 'rb')
  data.append( [f1.getparams(), f1.readframes(f1.getnframes())] )
  count = 0
  f1.close()
  print("Reading start")
  for file in files:
    w = wave.open(FILE_PATH+"/"+file, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()
    count += 1
  print("Synthesis start")
  out = wave.open(FILE_PATH+"/output.wav", 'wb')
  out.setparams(data[0][0])
  for i in range(count):
    out.writeframes(data[i][1])
  out.close()

# wav_joint testing
# file1 = "/mnt/d/Code_review/Voice_data/DNS_noisy_gener/clean_10h1_300mVpeak.wav"
# file2 = "/mnt/d/Code_review/Voice_data/DNS_noisy_gener/clean_10h2_300mVpeak.wav"
# wav_joint(file1, file2)

# wav_joint_infile testing
FILE_PATH = "/mnt/d/Code_review/Voice_data/DNS_noisy_gener/generated_noise_32k_new"
wav_joint_infile(FILE_PATH)
