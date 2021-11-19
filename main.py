# import pytesseract
from PIL import Image, ImageFilter
# from scipy.ndimage.filters import gaussian_filter
# import numpy
# from selenium import webdriver
# from selenium.webdriver.common.by import By
import time


def main():
    # driver = webdriver.Chrome()
    # driver.get("https://youtu.be/KcVHmlYsjnY?t=728")
    # time.sleep(5)
    # elem = driver.find_element(By.XPATH, '//*[@id="movie_player"]')
    # time.sleep(2)
    # elem.screenshot("yo.png")
    origin = Image.open("yo.png")
    black_and_white = origin.convert("L")
    threshold = black_and_white.point(lambda p: p > 100 and 255)
    threshold = threshold.filter(ImageFilter.EDGE_ENHANCE_MORE)
    threshold = threshold.filter(ImageFilter.SHARPEN)
    threshold = threshold.filter(ImageFilter.SMOOTH_MORE)
    threshold.save("wow.png")
    time.sleep(.2)
    cropped = Image.open("wow.png")
    w, h = cropped.size
    wow = cropped.crop((580, 120, w, h-140))
    wow.save("out.png")

if __name__ == '__main__':
    main()
