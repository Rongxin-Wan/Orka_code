# combine 2 PCM files to 1 output.cpm

import array

def pcm_joint(file1, file2, file3, channel=1, bits=16):
  f = open(file1, 'rb')
  data = f.read()
  print(type(data))
  f.close()
  f = open(file2, 'rb')
  data2 = f.read()
  f.close()