import subprocess

oko = subprocess.check_output ('"C:\\Program Files\\R\\R-4.0.0\\bin\\x64\\Rscript.exe" C:\\Users\\stz\\Desktop\\VoiceGenderReckognition\\main.R')
oko = [float(i) for i in str(oko).split("\"")[1].split(" ")]
print('oko:', oko)