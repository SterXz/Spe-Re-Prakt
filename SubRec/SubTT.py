import pytesseract
from videocr import get_subtitles

# Указание пути к tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

if __name__ == '__main__':  # This check is mandatory for Windows.
    result_file = open("subttres.txt", "a+")
    mp4path = 'heigthcheck.mp4'
    result_file.write(get_subtitles(mp4path, lang='rus', sim_threshold=70, conf_threshold=65))
    # print(get_subtitles('subtest.mp4', lang='rus', sim_threshold=70, conf_threshold=65))
    result_file.close()
