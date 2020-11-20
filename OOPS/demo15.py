import pyautogui
import webbrowser as wb
import time
wb.open("web.whatsapp.com")
time.sleep(30)
for i in range(1000):
    pyautogui.press("H")
    pyautogui.press("E")
    pyautogui.press("L")
    pyautogui.press("L")
    pyautogui.press("O")
    pyautogui.press("enter")