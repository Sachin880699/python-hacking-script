import pyautogui
import platform
from pathlib import Path
import os.path
import time


os = platform.system()


if os=='Linux':
    home = str(Path.home())


    screenshot = pyautogui.screenshot()
    screenshot.save(home + "/screen.png")
    time.sleep(5)

    home = str(Path.home())
    data = home + "/screen.png"

    import os

    myfile = data

    if os.path.isfile(myfile):
        os.remove(myfile)
    else:  ## Show an error ##
        print("Error: %s file not found" % myfile)






