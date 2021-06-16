import time
import pyautogui

x = 0
y = 0

anim_x = 0
anim_y = 0

v = 1
t = input("Video Amount: ")
try:
    t = int(t)
except:
    print("Please Type Numbers Only!")
    exit()

pauseBeforeStart = input("Seconds To Wait Before Starting: ")
try:
    pauseBeforeStart = int(pauseBeforeStart)
except:
    print("Please Type Numbers Only!")
    exit()

time.sleep(pauseBeforeStart)

while v < t + 1:
    v = v + 1
    x = x + 1
    if x > 10:
        x = 1
        y = y + 1
    anim_x = anim_x + 1
    if anim_x > 7:
        anim_x = 1
        anim_y = anim_y + 1
    for scroll in range(anim_y):
        pyautogui.click(885, 125)
        time.sleep(( 0.4 * anim_y ))
    time.sleep(0.4)
    pyautogui.click(65 + ( 105 * ( anim_x - 1) ), 125)
    pyautogui.click(915 + ( 100 * ( x - 1 ) ), 245 + ( 100 * y ))
    time.sleep(0.4)
    pyautogui.click(225, 50)
    time.sleep(0.4)
