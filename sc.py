from pynput.mouse import Button, Controller
import time
mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
     mouse.position))

#click mouse button
mouse.click(Button.left,2)

totaltime = 15
interval = 60

while True:
    print('The current pointer position is {0}'.format(mouse.position))
    time.sleep(180)
    
    mouse.click(Button.left,1)


