from PIL import Image
from gpiozero import SPIDevice, DigitalOutputDevice
import ST7735
import time
import sys

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

# Create TFT LCD display class.
spi_device = SPIDevice(port=0, device=0)
cs_pin = DigitalOutputDevice(10, active_high=True)
dc_pin = DigitalOutputDevice(9, active_high=True)
backlight_pin = DigitalOutputDevice(19, active_high=True)

disp = ST7735.ST7735(
    spi=spi_device,
    cs=cs_pin,
    dc=dc_pin,
    backlight=backlight_pin,
    rotation=0
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
