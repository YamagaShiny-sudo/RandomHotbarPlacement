import random, sys, time
#Don't forget to install this 2 packages with pip #pip install ...
import keyboard, mouse

#############################################################################################################################################################

#List of the key assign to the hotbar in QWERTY
listeKey = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

#Change keybind here
clickKey = "f4"
holdKey = "f6"
#Return to the menu
endKey = "esc"
#End program
exitKey = "f8"

#Change how fast "hold mode" switch between key. Careful when you are making a bigger value, you need to hold longer the key to escape. DO NOT PUT 0! 
timeSwitch = 0.1

#############################################################################################################################################################

#Pick one random slot of the hotbar
def random_pick():
    #Change the value to be between 0 and 9
    randomKey = random.randint(0,2)

    keyboard.send(listeKey[randomKey])

#When right click, change the slot
def click_mode():
    mouse.on_right_click(random_pick)
    if keyboard.wait(endKey):
        return

#Change constantly between differents slots
def hold_mode():
    while True:
        random_pick()
        time.sleep(timeSwitch)
        #Hold the button to exit correctly
        if keyboard.is_pressed(endKey):
            break

#End the program
def exit_mode():
    sys.exit()



#Main program need to hold the button for less than 0.1s to activate something
while True:
    try:
        time.sleep(0.1)
        if keyboard.is_pressed(clickKey):
                click_mode()
                mouse.unhook_all()
        if keyboard.is_pressed(holdKey):
                hold_mode()
        if keyboard.is_pressed(exitKey):
                exit_mode()
    except KeyboardInterrupt:
         print("End program")
         exit_mode()