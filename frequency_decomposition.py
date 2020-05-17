import librosa

y, sr = librosa.load(librosa.util.example_audio_file())
S = librosa.feature.melspectrogram(y=y, sr=sr)
components, activations = librosa.decompose.decompose(S)
print()