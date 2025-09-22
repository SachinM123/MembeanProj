import pyautogui
import time

while True:
    pyautogui.keyDown('a')
    time.sleep(1)
    pyautogui.keyUp('a')
    pyautogui.keyDown('d')
    time.sleep(1)
    pyautogui.keyUp('d')