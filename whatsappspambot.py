import pyautogui as auto
from time import sleep

while True:
    auto.write('hello hello!')
    auto.press('enter')
    sleep(0.005)
