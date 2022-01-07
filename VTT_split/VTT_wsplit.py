# Импорты
import wave
import math
import contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip
import os

# Директория файла например C:/Users/User/Desktop
os.chdir("./")

# Имя файла без разрешения например
filename = "test"

# Задание переменных
vid_name = filename + ".mp4"
aud_name = filename + "_transcribed_speech.wav"
clip = AudioFileClip(vid_name)
clip.write_audiofile(aud_name)

# Разбиение файла
with contextlib.closing(wave.open(aud_name, 'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
total_duration = math.ceil(duration / 60)

# Загрузка распознавателя текста
r = sr.Recognizer()
# Распознавание файла по частям и вывод ответа
for i in range(0, total_duration):
    with sr.AudioFile(aud_name) as source:
        audio = r.record(source, offset=i*60, duration=60)
    f = open(filename+"_transcription.txt", "a")
    f.write(r.recognize_google(audio, language="ru-RU"))
    f.write(" ")
    print(r.recognize_google(audio, language="ru-RU"))
f.close()

print("DONE")
