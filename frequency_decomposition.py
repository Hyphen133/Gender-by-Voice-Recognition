import librosa
import numpy as np
import librosa.display
# def PitchSpectralHps(X, f_s):
# 
#     # initialize
#     iOrder = 4
#     f_min = 300
#     f = np.zeros(X.shape[1])
# 
#     iLen = int((X.shape[0] - 1) / iOrder)
#     afHps = X[np.arange(0, iLen), :]
#     k_min = int(round(f_min / f_s * 2 * (X.shape[0] - 1)))
# 
#     # compute the HPS
#     for j in range(1, iOrder):
#         X_d = X[::(j + 1), :]
#         afHps *= X_d[np.arange(0, iLen), :]
# 
#     f = np.argmax(afHps[np.arange(k_min, afHps.shape[0])], axis=0)
# 
#     # find max index and convert to Hz
#     f = (f + k_min) / (X.shape[0] - 1) * f_s / 2
# 
#     return (f)
# 
# y, sr = librosa.load('F_0101_10y4m_1.wav')
# PitchSpectralHps(y, sr)
# S = librosa.feature.melspectrogram(y=y, sr=sr)
# components, activations = librosa.decompose.decompose(S, n_components=3, sort=True)
# print()

import matplotlib.pyplot as plt

n_mels = 280
fmax = 280


def get_fundamental_frequencies_values(filepath):
    y, sr = librosa.load(filepath)
    D = np.abs(librosa.stft(y)) ** 2
    S = librosa.feature.melspectrogram(S=D, sr=sr)
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels, fmax=fmax)
    print(S.transpose().shape)
    values = []
    for s in S.transpose():
        values.append(np.argmax(s) * fmax / n_mels)

    # plt.figure(figsize=(10, 4))
    # S_dB = librosa.power_to_db(S, ref=np.max)
    # librosa.display.specshow(S_dB, x_axis='time',
    #                          y_axis='mel', sr=sr,
    #                          fmax=20000)
    # plt.colorbar(format='%+2.0f dB')
    # plt.title('Mel-frequency spectrogram')
    # plt.tight_layout()
    # plt.show()
    return values
