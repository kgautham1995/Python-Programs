import pyautogui
import time
pyautogui.FAILSAFE=False
while True:
    time.sleep(10)
    for i in range(0, 100):
        pyautogui.moveTo(0, i * 3)
    for i in range(0, 1):
        pyautogui.press('enter')
