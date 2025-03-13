import pyautogui
import time
from PIL import ImageGrab


class PianoTiles():
    
    def __init__(self):
        self.screenWidth, self.screenHeight = pyautogui.size()
        print(self.screenWidth, self.screenHeight)

        self.t1 = self.screenWidth*0.33 # 0.33 650
        self.t2 = self.screenWidth*0.41 # 0.41 800
        self.t3 = self.screenWidth*0.48 # 0.48 925
        self.t4 = self.screenWidth*0.54 # 0.54 1050
        self.h = self.screenHeight*0.63
        self.round = 0

        self.pos = [(self.t1, self.h), (self.t2, self.h), (self.t3, self.h), (self.t4, self.h)]

    def clc(self, pos): # Click (Moves and clicks mouse)
        pyautogui.click(pos[0], pos[1])

    def start(self):
        start_color_present = 0
        while start_color_present == 0:
            image = ImageGrab.grab()
            image_gray = image.convert('L')
            for i, value in enumerate(self.pos):
                pixel = image_gray.getpixel(value)
                if pixel == 132:
                    mt_value = self.pos[i]
                    self.clc(mt_value)
                    start_color_present = 1
            if pixel != 132:
                    time.sleep(0.1)
            

    def test_and_click(self, boost):
        image = ImageGrab.grab()
        image_gray = image.convert('L')
        for i, value in enumerate(self.pos):
                test_value = (value[0], (self.h-boost))
                pixel = image_gray.getpixel(test_value)
                print(pixel)
                if pixel <= 150:
                    mt_value = self.pos[i]
                    self.clc(mt_value)
                    self.round += 1
                    break
    
    def go(self):
        #time.sleep(3)
        #test()
        #l.mt(t2,h)
        boost = 50
        self.start()
        for repeat in range(2000):
            self.test_and_click(boost)
            #if self.round >= 400:
            #    boost = 70
            #if self.round >= 580:
            #    boost = 130
            #elif self.round >= 500:
            #    boost = 90
            #elif self.round >= 400:
            #    boost = 70
            #time.sleep(0.001)
        #image_gray.show()
