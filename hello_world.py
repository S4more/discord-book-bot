from pyautogui import hotkey, press, screenshot, click, position
import ai
import pyperclip
import time
import sys
import subprocess

def captureScreen():
    myScreenshot = screenshot()
    myScreenshot.save('screenshot.png')

def moveMouse():
    point = ai.getPoints()
    try:
        click(point[0], point[1])
    except:
        tracer("Discord wasn't detected")


def copyAndWrite(file):
    """Reads file, line by line and paste each one of them
        where the mouse is."""

    # position of the mouse
    initialPoint = position()
    bounding_box = {'top': 330, 'left': int(initialPoint[0]) - 100, 'width': 560, 'height': 265}


    with open(file, "r") as a_file:
        for line in a_file:
            if ai.isFlooding(bounding_box):
                print("You are sending messages too fast.")
                for second in range (0, 5):
                    time.sleep(1)
                    # print(f'{second + 1}s ellapsed. {5 - second -1} more to go.')

                click(initialPoint[0], initialPoint[1])
                time.sleep(0.5)
                press('enter')

            if position() != initialPoint:
                return

            try:
                line = line.strip().split(": ")[1]
            except:
                line = line.strip()

            if line == "<Media omitted>":
                continue
            elif line.strip == "":
                continue

            pyperclip.copy(line)
            hotkey('ctrl', 'v')
            press('enter')
            time.sleep(0.6)

def tracer(message):
    print(f"{'-'*(len(message) - 15)}DISCORD FLOODER{'-'*(len(message) - 15)}")
    print(f"ERROR: {message}.")
    sys.exit(f"{'-'* (len(message) + 8)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        tracer("File not especified")
    subprocess.run(["wmctrl", "-a", "discord"])
    time.sleep(1)

    captureScreen()
    moveMouse()
    start = time.time()
    copyAndWrite(sys.argv[1])
    end = time.time()
    print(end - start)

    print("Mouse moved. Breaking the program.")
