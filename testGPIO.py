from PIL import Image
import ST7735
import time
import sys
import RPi.GPIO as GPIO

print("""
gif.py - Display a gif on the LCD.
If you're using Breakout Garden, plug the 0.96" LCD (SPI)
breakout into the front slot.
""")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

if len(sys.argv) > 1:
    image_file = sys.argv[1]
else:
    print("Usage: {} <filename.gif>".format(sys.argv[0]))
    sys.exit(0)

# Set up GPIO pins.
CS_PIN = 8
DC_PIN = 25
BACKLIGHT_PIN = 24

GPIO.setup(CS_PIN, GPIO.OUT)
GPIO.setup(DC_PIN, GPIO.OUT)
GPIO.setup(BACKLIGHT_PIN, GPIO.OUT)

# Create TFT LCD display class.
disp = ST7735.ST7735(
    port=0,
    cs=CS_PIN,
    dc=DC_PIN,
    backlight=BACKLIGHT_PIN,
    spi_speed_hz=4000000
)

# Initialize display.
disp.begin()

width = disp.width
height = disp.height

# Load an image.
print('Loading gif: {}...'.format(image_file))
image = Image.open(image_file)

print('Drawing gif, press Ctrl+C to exit!')

frame = 0

while True:
    try:
        image.seek(frame)
        disp.display(image.resize((width, height)))
        frame += 1
        time.sleep(0.05)

    except EOFError:
        frame = 0
