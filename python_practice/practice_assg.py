# i=1
# while i<=400:
#     print(i)
#     i+=1
from pynput import keyboard
from pynput.keyboard import Key,Controller,Listener
import time
keyboard=Controller()
def cordinate(x,y):
    x=10
    y=10
   if input(keyboard.press(Key.lift)):
       x=+1
       y=y
    elif input(keyboard.press(Key.right)):
        y=+1
        x=x
    elif input(keyboard.press(Key.up)):
        x=+1
        y=y
    elif input(keyboard.press(Key.down)):
        x=x
        y=+1
    else:
        print(" Hello")


