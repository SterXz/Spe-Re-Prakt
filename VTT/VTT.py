# Конвертирование видео в аудио
import moviepy.editor as mp

# Загрузка модели
from vosk import Model, KaldiRecognizer, SetLogLevel
import os
import wave

# Отладка кода
SetLogLevel(-1)

# Локальный путь к видео файлу
clip = mp.VideoFileClip("./test.mp4")

# Локальный путь к аудио файлу
clip.audio.write_audiofile("./test_conv.wav", ffmpeg_params=["-ac", "1"])

# Проверка наличия модели
if not os.path.exists("vosk-model-ru-0.10"):
    print("Please download the model from "
          "https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit(1)

# Открытие аудиофайла формата wav
wf = wave.open("./test_conv.wav")

# Проверка соответствия WAV файла формату
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print("Audio file must be WAV format mono PCM.")
    exit(1)

# Загрузка модели
model = Model("vosk-model-ru-0.10")
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)

# Создание ответа
results = []
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        results.append(rec.Result())
results.append(rec.FinalResult())
text = ''
for i in results:
    ind = i.find('text')
    if ind:
        ind += 9
        text += i[ind:-3]
        text += " "

result_file = open("./result.txt", "a+")
result_file.write(text)
result_file.close()
