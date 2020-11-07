import psutil
import time

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)
if(plugged):
    plugged = "YES"
else:
    plugged = "NO"
# print('Battery Percentage: '+percent+'% \nCharger Plugged:    '+plugged)
while(True):
    print('Battery Percentage: '+percent+'% \nCharger Plugged:    '+plugged)
    ch = input('Enter \"EXIT\" to exit the window: ')
    if(ch == "EXIT"):
        break