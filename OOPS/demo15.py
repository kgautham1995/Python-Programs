import pyautogui as p
import webbrowser as wb
import time
wb.open("web.whatsapp.com")
word="Programming with gautam"
time.sleep(30)
for i in range(100):
    for x in word:
        p.press(x)
    p.press("enter")