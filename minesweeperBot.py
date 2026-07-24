from selenium import webdriver
import undetected_chromedriver as uc
import pynput


options = uc.ChromeOptions()
driver = uc.Chrome(options=options, use_subprocess=False)

minesweeperLink = "https://www.google.com/search?q=minesweeper&rlz=1C1VDKB_en-GBAU1163AU1163&oq=minesweeper&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg70gEIMTY0NGowajeoAgCwAgA&sourceid=chrome&source=chrome.ob&ie=UTF-8&safe=active&ssui=on"
browser = webdriver.Chrome()
browser.get(minesweeperLink)
