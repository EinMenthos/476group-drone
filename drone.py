from djitellopy import tello
#import tellopy     //not needed for this code
import time

#enable venv
#source source myenv/bin/activate 

# check ping
# ping 192.168.10.1

# Allow Local Network Access (macOS Sequoia/Big Sur): (this is it!!!)
# Go to System Settings > Privacy & Security > Local Network. 
# Ensure your terminal app (Terminal, iTerm, PyCharm, VS Code) is enabled.

# Check if firewall allow incoming connections: (not work)
# Python (whichever interpreter VS Code is using)
# Visual Studio Code (after adding, it is shown as CODE)

#do disable firewall completely (did not work)
# MACOS -> SYSTEM -> NETWORK -> Firewall

#check if there is any app using port 8889
# lsof -nP | grep UDP
# next code is more specific. Nothing happens if port is not being used.
# lsof -nP | grep UDP | grep 8889

# check if package is installed correctly
# pip show djitellopy

me = tello.Tello()
me.connect()
print("Test: Battery Status: ")
print(me.get_battery())