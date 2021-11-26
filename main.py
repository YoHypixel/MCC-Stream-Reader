from selenium import webdriver
from selenium.webdriver.common.by import By
import pytesseract
import time
import os
import cv2 as cv
import numpy as np
from PIL import Image, ImageFilter


def main():
    driver = webdriver.Chrome()
    driver.get("https://youtu.be/KcVHmlYsjnY?t=728")
    time.sleep(5)
    counter = 0
    elem = driver.find_element(By.XPATH, '//*[@id="movie_player"]')
    elem.click()
    time.sleep(0.4)
    elem.click()
    time.sleep(.5)
    elem.send_keys("f")
    while counter < 5:
        elem.click()
        time.sleep(0.4)
        elem.click()
        elem.screenshot("yo.png")
        origin = Image.open("yo.png")
        max_size = (4028, 1028)
        w, h = origin.size
        origin = origin.crop((970, 221, w - 80, h - 420))
        origin.save(f"output/wow1{counter}.png")
        origin.close()
        origin = Image.open(f"output/wow1{counter}.png")
        i = origin.resize(max_size, Image.ANTIALIAS)
        i = i.filter(ImageFilter.SHARPEN)
        i = i.filter(ImageFilter.SMOOTH)
        i = i.filter(ImageFilter.DETAIL)
        # i = i.convert("L")
        # i = i.point(lambda p: p > 100 and 255)
        i.save(f"output/wow2{counter}.png")
        i.close()
        convert = cv.imread(f"output/wow2{counter}.png")
        top = np.array([255, 255, 255])
        bottom = np.array([10, 10, 10])
        mask = cv.inRange(convert, bottom, top)
        res = cv.bitwise_and(convert, convert, mask=mask)
        cv.imwrite(f'output/wow3{counter}.png', res)
        test = Image.open(f"output/wow3{counter}.png")
        i = test.convert("L")
        i = i.point(lambda p: p > 100 and 255)
        i.save(f'output/{counter}.png')
        game_time = pytesseract.image_to_string(i)
        test.close()
        game_time = game_time.split("\n")
        game_time = game_time[0]
        if game_time == '0':
            print('no output')
        else:
            print(game_time)
        os.remove('yo.png')
        time.sleep(1)
        counter += 1
    driver.close()


if __name__ == '__main__':
    main()
