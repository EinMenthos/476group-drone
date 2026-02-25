from djitellopy import tello
import time
from pynput.keyboard import Listener

keyboard_quit = False

def keyboard_handler(key):
    global keyboard_quit
    if hasattr(key, 'char') and key.char == 'q':
        keyboard_quit = True
        return False  # Stop listener

me = tello.Tello()
me.connect()

# Start non-blocking listener
listener = Listener(on_press=keyboard_handler)
listener.start()

while not keyboard_quit:
    print(f"X-Axis: {me.get_acceleration_x()}")
    print(f"Y-Axis: {me.get_acceleration_y()}")
    print(f"Z-Axis: {me.get_acceleration_z()}")
    time.sleep(5)

me.end()