import speech_recognition as sr
import time
import board
import adafruit_st7735 as st7735


spi = board.SPI()
tft_cs = board.CE0
tft_dc = board.D25
display = st7735.ST7735R(spi, rotation=90, cs=tft_cs, dc=tft_dc)


r = sr.Recognizer()
mic = sr.Microphone()

# read text
with open('Script.txt') as f:
    text = f.read()
words = text.split()

# function to display  10 words
def display_next_10_words(start_index):
    display.fill(0)
    display.text(' '.join(words[start_index:start_index+10]), 0, 0, color=(255, 255, 255))
    display.show()


i = 0
while i < len(words):
    display_next_10_words(i)
    if words[i] == 'also':
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            if 'also' in text.lower():
                i += 10
        except sr.UnknownValueError:
            pass
    i += 1
    time.sleep(0.5)
