import librosa as librosa
import numpy as np
import matplotlib.pyplot as plt
from entropy import entropy
from scipy import stats

from utils.spectral_flatness import FeatureSpectralFlatness

data, sampling_rate = librosa.load('friday-rocks.wav')


frequency_components = np.fft.fft(data)
frequency_components = np.abs(frequency_components)
frequency_components = frequency_components[:int(sampling_rate/2)]
frequency_values = np.linspace(0, len(frequency_components), len(frequency_components))

#Converting to kHz
frequency_components = [fc/1000 for fc in frequency_components[:280]]
frequency_values = frequency_values[:280]

plt.plot(frequency_values, frequency_components)
plt.show()

mean_freq = sum([ frequency_values[i] * frequency_components[i] for i in range(len(frequency_values))])/sum(frequency_components)
std_freq = np.std(frequency_values)
median_freq = np.median(frequency_values)
q25 = np.quantile(frequency_values, 0.25)
q75 = np.quantile(frequency_values, 0.75)
iqr = stats.iqr(frequency_values)
skew = stats.skew(data)
kurt = stats.kurtosis(data)
spectral_entropy = entropy.spectral_entropy(data, sampling_rate, normalize=True)
spectral_flatness = np.mean(librosa.feature.spectral_flatness(y=data))

print("Mean frequency: " + str(mean_freq))
print("Standard deviation: " + str(std_freq))
print("Median: " + str(median_freq))
print("Q25: " + str(q25))
print("Q75: " + str(q75))
print("IQR: " + str(iqr))
print("Skew: " + str(skew))
print("Kurt: " + str(kurt))
print("Spectral Entropy: " + str(spectral_entropy))
print("Spectral Flatness: " + str(spectral_flatness))


print()