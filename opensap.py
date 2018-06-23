import pyautogui as pagi
import webbrowser
import time
import pyperclip
import csv
from PIL import Image

# shortcut keys to copy


def ctrlc():
    pagi.keyDown('ctrl')
    pagi.keyDown('c')
    pagi.keyUp('c')
    pagi.keyUp('ctrl')

# hot-keys to copy


def copy():
    ulist = pagi.click(395, 850), pagi.dragRel(0, 249, 2), pagi.dragRel(1168, 0, 2), pagi.hotkey('ctrl', 'c')


link_obj = webbrowser.open('http://kiitportal.kiituniversity.net/irj/portal')
try:
    # '''
    #  FAILSAFE = False
    # User
    time.sleep(5)
    # pagi.click(926, 553)

    '''coordinates = pagi.locateOnScreen('../Images/User.PNG')
    centre = pagi.center(coordinates)
    pagi.click([centre[0]+200, centre[1]])'''

    pagi.typewrite('1605XXX')
    coordinates = pagi.position()
    # Position
    print(coordinates)
    time.sleep(2)
    pagi.click(coordinates[0], coordinates[1]+20)
    # pagi.click(940, 582)
    pagi.typewrite('Your Password')
    # Log on button
    time.sleep(2)
    pagi.click(1121, 643)
    # Student self service link
    time.sleep(2)
    pagi.click(173, 236)  # (229, 245)
    # Student attendance details
    time.sleep(2)
    pagi.click(93, 726)  # (1417, 860)
    # '''
    # Copying data by dragging
    #pyperclip.copy('')
    time.sleep(10)

    copy()
    # saving a screen-shot of attendance details
    image = pagi.screenshot()
    image.save("../Images/screenshot1.png")
    data = pyperclip.paste()
    if data is None:
        print("Not Working!!")
        raise KeyboardInterrupt
    # since hotkey() doesn't work properly use pywinauto
    # image.save('a');
    # Image.open('a')
    print(data)
    # modify the data to remove newlines
    cdata = ""
    for i in data:
        if i is '\n' or i is '\r':
            cdata += ''
        else:
            cdata += i

    # print('where"s')
    print(cdata)
    '''
    # writing onto csv
    csv_file = open('sample.csv', 'w', newline='')
    csv_writer = csv.writer(csv_file)
    row = []
    cell = ''
    n = len(cdata)
    for i in range(0, n):
        try:
            if i + 1 < n and cdata[i] is ' ' and cdata[i + 1] is ' ':
                csv_writer = csv.writerow(row)
                print(row)
                row = []
            elif cdata[i] is ' ':
                row.append(cell)
                cell = ''
            else:
                cell += cdata[i]
        except EOFError:
            pass
    '''

except KeyboardInterrupt:
    print("Interrupted")

pagi.click(1708, 171)
time.sleep(10)
coordinates = pagi.locateOnScreen('attendanceSubject.PNG')
centre = pagi.center(coordinates)
pagi.click(centre)
