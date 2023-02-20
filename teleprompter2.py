import speech_recognition as sr
import time
import st7735


display = st7735.ST7735(
    port=0,
    cs=1,
    dc=9,
    backlight=12,
    rotation=270,
    spi_speed_hz=4000000
)


r = sr.Recognizer()
mic = sr.Microphone()


with open('Script.txt') as f:
    text = f.read()
words = text.split()


def display_next_10_words(start_index):
    display.fill(0)
    display.text(' '.join(words[start_index:start_index+10]), 0, 0, color=st7735.WHITE)
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
