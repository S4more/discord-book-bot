import cv2
import numpy as np
from mss import mss
import subprocess


# TODO user needs to decide which monitor
def screenResolution() -> dict:
    output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
    resolution = output.split()[1].split(b'x')
    return {'width' : 1400, 'height' : 900}


def getPoints():
    img_bgr = cv2.imread('screenshot.png')
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    template = cv2.imread('./icons/chatAnchor.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.95
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        return [pt[0] + w + 50, pt[1] +h / 2]

def isFlooding(bounding_box):
    sct = mss()

    # while True:
    img_bgr = sct.grab(bounding_box)
    img_gray = cv2.cvtColor(np.array(img_bgr), cv2.COLOR_BGR2GRAY)

    template = cv2.imread('./icons/discordWarning.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.6
    loc = np.where(res >= threshold)

    try:
        for pt in zip(*loc[::-1]):
            return True

    except:
        return False

def debug():
    plusIcon = getPoints()
    resolution = screenResolution()
    bounding_box = {'top': resolution['height'] //2 - 251 // 2, 'left': resolution['width'] // 2 - 285, 'width': 551, 'height': 265}

    sct = mss()

    while True:
        img_bgr = sct.grab(bounding_box)
        img_gray = cv2.cvtColor(np.array(img_bgr), cv2.COLOR_BGR2GRAY)

        template = cv2.imread('./icons/discordWarning.png', 0)
        print(template.shape)

        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
            print(pt)

        cv2.imshow('screen', np.array(img_bgr))

        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    debug()