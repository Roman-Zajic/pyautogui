import pyautogui
import logging
import os


logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s -  %(message)s',
                    datefmt='%H:%M:%S')


#global variables
screenWidth, screenHeight = pyautogui.size()
workspace = (0, 0, screenWidth, screenHeight)
imageFolder = os.getcwd() + os.sep + 'img' + os.sep

def checkImage(img, region = workspace):
    img_path = imageFolder + img
    location = None
    location = pyautogui.locateCenterOnScreen(img_path, region=region)

    return location != None


logging.info("starting program")
