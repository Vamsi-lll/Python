# import the required modules
import pyautogui as auto
import time

# script to open the youtube in the chrome
auto.press("win")
time.sleep(2) # to delay the process for the system to responce
auto.typewrite("chrome",interval=0.5)
auto.press("enter")
time.sleep(2)
auto.press("tab")
time.sleep(2)
auto.press("enter")
time.sleep(2)
auto.hotkey("ctrl","t")  # special hot key for opening new tab in the chrome
time.sleep(1)
auto.typewrite("youtube.com",interval=0.5)
auto.press("enter")
