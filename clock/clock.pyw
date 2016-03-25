# clock app by Domantas Jurkus
from canvas import *
from math import *
from time import *

# functions for finding endpoint coordinates
def endX(centerX, r, degrees):
	return centerX + sin(radians(degrees))*r
def endY(centerY, r, degrees):
	return centerY - cos(radians(degrees))*r

# screen width, height, center point
WIDTH = 400
HEIGHT = 400
c = WIDTH/2

# length of clock hands
lenSec = 160
lenMin = 140
lenHou = 100

# these are use for the hour markers
r1 = 170
r2 = 185

# main functon
def main():

        # drawing the clock canvas
        create_oval(10, 10, WIDTH-10, HEIGHT-10, fill='#dde')

        # creating the hour markers
        for i in range(0, 361, 30):
                x1 = endX(c, r1, i)
                y1 = endY(c, r1, i)
                x2 = endX(c, r2, i)
                y2 = endY(c, r2, i)
                create_line(x1, y1, x2, y2)

        # some blank hands - these will be used for create_line
        newSecondHand = 0
        newMinuteHand = 0
        newHourHand = 0

        while True:

                # we take the old hands and draw them again
                # this is to prevent jitter
                oldSecondHand = newSecondHand
                oldMinuteHand = newMinuteHand
                oldHourHand = newHourHand

                # new hand calculations
                secondsFromStart = float(floor(clock()))
                currentSeconds = float(strftime("%S", gmtime()))
                currentMinutes = int(strftime("%M", gmtime()))
                currentHours = int(strftime("%I", gmtime()))

                # draw second hand
                secondsDeg = currentSeconds*6
                xSec = endX(c, lenSec, secondsDeg)
                ySec = endY(c, lenSec, secondsDeg)
                newSecondHand = create_line(c, c, xSec, ySec, fill='red')

                # draw minute hand
                minutesDeg = currentMinutes*6 + secondsDeg/60
                xMin = endX(c, lenMin, minutesDeg)
                yMin = endY(c, lenMin, minutesDeg)
                newMinuteHand = create_line(c, c, xMin, yMin)

                # draw hour hand
                hoursDeg = currentHours*30 + minutesDeg/6
                xHou = endX(c, lenHou, hoursDeg)
                yHou = endY(c, lenHou, hoursDeg)
                newHourHand = create_line(c, c, xHou, yHou)

                # first delete the old hands, then wait
                delete(oldSecondHand)
                delete(oldMinuteHand)
                delete(oldHourHand)
                wait(1)

runGraphicsFn(main)

complete()
