import pyautogui

size = pyautogui.size()
postion = pyautogui.position()


class Fun():

    def Box():
        box = pyautogui.alert('This is an alert box.')
        return box

    def Down():
        down = pyautogui.press('down')
        return down

    def Up():
        up = pyautogui.press('up')
        return up

    def Right():
        right = pyautogui.press('right')
        return right

    def Left():
        left = pyautogui.press('left')
        return left

    def Space():
        space = pyautogui.press('space')
        return space

    def EN_s():
        s = pyautogui.press('s')
        return s
