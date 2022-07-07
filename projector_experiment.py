from psychopy import visual, core
from random import *


numTrials = 200
min_isi_time = 1
max_isi_time = 2
white_screen_time = 2
trigger_on_value = 10
trigger_off_value = 5

stim_window = visual.Window(800, 600)


def isi():
    core.wait(uniform(min_isi_time, max_isi_time))

def screen():
    # set color of window to white
    # send trigger on
    stim_window.flip()
    core.wait(white_screen_time)
    # send trigger off
    # set color of window black

def cleanup():
    win.close()
    core.quit()

def stim_start():
    for trial_i in range(numTrials):
        isi()
        screen()
    cleanup()


if __name__ == "__main__":
    stim_start()
