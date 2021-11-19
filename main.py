# from scipy.ndimage.filters import gaussian_filter
# import numpy
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytesseract
import time
import cv2

from PIL import Image, ImageFilter


def main():
    driver = webdriver.Chrome()
    driver.get("https://youtu.be/KcVHmlYsjnY?t=728")
    time.sleep(5)
    elem = driver.find_element(By.XPATH, '//*[@id="movie_player"]')
    elem.click()
    time.sleep(0.4)
    elem.click()
    time.sleep(.5)
    elem.send_keys("f")
    elem.screenshot("yo.png")
    origin = Image.open("yo.png")
    black_and_white = origin.convert("L")
    threshold = black_and_white.point(lambda p: p > 100 and 255)
    threshold = threshold.filter(ImageFilter.EDGE_ENHANCE_MORE)
    threshold = threshold.filter(ImageFilter.SHARPEN)
    threshold = threshold.filter(ImageFilter.SMOOTH_MORE)
    threshold = threshold.filter(ImageFilter.FIND_EDGES)
    w, h = threshold.size
    threshold = threshold.crop((580, 120, w-20, h-170))
    threshold.save("wow.png")
    time.sleep(.2)
    cropped = Image.open("wow.png")
    print(pytesseract.image_to_string(cropped))


if __name__ == '__main__':
    main()
