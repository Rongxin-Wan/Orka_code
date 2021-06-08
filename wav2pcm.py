import numpy as np
import os
import wave

def wav2pcm(wavfile, pcmfile, data_type=np.int16):
    f = open(wavfile, "rb")
    f.seek(0)
    f.read(44)
    data = np.fromfile(f, dtype= data_type)
    data.tofile(pcmfile)

def pcm2wav(pcm_file, wav_file, channels=1, bits=16, sample_rate=32000):
    pcmf = open(pcm_file, 'rb')
    pcmdata = pcmf.read()
    pcmf.close()
    if bits % 8 != 0:
        raise ValueError("bits % 8 must == 0. now bits:" + str(bits))
    wavfile = wave.open(wav_file, 'wb')
    wavfile.setnchannels(channels)
    wavfile.setsampwidth(bits // 8)
    wavfile.setframerate(sample_rate)
    wavfile.writeframes(pcmdata)
    wavfile.close()

def wav2pcm_infile(FILE_PATH_WAV, FILE_PATH_PCM, data_type=np.int16):
    files = os.listdir(FILE_PATH_WAV)
    for file in files:
        wav2pcm(FILE_PATH_WAV+"/"+file, FILE_PATH_PCM+"/"+file, data_type)
    