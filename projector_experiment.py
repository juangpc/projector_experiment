from psychopy import visual, core
from random import *


numTrials = 200
min_isi_time = 1
max_isi_time = 2
white_screen_time = 2
trigger_on_value = 10
trigger_off_value = 5

stim_window = visual.Window(800, 600)

def send_trigger(value):
    pass

def isi():
    core.wait(uniform(min_isi_time, max_isi_time))

def screen():
    stim_window.color(1, 1, 1)
    stim_window.callOnFlip(send_trigger, trigger_on_value)
    stim_window.flip()
    core.wait(white_screen_time)
    stim_window.callOnFlip(send_trigger, trigger_off_value)
    stim_window.color(0, 0, 0)
    stim_window.flip()

def cleanup():
    stim_window.close()
    core.quit()

def stim_start():
    stim.window.fullscr = True
    for trial_i in range(numTrials):
        isi()
        screen()
    stim.window.fullscr = False
    cleanup()


if __name__ == "__main__":
    stim_start()
