import librosa as librosa
import numpy as np
import matplotlib.pyplot as plt

data, sampling_rate = librosa.load('friday-rocks.wav')


frequency_components = np.fft.fft(data)
frequency_components = np.abs(frequency_components)
frequency_components = frequency_components[:int(sampling_rate/2)]
frequency_values = np.linspace(0, len(frequency_components), len(frequency_components))

frequency_components = frequency_components[:280]
frequency_values = frequency_values[:280]

plt.plot(frequency_values, frequency_components)
plt.show()

mean_freq = sum([ frequency_values[i] * frequency_components[i] for i in range(len(frequency_values))])/sum(frequency_components)
mean_freq = mean_freq/1000

print("Mean frequency: " + str(mean_freq))

print()