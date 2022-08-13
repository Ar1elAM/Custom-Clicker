from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import pyautogui
import threading
import random
import time

pyautogui.FAILSAFE = False
mouse_pos = [0]
mouse_time = [0]
button = Button.right
custom = False
delay = 0.5
print('After setting up hotkeys, the mouse will move to get screen limits.\nPlease don\'t move the mouse until you read "Done"\n')
set_XY_key = KeyCode(char=input("Please choose a key to set custom mouse positions:"))
start_stop_key = KeyCode(char=input("Please choose a key to start/stop mouse movement:"))
quit_key = KeyCode(char=input("Please choose a key to quit the program:"))

class AutoMouse(threading.Thread):

    def __init__(self, delay, button):
        super(AutoMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        x = 0
        global custom
        while (x <= 5):
            pyautogui.moveRel(0, 100)
            pyautogui.moveRel(-100, 0)
            pyautogui.moveRel(-4000, -3000)
            x += 1
        current_mouse_pos = mouse.position
        x_limit = (current_mouse_pos)
        x = 0
        while (x <= 5):
            pyautogui.moveRel(0, -100)
            pyautogui.moveRel(100, 0)
            pyautogui.moveRel(4000, 3000)
            x += 1
        current_mouse_pos = mouse.position
        y_limit = (current_mouse_pos)
        print("\nDone")
        while self.program_running:
            while self.running:
                if (custom == False):
                    r_timer = round(random.uniform(0.1, 10), 2)
                    time.sleep((r_timer/3))
                    r_x = random.randint(int(x_limit[0]), int(y_limit[0]))
                    r_y = random.randint(int(x_limit[1]), int(y_limit[1]))
                    print(r_x, r_y, r_timer)
                    timer = (r_timer)
                    pos_x = (r_x)
                    pos_y = (r_y)
                    pyautogui.moveTo(pos_x, pos_y)
                    time.sleep(r_timer)
                else:
                    x = 1
                    while(x<len(mouse_pos)):
                        pyautogui.click(mouse_pos[x])
                        time.sleep(mouse_time[x])
                        x+=1
                time.sleep(5)

mouse = Controller()
auto_thread = AutoMouse(delay, button)
auto_thread.start()

def key_press(key):
    # start_stop_key will stop clicking
    global custom
    #custom_in = custom
    if key == set_XY_key:
        if (custom == True):
            current_mouse_pos = mouse.position
            mouse_pos.append(current_mouse_pos)
            mouse_time.append(float(input("\nPlease choose a value(in seconds) for the time you wish to wait between actions:")))
            #print(mouse_pos)
        else:
            custom = True
            print("\nYou chose custom mode, this mode is useful for precise clicks positioning.\nJust hover your mouse where you want it to click, and press the ",set_XY_key," key, and type the amount of seconds you want it to wait.\nWhen ready just press the button you chose as " '"start button": ',start_stop_key, " key.")
    elif key == start_stop_key:
        if auto_thread.running:
            auto_thread.stop_clicking()
            custom = False
        else:
            auto_thread.start_clicking()
            print("\nAt any moment you can press the ", quit_key, " key to close the script, or the ", start_stop_key, " to stop.\nThe script will keep in loop until one of the previous keys are pressed\nThe program will stop when the set have finished.")
    elif key == quit_key:
        listener.stop()
        auto_thread.stop_clicking()
        auto_thread.exit()

with Listener(on_press=key_press) as listener:
    listener.join()