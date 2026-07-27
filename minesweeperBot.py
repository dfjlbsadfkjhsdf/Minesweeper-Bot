import time
from selenium import webdriver
from pynput.mouse import Button, Controller
mouse = Controller()

from pynput.keyboard import Key, Controller
keyboard = Controller()

browser = webdriver.Chrome()
browser.get("https://www.google.com/fbx?fbx=minesweeper")
keyboard.press(Key.f11)

time.sleep(5)
mouse.position = (683, 384)
mouse.click(Button.left, 1)
time.sleep(2)
browser.save_screenshot("First.png")
