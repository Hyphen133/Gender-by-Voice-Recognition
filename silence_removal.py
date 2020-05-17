import librosa
import time

start = time.time()

data, sampling_rate = librosa.load('F_0101_10y4m_1.wav')
x = librosa.effects.split(data, top_db=40)

end = time.time()
print(end - start)

interval_start = x[2][0]
interval_end = x[2][1]

librosa.output.write_wav("test.wav", data[interval_start:interval_end], sampling_rate)