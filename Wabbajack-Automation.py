from python_imagesearch.imagesearch import imagesearch
import pyautogui
import sys
import time
import win32api, win32con

maxTime   = 0                       # Time in minutes to wait with no matches until it closes (leave it as 0 for infinite time)
nFound    = 0                       # How many times the image was found/clicked
aniChar   = ["|", "/", "-", "\\"]   # aniChars between the searchs

print(" __          __   _     _           _            _                        _                        _   _             ")
print(" \ \        / /  | |   | |         (_)          | |            /\        | |                      | | (_)            ")
print("  \ \  /\  / /_ _| |__ | |__   __ _ _  __ _  ___| | __        /  \  _   _| |_ ___  _ __ ___   __ _| |_ _  ___  _ __  ")
print("   \ \/  \/ / _` | '_ \| '_ \ / _` | |/ _` |/ __| |/ /       / /\ \| | | | __/ _ \| '_ ` _ \ / _` | __| |/ _ \| '_ \ ")
print("    \  /\  / (_| | |_) | |_) | (_| | | (_| | (__|   <       / ____ \ |_| | || (_) | | | | | | (_| | |_| | (_) | | | |")
print("     \/  \/ \__,_|_.__/|_.__/ \__,_| |\__,_|\___|_|\_\     /_/    \_\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___/|_| |_|")
print("                                  _/ |                                                                               ")
print("                                 |__/                                                                                ")

def imagesearch_numLoop(image, maxSamples, precision=0.8):
    pos = imagesearch(image, precision);
    count = 0
    while pos[0] == -1:
        for i in range(len(aniChar)):
            time.sleep(0.1)
            sys.stdout.write("\r" + aniChar[i % len(aniChar)])
            sys.stdout.flush()
        pos = imagesearch(image, precision)
        count += 1
        if count > maxSamples:
            if maxSamples == 0:
                count -= 27000
            else:
                break
    return pos

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while (1):
    pos = imagesearch_numLoop("./slowdownload.png", maxTime*60)
    if pos[0] != -1:
        nFound += 1
        print("\r[%d]" %nFound, "Found at", "x:%d" %pos[0], "y:%d" %pos[1])
        click(pos[0]+67, pos[1]+6)
        time.sleep(0.1)   
    else:
        print("Couldn't find the button within the estimated time.")
        print("Button was found: %d times!" %nFound)
        input('Press anything to close...\n')
        sys.exit()
        