
from pynput.keyboard import Key, Controller, Listener
import time
import random


# askey=Controller()
# sentence="this is a sentence type by python script not by me"
# askey.type(sentence)
# for c in sentence:
#     askey.press(c)
#     askey.release(c)
#     delay=random.uniform(0,0.2)
#     print(delay)
#     time.sleep(delay)
def on_press(key):
    print("key pressed:",key)
    Listener.stop()
def on_release(key):
    print("key release:",key)
with Listener(on_press=on_press, on_release=on_release) as Listener:
    Listener.join()

# from pynput.keyboard import Key, Controller
# keyboard = Controller()
# keyboard.press(input('a'))
# keyboard.release(input('a'))
# keyboard.press(Key.space)
# keyboard.release(Key.space)
# keyboard.press(Key.ctrl)
# keyboard.release(Key.ctrl)
# keyboard.type(input('Hello World!!'))