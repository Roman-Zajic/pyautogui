import pyautogui
import logging
import os

logging.basicConfig(filename='log.txt', encoding='utf-8', format='%(asctime)s -  %(message)s', level=logging.DEBUG,
                    datefmt='%H:%M:%S')

# global variables
screenWidth, screenHeight = pyautogui.size()
workspace = (0, 0, screenWidth, screenHeight)  # screen size
imageFolder = os.getcwd() + os.sep + 'img' + os.sep  # image folder
pause = 3  # default waiting time


# checking if image is on screen returning true/false
def checkImage(img, region=workspace):
    try:
        imgPath = imageFolder + img
        location = pyautogui.locateCenterOnScreen(imgPath, region=region)
    except Exception as e:
        print(e)

    return location != None

def clickOn(img, region=workspace, button='left'):
    img_path = imageFolder + img

    try:
        location = pyautogui.locateCenterOnScreen(img_path, region=region)
        if location is None:
            logging.error("fail clicking on " + img)
        else:
            pyautogui.click(location, button=button)
            logging.info("clicked on " + img)
    except Exception as e:
        print(e)
    return location


# Main program
if __name__ == '__main__':
    logging.info("starting program")
