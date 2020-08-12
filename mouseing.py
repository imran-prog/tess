import pyautogui
import keyboard
import time


class mouse_control:

    def __init__(self):
        pass

    @staticmethod
    def resolution():
        return pyautogui.size()

    @staticmethod
    def opening_computer_window():
        keyboard.press_and_release('win + m')
        pyautogui.moveTo(41, 39, duration=0.5)
        pyautogui.click(41, 39)
        pyautogui.click(41, 39)
        time.sleep(1)
        keyboard.press_and_release("alt + space")
        for i in range(4):
            keyboard.press_and_release("down")
        keyboard.press_and_release("enter")
        time.sleep(1)

    @staticmethod
    def opening_folder():
        time.sleep(2)
        pyautogui.click(871, 442)
        pyautogui.click(871, 442)
        time.sleep(1)
        pyautogui.click(871, 442)
        pyautogui.click(871, 442)

mouse_control.opening_computer_window()
time.sleep(2)
mouse_control.opening_folder()