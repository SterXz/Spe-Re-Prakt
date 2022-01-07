#Локальная распаковка модели
from zipfile import ZipFile
with ZipFile('/vosk-model-ru-0.10.zip', 'r') as zf:
    zf.extractall('')
