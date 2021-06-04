# combine 2 WAV files to 1 output.wav

import wave

def wav_joint(file1, file2, out_file):
  data= []
  w = wave.open(file1, 'rb')
  data.append( [w.getparams(), w.readframes(w.getnframes())] )
  w.close()
  w = wave.open(file2, 'rb')
  data.append( [w.getparams(), w.readframes(w.getnframes())] )
  w.close()
  output = wave.open(out_file, 'wb')
  output.setparams(data[0][0])
  output.writeframes(data[0][1])
  output.writeframes(data[1][1])
  output.close()