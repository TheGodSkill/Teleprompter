from PIL import Image
import ST7735
import time
import sys
from gpiozero import SPIDevice, DigitalOutputDevice

print("""
gif.py - Display a gif on the LCD.
If you're using Breakout Garden, plug the 0.96" LCD (SPI)
breakout into the front slot.
""")

if len(sys.argv) > 1:
    image_file = sys.argv[1]
else:
    print("Usage: {} <filename.gif>".format(sys.argv[0]))
    sys.exit(0)

spi = SPIDevice(port=0, device=0, baudrate=4000000, polarity=0, phase=0)
dc = DigitalOutputDevice(9)
bl = DigitalOutputDevice(19)

# Create TFT LCD display class.
disp = ST7735.ST7735(
    spi=spi,
    dc=dc,
    rst=None,
    cs=0,
    backlight=bl,
    rotation=270,
    width=80,
    height=160,
    colstart=24,
    rowstart=0
)

# Initialize display.
disp.init()

width = disp.width
height = disp.height

# Load an image.
print('Loading gif: {}...'.format(image_file))
image = Image.open(image_file)

print('Drawing gif, press Ctrl+C to exit!')
print('Eddy du genius')

frame = 0

while True:
    try:
        image.seek(frame)
        disp.display(image.resize((width, height)))
        frame += 1
        time.sleep(0.05)

    except EOFError:
        frame = 0
