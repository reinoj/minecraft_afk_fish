from math import ceil, floor
import numpy as np
from PIL import ImageGrab
from threading import Thread
import time
# import matplotlib.pyplot as plt

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
    
    vLow = floor(v * 0.438)
    vHigh = ceil(v * 0.478)
    hLow = floor(h * 0.497)
    hHigh = ceil(h * 0.500)
    step = ceil(v * 0.00139)

    while FISHING:
        im = np.asarray(ImageGrab.grab())
        im = im[vLow:vHigh, hLow:hHigh, :]

        # showImage(im)
        
        if not hasBobber(im, step):
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

# def showImage(im):
#     plt.imshow(im)
#     plt.show()

def main():
    print('Start Fishing: Ctrl + Alt + F')
    print('Stop Fishing:  Ctrl + Alt + S')
    print('Stop Script:   Ctrl + Alt + D')
    print('Conditions:\n- Looking down 20 degrees\n- One block back from water\'s edge')
    
    # hotkey to start fishing
    keyboard.add_hotkey('ctrl+alt+f', startFishing)
    # hotkey to stop fishing
    keyboard.add_hotkey('ctrl+alt+s', stopFishing)
    # wait to exit until these keys are pressed
    keyboard.wait('ctrl+alt+d')


if __name__ == "__main__":
    main()