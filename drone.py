from djitellopy import tello
#import tellopy     //not needed for this code
import time

#evable venv
#source source myenv/bin/activate 

# Check if firewall allow incoming connections:
# Python (whichever interpreter VS Code is using)
# Visual Studio Code (after adding, it is shown as CODE)

#do disable firewall completly
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