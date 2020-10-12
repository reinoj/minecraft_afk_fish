from math import ceil, floor
import numpy as np
from PIL import ImageGrab
from threading import Thread
import time

import keyboard
import mouse

# global variable for whether to be fishing or not
FISHING = False

# sets FISHING to true and starts fish function
def startFishing():
    global FISHING
    if not FISHING:
        FISHING = True
        Thread(target=fish).start()

# sets FISHING to false
def stopFishing():
    global FISHING
    if FISHING:
        FISHING = False

# function for fishing
def fish():
    global FISHING
    im = np.asarray(ImageGrab.grab())
    v, h, _ = im.shape
    
    vLow = floor(v * 0.521)
    vHigh = ceil(v * 0.694)
    hLow = floor(h * 0.492)
    hHigh = ceil(h * 0.510)
    step = ceil(v * 0.00347)

    while FISHING:
        im = np.asarray(ImageGrab.grab())
        im = im[vLow:vHigh, hLow:hHigh, :]
        
        if hasBobber(im, step):
            mouse.click(button='right')
            time.sleep(0.5)
            mouse.click(button='right')
            time.sleep(0.9)
        time.sleep(0.1)

# determines whether the bobber is in the image
def hasBobber(im, step):
    v, h, _ = im.shape
    for i in range(0, v, step):
        for j in range(h):
            if im[i, j, 0] > 118:
                if im[i, j, 2] < 112:
                    return True
    return False
# def hasBobber(im):
#     v, h, _ = im.shape
#     rcount = 0
#     for i in range(0, v, 5):
#         for j in range(h):
#             if rcount > 10:
#                 return True
#             if im[i, j, 0] > 118:
#                 rcount += 1
#     return False

def main():
    # hotkey to start fishing
    keyboard.add_hotkey('ctrl+alt+f', startFishing)
    # hotkey to stop fishing
    keyboard.add_hotkey('ctrl+alt+s', stopFishing)
    
    # wait to exit until these keys are pressed
    keyboard.wait('ctrl+alt+d')

if __name__ == "__main__":
    main()