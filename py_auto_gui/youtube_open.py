import pyautogui as auto
import time

auto.press("win")
time.sleep(2)
auto.typewrite("chrome",interval=0.5)
auto.press("enter")
time.sleep(2)
auto.press("tab")
time.sleep(2)
auto.press("enter")
time.sleep(2)
auto.hotkey("ctrl","t")
time.sleep(1)
auto.typewrite("youtube.com",interval=0.5)
auto.press("enter")
