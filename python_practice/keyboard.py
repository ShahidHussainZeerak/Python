from pynput import keyboard
from pynput.keyboard import key ,Controller
import time
keyboard=Controller()
time.sleep(3)
# keyboard.press('a')
# keyboard.release('a' )
# sentence="this  is a sentence : "
# keyboard.type(sentence)
# for c in sentence:
#     keyboard.type(sentence)
# time.sleep(5)

# def say(word):
#     time.sleep(2)
#     keyboard.type(word)
# print(say("hello"))

keyboard.press(key.cmd)
keyboard.release(key.cmd)
