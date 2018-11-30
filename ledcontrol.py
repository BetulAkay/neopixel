import time
from neopixel import *
import neopixel
import argparse
import math


# LED strip configuration:
LED_COUNT = 30  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53


def SetAll(strip, color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)

def TurnOn(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()


def snake(strip, color, red, green, blue, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(0, LED_COUNT):      #strip.numPixels()
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)
    for i in range(127, 0, -1):  # new line
        r = int(math.floor((i / 127.0) * red))
        g = int(math.floor((i / 127.0) * green))
        b = int(math.floor((i / 127.0) * blue))
        SetAll(strip, Color(r, g, b))
        strip.show()
        time.sleep(0.005)
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()


def BreathInOut(strip, red, green, blue):
    # Fade In.

    for i in range(0, 127):
        r = int(math.floor((i / 127.0) * red))
        g = int(math.floor((i / 127.0) * green))
        b = int(math.floor((i / 127.0) * blue))
        SetAll(strip, Color(r, g, b))
        strip.show()
        time.sleep(.01)
        # Fade Out.
    for i in range(256, 0, -1):
        r = int(math.floor((i / 127.0) * red))
        g = int(math.floor((i / 127.0) * green))
        b = int(math.floor((i / 127.0) * blue))
        SetAll(strip, Color(r, g, b))
        strip.show()
        time.sleep(.01)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            print("Fading Snake")
            snake(strip, Color(127, 127, 127), 127, 127, 127)
            print("Breathing Effect")
            BreathInOut(strip, 127, 127, 127)
            print("Movements")
            OutsideToCenter(strip, 255, 0, 0, 8, .5, .05)
            print("meeting")
            meeting(strip, 127, 127, 127)
            print("TurnOn")
            TurnOn(strip, Color(127, 127, 127))
            print("Reversed Color Wipe")
            ColorWipeReverse(strip, 127, 127, 127, 0.5)


    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0, 0, 0), 10)