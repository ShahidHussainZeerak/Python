from pynput import keyboard
from pynput.keyboard import Key,Listener
import time
keyboard=Listener()
def cordinate(x,y):
    x=10
    y=10
    if input(keyboard.press(Key.left)):
        x=+1
        y=y
    elif input(keyboard.press(Key.right)):
        x=x
        y=+1
    elif input(keyboard.press(Key.up)):
        x=+1
        y=y
    elif input(keyboard.press(Key.down)):
        x=x
        y=+1
    else:
        print("Hello")
cordinate(10,10)
