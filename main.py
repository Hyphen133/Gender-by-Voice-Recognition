import subprocess


def get_recorded_audio_sample():
    r_command = '"C:\\Program Files\\R\\R-4.0.0\\bin\\x64\\Rscript.exe" C:\\Users\\stz\\Desktop\\VoiceGenderReckognition\\main.R'
    vector = subprocess.check_output(r_command)
    return [float(i) for i in str(vector).split("\"")[1].split(" ")]

print(get_recorded_audio_sample())

