#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on November 20, 2025, at 16:32
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.5')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, iohub, hardware
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
import numpy as np
# Patch for np.str removal in newer NumPy versions
if not hasattr(np, 'str'):
    np.str = str



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'eyetrack_ibl'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, data.getDateStr(format="%Y_%b_%d_%H.%M.%S"))

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\LabProefpersoonPDC\\Desktop\\Code_19Nov\\WIN_cursor_ibl_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='labMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='add', useFBO=True, 
    units='pix')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup eyetracking
ioConfig['eyetracker.hw.mouse.EyeTracker'] = {
    'name': 'tracker',
    'controls': {
        'move': [],
        'blink':('MIDDLE_BUTTON',),
        'saccade_threshold': 0.5,
    }
}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, experiment_code='eyetrack_ibl', session_code=ioSession, datastore_name=filename, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "welcome" ---
welcome_position = visual.TextStim(win=win, name='welcome_position',
    text="Welcome to the experiment! \n\n\nMake sure that you can comfortably reach the mouse; you will not need the keyboard for now.\n\nIt is really important that you stay in the same position throughout the experiment. Do not move your head, your arms, or the chair. You can only move the mouse for the game.\n\nClick 'Continue' when you are ready.",
    font='Arial',
    units='height', pos=(0, 0.05), height=0.035, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
continue_txt = visual.TextStim(win=win, name='continue_txt',
    text='Continue',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
mouse_1 = event.Mouse(win=win)
x, y = [None, None]
mouse_1.mouseClock = core.Clock()

# --- Initialize components for Routine "setup_camera" ---
camera_info_txt = visual.TextStim(win=win, name='camera_info_txt',
    text="We will now set up the eye-tracking camera.\nThis will take just a couple minutes.\n\nA dot will appear on the screen at different locations.\nSimply move your eyes to follow the dot on the screen.\nPlease keep staring directly at the dot until it moves to a new location.\n\nClick 'Continue' to start the camera setup.",
    font='Arial',
    units='height', pos=(0, 0.05), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
continue_txt_17 = visual.TextStim(win=win, name='continue_txt_17',
    text='Continue',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
mouse_19 = event.Mouse(win=win)
x, y = [None, None]
mouse_19.mouseClock = core.Clock()
tobii_record = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start Only'
)
# Run 'Begin Experiment' code from eeg_set_up
import python_markers.marker_management as mark
import python_markers.GS_timing as timing

# Find the marker device. In the current example, a UsbParMarker is used.
# When the marker device is not found, an error is thrown.
device_info = mark.find_device(device_type='', fallback_to_fake=False)

# Initialize the marker_manager. Use the device_info obtained previously. In the
# current example, the task will not crash when a marker error occurs (see
# example.py for more info).
cur_device_type = device_info['device']['Device']
cur_device_address = device_info['com_port']
marker_manager = mark.MarkerManager(cur_device_type, cur_device_address, crash_on_marker_errors=False)

# Send a short pulse of 255 to check that markers are sent, then reset to 0.
marker_manager.set_value(255)
timing.delay(100)
marker_manager.set_value(0)
# Run 'Begin Experiment' code from code_tobii_start
from pylsl import local_clock


# --- Initialize components for Routine "demographics" ---
# Run 'Begin Experiment' code from mouse_visible_4
tot_points = 0
demogr_txt = visual.TextStim(win=win, name='demogr_txt',
    text='Thank you! The camera setup is done.\n\nWe will now ask you some information about your age, gender, and handedness.',
    font='Arial',
    units='height', pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
continue_txt_8 = visual.TextStim(win=win, name='continue_txt_8',
    text='Continue',
    font='Arial',
    units='height', pos=(0, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse_10 = event.Mouse(win=win)
x, y = [None, None]
mouse_10.mouseClock = core.Clock()

# --- Initialize components for Routine "age" ---
age_txt = visual.TextStim(win=win, name='age_txt',
    text="How old are you?\n\nClick on a number to select your age, then click 'Continue'. \nIf you prefer not to say, click 'Continue'.",
    font='Arial',
    units='deg', pos=(0, 5), height=0.75, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
age_slider = visual.Slider(win=win, name='age_slider',
    startValue=None, size=(35, 2), pos=(0, 0), units='deg',
    labels=[18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], ticks=(18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor=[0.8824, 0.9451, 1.0000], markerColor='white', lineColor='black', colorSpace='rgb',
    font='Arial', labelHeight=0.7,
    flip=False, ori=0.0, depth=-1, readOnly=False)
continue_txt_4 = visual.TextStim(win=win, name='continue_txt_4',
    text='Continue',
    font='Arial',
    units='deg', pos=(0, -5), height=0.75, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()

# --- Initialize components for Routine "gender" ---
gender_txt = visual.TextStim(win=win, name='gender_txt',
    text='What is your gender?',
    font='Arial',
    units='height', pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
woman = visual.TextStim(win=win, name='woman',
    text='Woman',
    font='Arial',
    units='height', pos=(-0.4, -0.1), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
man = visual.TextStim(win=win, name='man',
    text='Man',
    font='Arial',
    units='height', pos=(-0.15, -0.1), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
nonbinary = visual.TextStim(win=win, name='nonbinary',
    text='Non-binary',
    font='Arial',
    units='height', pos=(0.09, -0.1), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
other = visual.TextStim(win=win, name='other',
    text='Other/\nPrefer not to say',
    font='Arial',
    units='height', pos=(0.4, -0.1), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
mouse_5 = event.Mouse(win=win)
x, y = [None, None]
mouse_5.mouseClock = core.Clock()

# --- Initialize components for Routine "handedness" ---
handedness_txt = visual.TextStim(win=win, name='handedness_txt',
    text='Are you:',
    font='Arial',
    units='height', pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
right_hand = visual.TextStim(win=win, name='right_hand',
    text='Right-handed',
    font='Arial',
    units='height', pos=(-0.4, -0.1), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
left_hand = visual.TextStim(win=win, name='left_hand',
    text='Left-handed',
    font='Arial',
    units='height', pos=(0, -0.1), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
ambidx = visual.TextStim(win=win, name='ambidx',
    text='Other/\nPrefer not to say',
    font='Arial',
    units='height', pos=(0.4, -0.1), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
mouse_6 = event.Mouse(win=win)
x, y = [None, None]
mouse_6.mouseClock = core.Clock()

# --- Initialize components for Routine "pre_instr" ---
pre_instr_txt = visual.TextStim(win=win, name='pre_instr_txt',
    text="Thank you! We will now move on to the experiment.\n\nYou will take part in a computer game.\n\nYou will now see some written instructions, as well as two example images of what the stimuli look like.\n\nYou will then practice the game in a few example trials.\n\n\nClick 'Continue' to see the instructions.",
    font='Arial',
    units='height', pos=(0, 0.1), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
continue_txt_18 = visual.TextStim(win=win, name='continue_txt_18',
    text='Continue',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
mouse_22 = event.Mouse(win=win)
x, y = [None, None]
mouse_22.mouseClock = core.Clock()

# --- Initialize components for Routine "instructions_1" ---
# Run 'Begin Experiment' code from save_winsize
thisExp.addData("win_size", win.size)
instruction_txt = visual.TextStim(win=win, name='instruction_txt',
    text="The game consists of many trials. \n\nBefore each trial, you will see a blank gray screen. During this time you can blink as much as you need. You are not allowed to blink when the trial starts! You do not have to blink at each gray screen.\n\nAt the beginning of each trial you will hear a sharp beep. In each trial, you will see a red fixation point in the middle of the screen. After the beep, you see two target images appear on each side of the screen. \n\nClick 'Continue' to see more instructions and examples.",
    font='Arial',
    units='height', pos=(0, 0.1), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
continue_txt_2 = visual.TextStim(win=win, name='continue_txt_2',
    text='Continue',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

# --- Initialize components for Routine "instructions_2" ---
example_r = visual.ImageStim(
    win=win,
    name='example_r', units='height', 
    image='example right.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.1), size=(1.2, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
instruction_txt_2 = visual.TextStim(win=win, name='instruction_txt_2',
    text="On each trial, you must decide which of the two target images has the higher contrast (i.e., appears darker). \nTo select the target with the higher contrast, simply move the mouse until the chosen target reaches the center of the screen.\n\nFor example, in the image below, the right target has the higher contrast, so you would move your mouse to the left.\n\nClick 'Continue' to see more instructions and another example.",
    font='Arial',
    units='height', pos=(0, 0.3), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
continue_txt_9 = visual.TextStim(win=win, name='continue_txt_9',
    text='Continue',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse_11 = event.Mouse(win=win)
x, y = [None, None]
mouse_11.mouseClock = core.Clock()

# --- Initialize components for Routine "instructions_3" ---
example_l = visual.ImageStim(
    win=win,
    name='example_l', units='height', 
    image='example left.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.1), size=(1.2, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
instruction_txt_3 = visual.TextStim(win=win, name='instruction_txt_3',
    text="In this example image, the left target has the higher contrast, so you would move your mouse to the right.\n\nTo interact with the game, you will only need to move the mouse; clicking does not do anything.\n\nClick 'Continue' to see more instructions.",
    font='Arial',
    units='height', pos=(0, 0.3), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
continue_txt_10 = visual.TextStim(win=win, name='continue_txt_10',
    text='Continue',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse_12 = event.Mouse(win=win)
x, y = [None, None]
mouse_12.mouseClock = core.Clock()

# --- Initialize components for Routine "instructions_4" ---
instruction_txt_4 = visual.TextStim(win=win, name='instruction_txt_4',
    text="You will hear a high beep if you answer correctly.\nIf you answer incorrectly, you will hear a buzzing noise instead.\nIf you take too long to answer, you will hear a low beep.\n\nPlease try to be as accurate and fast as possible, and try not to let the trial time-out without a response.\n\n\nClick 'Continue' to see more instructions.",
    font='Arial',
    units='height', pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
continue_txt_11 = visual.TextStim(win=win, name='continue_txt_11',
    text='Continue',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
mouse_13 = event.Mouse(win=win)
x, y = [None, None]
mouse_13.mouseClock = core.Clock()

# --- Initialize components for Routine "instructions_5" ---
instruction_txt_5 = visual.TextStim(win=win, name='instruction_txt_5',
    text="Remember:\n- You can only blink during the blank grey screen.\n- You do not have to blink at every blank screen, but the screen has to be blank for you to blink!\n- You should not move your eyes when inspecting the images.\n- To inspect the image, please drag the images to the center of the screen.\n- Always keep your eyes on the red dot.\n- Keep as still as possible.\n\n\nClick 'Continue' to practice a few example trials.",
    font='Arial',
    units='height', pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
continue_txt_32 = visual.TextStim(win=win, name='continue_txt_32',
    text='Continue',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
mouse_36 = event.Mouse(win=win)
x, y = [None, None]
mouse_36.mouseClock = core.Clock()

# --- Initialize components for Routine "blink_practice" ---
# Run 'Begin Experiment' code from code_5
import random
blink_practice = 1.5
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "fix_practice" ---
# Run 'Begin Experiment' code from set_contrast_side_2
import random
fixation_tobii_practice = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
fixation_5 = visual.ImageStim(
    win=win,
    name='fixation_5', units='deg', 
    image='fixation_object.png', mask='circle', anchor='center',
    ori=0.0, pos=(0, 0), size=1.0,
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "trial_practice" ---
stimulus_onset_practice_tobii = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
# Run 'Begin Experiment' code from dragging_code_3
correct = 9
dot_3 = visual.ShapeStim(
    win=win, name='dot_3',units='pix', 
    size=(5, 5), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0],
    opacity=None, depth=-3.0, interpolate=True)
fixation_6 = visual.ImageStim(
    win=win,
    name='fixation_6', units='deg', 
    image='fixation_object.png', mask='circle', anchor='center',
    ori=0.0, pos=(0, 0), size=1.0,
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
grating_l_3 = visual.GratingStim(
    win=win, name='grating_l_3',units='pix', 
    tex='sin', mask='gauss', anchor='center',
    ori=0.0, pos=[0,0], size=(618, 618), sf=0.0073, phase=1.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
grating_r_3 = visual.GratingStim(
    win=win, name='grating_r_3',units='pix', 
    tex='sin', mask='gauss', anchor='center',
    ori=0.0, pos=[0,0], size=(618, 618), sf=0.0073, phase=1.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-6.0)
mouse_21 = event.Mouse(win=win)
x, y = [None, None]
mouse_21.mouseClock = core.Clock()
sound_trial_start_3 = sound.Sound('A', secs=0.1, stereo=True, hamming=True,
    name='sound_trial_start_3')
sound_trial_start_3.setVolume(0.1)
sound_no_resp_3 = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='sound_no_resp_3')
sound_no_resp_3.setVolume(0.1)
response_practice_tobii = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)

# --- Initialize components for Routine "feedback_practice" ---
feedback_practice_tobii = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
# Run 'Begin Experiment' code from feedback_code_2
fb_sound = 100
fb_dur = 10
fb_sound_dur = 5
fb_volume = 0.1
feedback_sound_2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='feedback_sound_2')
feedback_sound_2.setVolume(1.0)
fixation_7 = visual.ImageStim(
    win=win,
    name='fixation_7', units='deg', 
    image='fixation_object.png', mask='circle', anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "start_session" ---
end_practice_txt = visual.TextStim(win=win, name='end_practice_txt',
    text="That is the end of the practice trials.\n\nHere is a last reminder of the instructions:\n\nIn each trial, you will hear a beep and two targets will appear.\nYou must decide which target has the higher contrast.\nTo respond, move your mouse left or right to bring the chosen target into the middle of the screen. You don't need to click, simply drag the mouse.\n\nIf you are correct, you will hear a high beep; if you are incorrect, you will hear a buzzing noise.\n\nImportant: during the game you will see a red cross i the middle of the screen. Please try to keep your eyes fixated on this cross throughout the experiment.\n\nIf you have any questions, feel free to ask out loud, the experimenter can hear you and will help you out.\n\nClick 'Continue'.",
    font='Arial',
    units='height', pos=(0, 0.1), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
continue_txt_12 = visual.TextStim(win=win, name='continue_txt_12',
    text='Continue',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse_14 = event.Mouse(win=win)
x, y = [None, None]
mouse_14.mouseClock = core.Clock()

# --- Initialize components for Routine "start_reminder" ---
instruction_txt_6 = visual.TextStim(win=win, name='instruction_txt_6',
    text='Remember:\n- You can only blink during the blank grey screen.\n- You do not have to blink at every blank screen, but the screen has to be blank for you to blink!\n- You should not move your eyes when inspecting the images.\n- To inspect the image, please drag the images to the center of the screen.\n- Always keep your eyes on the red dot.\n- Keep as still as possible.\n\nYou will now start the real experiment. Good luck!',
    font='Arial',
    units='height', pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
continue_txt_33 = visual.TextStim(win=win, name='continue_txt_33',
    text='Start experiment',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse_37 = event.Mouse(win=win)
x, y = [None, None]
mouse_37.mouseClock = core.Clock()

# --- Initialize components for Routine "blink" ---
# Run 'Begin Experiment' code from code_6
import random
blink_trial = 1.0
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "fix" ---
fixation_tobii = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
fixation_2 = visual.ImageStim(
    win=win,
    name='fixation_2', units='deg', 
    image='fixation_object.png', mask='circle', anchor='center',
    ori=0.0, pos=(0, 0), size=1.0,
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "trial" ---
stimulus_onset_tobii = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
# Run 'Begin Experiment' code from dragging_code
correct = 9

dot = visual.ShapeStim(
    win=win, name='dot',units='pix', 
    size=(5, 5), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0],
    opacity=None, depth=-3.0, interpolate=True)
grating_l = visual.GratingStim(
    win=win, name='grating_l',units='pix', 
    tex='sin', mask='gauss', anchor='center',
    ori=0.0, pos=[0,0], size=(618, 618), sf=0.0073, phase=1.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
grating_r = visual.GratingStim(
    win=win, name='grating_r',units='pix', 
    tex='sin', mask='gauss', anchor='center',
    ori=0.0, pos=[0,0], size=(618, 618), sf=0.0073, phase=1.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
fixation = visual.ImageStim(
    win=win,
    name='fixation', units='deg', 
    image='fixation_object.png', mask='circle', anchor='center',
    ori=0.0, pos=(0, 0), size=1.0,
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
sound_trial_start = sound.Sound('A', secs=0.1, stereo=True, hamming=True,
    name='sound_trial_start')
sound_trial_start.setVolume(0.1)
sound_no_resp = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='sound_no_resp')
sound_no_resp.setVolume(0.1)
response_tobii = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)

# --- Initialize components for Routine "feedback" ---
feedback_tobii = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
# Run 'Begin Experiment' code from feedback_code
fb_sound = 100
fb_dur = 10
fb_sound_dur = 5
fb_volume = 0.1
feedback_sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='feedback_sound')
feedback_sound.setVolume(1.0)
fixation_3 = visual.ImageStim(
    win=win,
    name='fixation_3', units='deg', 
    image='fixation_object.png', mask='circle', anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "break_time" ---
end_practice_txt_2 = visual.TextStim(win=win, name='end_practice_txt_2',
    text='You are halfway done! \n\nYou will now get a short break. Please do not move or get up! \nThe purpose of this break is for us to check the equipment. \n\nYou will start the new trials once we ensure everything is okay. Please do not click anything until instructed to do so.\n\nThank you for your hard work so far!',
    font='Arial',
    units='height', pos=(0, 0.1), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
continue_txt_30 = visual.TextStim(win=win, name='continue_txt_30',
    text='Start experiment',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
mouse_34 = event.Mouse(win=win)
x, y = [None, None]
mouse_34.mouseClock = core.Clock()

# --- Initialize components for Routine "start_after_break" ---
end_practice_txt_3 = visual.TextStim(win=win, name='end_practice_txt_3',
    text="You will now start the second block.\n\nRemember:\n- You can only blink during the blank grey screen.\n- You do not have to blink at every blank screen, but the screen has to be blank for you to blink!\n- You should not move your eyes when inspecting the images.\n- To inspect the image, please drag the images to the center of the screen.\n- Always keep your eyes on the red dot.\n- Keep as still as possible.\n\nClick 'Continue' to start with the second block.",
    font='Arial',
    units='height', pos=(0, 0.1), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
continue_txt_31 = visual.TextStim(win=win, name='continue_txt_31',
    text='Continue',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
mouse_35 = event.Mouse(win=win)
x, y = [None, None]
mouse_35.mouseClock = core.Clock()

# --- Initialize components for Routine "blink" ---
# Run 'Begin Experiment' code from code_6
import random
blink_trial = 1.0
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "fix" ---
fixation_tobii = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
fixation_2 = visual.ImageStim(
    win=win,
    name='fixation_2', units='deg', 
    image='fixation_object.png', mask='circle', anchor='center',
    ori=0.0, pos=(0, 0), size=1.0,
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "trial" ---
stimulus_onset_tobii = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
# Run 'Begin Experiment' code from dragging_code
correct = 9

dot = visual.ShapeStim(
    win=win, name='dot',units='pix', 
    size=(5, 5), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0],
    opacity=None, depth=-3.0, interpolate=True)
grating_l = visual.GratingStim(
    win=win, name='grating_l',units='pix', 
    tex='sin', mask='gauss', anchor='center',
    ori=0.0, pos=[0,0], size=(618, 618), sf=0.0073, phase=1.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
grating_r = visual.GratingStim(
    win=win, name='grating_r',units='pix', 
    tex='sin', mask='gauss', anchor='center',
    ori=0.0, pos=[0,0], size=(618, 618), sf=0.0073, phase=1.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
fixation = visual.ImageStim(
    win=win,
    name='fixation', units='deg', 
    image='fixation_object.png', mask='circle', anchor='center',
    ori=0.0, pos=(0, 0), size=1.0,
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
sound_trial_start = sound.Sound('A', secs=0.1, stereo=True, hamming=True,
    name='sound_trial_start')
sound_trial_start.setVolume(0.1)
sound_no_resp = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='sound_no_resp')
sound_no_resp.setVolume(0.1)
response_tobii = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)

# --- Initialize components for Routine "feedback" ---
feedback_tobii = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
# Run 'Begin Experiment' code from feedback_code
fb_sound = 100
fb_dur = 10
fb_sound_dur = 5
fb_volume = 0.1
feedback_sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='feedback_sound')
feedback_sound.setVolume(1.0)
fixation_3 = visual.ImageStim(
    win=win,
    name='fixation_3', units='deg', 
    image='fixation_object.png', mask='circle', anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "record_delay" ---
blank_txt = visual.TextStim(win=win, name='blank_txt',
    text='wait...',
    font='Arial',
    units='height', pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color=[0.0000, 0.0000, 0.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "end_task" ---
end_task_txt = visual.TextStim(win=win, name='end_task_txt',
    text="That's the end of the game.\nThank you for participating! \n\nBefore we show you your final score, we will ask you a few questions about the game you just completed.\n\nYou no longer need to sit still. You can also blink freely now.\nPlease take the keyboard you see on the desk, and use it to type your answers. \n\nWhen answering questions, please do not press 'Enter' on the keyboard. Simply use punctuation to separate your sentences.\n\nClick 'Continue' to see the first question.",
    font='Arial',
    units='height', pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
continue_txt_22 = visual.TextStim(win=win, name='continue_txt_22',
    text='Continue',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
mouse_26 = event.Mouse(win=win)
x, y = [None, None]
mouse_26.mouseClock = core.Clock()
tobii_stop = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Stop Only'
)

# --- Initialize components for Routine "question1" ---
q1_txt = visual.TextStim(win=win, name='q1_txt',
    text="Please describe how you think the game worked\nand what you think the rules were.\n\nClick 'Continue' to see the next question.",
    font='Arial',
    units='height', pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
textbox1 = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),units='height',     letterHeight=0.03,
     size=(0.8, 0.5), borderWidth=0.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.02, alignment='top-left',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox1',
     autoLog=True,
)
continue_txt_23 = visual.TextStim(win=win, name='continue_txt_23',
    text='Continue',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse_27 = event.Mouse(win=win)
x, y = [None, None]
mouse_27.mouseClock = core.Clock()

# --- Initialize components for Routine "question2" ---
q2_txt = visual.TextStim(win=win, name='q2_txt',
    text="How well do you think you did in the game?\n\nClick 'Continue' to see the next question.",
    font='Arial',
    units='height', pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
textbox2 = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),units='height',     letterHeight=0.03,
     size=(0.8, 0.5), borderWidth=0.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.02, alignment='top-left',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox2',
     autoLog=True,
)
continue_txt_24 = visual.TextStim(win=win, name='continue_txt_24',
    text='Continue',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse_28 = event.Mouse(win=win)
x, y = [None, None]
mouse_28.mouseClock = core.Clock()

# --- Initialize components for Routine "question3" ---
q3_txt = visual.TextStim(win=win, name='q3_txt',
    text="What strategies did you use during the game?\n\nClick 'Continue' to see the next question.",
    font='Arial',
    units='height', pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
textbox3 = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),units='height',     letterHeight=0.03,
     size=(0.8, 0.5), borderWidth=0.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.02, alignment='top-left',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox3',
     autoLog=True,
)
continue_txt_25 = visual.TextStim(win=win, name='continue_txt_25',
    text='Continue',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse_29 = event.Mouse(win=win)
x, y = [None, None]
mouse_29.mouseClock = core.Clock()

# --- Initialize components for Routine "question4" ---
q4_txt = visual.TextStim(win=win, name='q4_txt',
    text="Did you notice any patterns in the game?\n\nClick 'Continue' to see the next question.",
    font='Arial',
    units='height', pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
textbox4 = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),units='height',     letterHeight=0.03,
     size=(0.8, 0.5), borderWidth=0.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.02, alignment='top-left',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox4',
     autoLog=True,
)
continue_txt_26 = visual.TextStim(win=win, name='continue_txt_26',
    text='Continue',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse_30 = event.Mouse(win=win)
x, y = [None, None]
mouse_30.mouseClock = core.Clock()

# --- Initialize components for Routine "question5" ---
q5_txt = visual.TextStim(win=win, name='q5_txt',
    text="Is there anything else you would like to add?\n\nClick 'Continue' when you are done.",
    font='Arial',
    units='height', pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
textbox5 = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),units='height',     letterHeight=0.03,
     size=(0.8, 0.5), borderWidth=0.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.02, alignment='top-left',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox5',
     autoLog=True,
)
continue_txt_29 = visual.TextStim(win=win, name='continue_txt_29',
    text='Continue',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse_33 = event.Mouse(win=win)
x, y = [None, None]
mouse_33.mouseClock = core.Clock()

# --- Initialize components for Routine "end_exp" ---
end_exp_txt = visual.TextStim(win=win, name='end_exp_txt',
    text='',
    font='Arial',
    units='height', pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
continue_txt_27 = visual.TextStim(win=win, name='continue_txt_27',
    text='Finish',
    font='Arial',
    units='height', pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='orange', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
mouse_31 = event.Mouse(win=win)
x, y = [None, None]
mouse_31.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_1
mouse_1.x = []
mouse_1.y = []
mouse_1.leftButton = []
mouse_1.midButton = []
mouse_1.rightButton = []
mouse_1.time = []
mouse_1.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
welcomeComponents = [welcome_position, continue_txt, mouse_1]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_position* updates
    if welcome_position.status == NOT_STARTED and frameN >= 0.0:
        # keep track of start time/frame for later
        welcome_position.frameNStart = frameN  # exact frame index
        welcome_position.tStart = t  # local t and not account for scr refresh
        welcome_position.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_position, 'tStartRefresh')  # time at next scr refresh
        welcome_position.setAutoDraw(True)
    
    # *continue_txt* updates
    if continue_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt.frameNStart = frameN  # exact frame index
        continue_txt.tStart = t  # local t and not account for scr refresh
        continue_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt.started')
        continue_txt.setAutoDraw(True)
    # *mouse_1* updates
    if mouse_1.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_1.frameNStart = frameN  # exact frame index
        mouse_1.tStart = t  # local t and not account for scr refresh
        mouse_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_1, 'tStartRefresh')  # time at next scr refresh
        mouse_1.status = STARTED
        mouse_1.mouseClock.reset()
        prevButtonState = mouse_1.getPressed()  # if button is down already this ISN'T a new click
    if mouse_1.status == STARTED:  # only update if started and not finished!
        buttons = mouse_1.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt)
                    clickableList = continue_txt
                except:
                    clickableList = [continue_txt]
                for obj in clickableList:
                    if obj.contains(mouse_1):
                        gotValidClick = True
                        mouse_1.clicked_name.append(obj.name)
                x, y = mouse_1.getPos()
                mouse_1.x.append(x)
                mouse_1.y.append(y)
                buttons = mouse_1.getPressed()
                mouse_1.leftButton.append(buttons[0])
                mouse_1.midButton.append(buttons[1])
                mouse_1.rightButton.append(buttons[2])
                mouse_1.time.append(mouse_1.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "welcome" ---
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_1.x', mouse_1.x)
thisExp.addData('mouse_1.y', mouse_1.y)
thisExp.addData('mouse_1.leftButton', mouse_1.leftButton)
thisExp.addData('mouse_1.midButton', mouse_1.midButton)
thisExp.addData('mouse_1.rightButton', mouse_1.rightButton)
thisExp.addData('mouse_1.time', mouse_1.time)
thisExp.addData('mouse_1.clicked_name', mouse_1.clicked_name)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "setup_camera" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_19
mouse_19.x = []
mouse_19.y = []
mouse_19.leftButton = []
mouse_19.midButton = []
mouse_19.rightButton = []
mouse_19.time = []
mouse_19.clicked_name = []
gotValidClick = False  # until a click is received
# Run 'Begin Routine' code from code_tobii_start
tobii_start_elapsed = globalClock.getTime()

tobii_start_lsl = local_clock()

thisExp.addData("tobii_record_start_elapsed", tobii_start_elapsed)
thisExp.addData("tobii_record_start_lsl", tobii_start_lsl)
# keep track of which components have finished
setup_cameraComponents = [camera_info_txt, continue_txt_17, mouse_19, tobii_record]
for thisComponent in setup_cameraComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "setup_camera" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *camera_info_txt* updates
    if camera_info_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        camera_info_txt.frameNStart = frameN  # exact frame index
        camera_info_txt.tStart = t  # local t and not account for scr refresh
        camera_info_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(camera_info_txt, 'tStartRefresh')  # time at next scr refresh
        camera_info_txt.setAutoDraw(True)
    
    # *continue_txt_17* updates
    if continue_txt_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_17.frameNStart = frameN  # exact frame index
        continue_txt_17.tStart = t  # local t and not account for scr refresh
        continue_txt_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_17, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_17.started')
        continue_txt_17.setAutoDraw(True)
    # *mouse_19* updates
    if mouse_19.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_19.frameNStart = frameN  # exact frame index
        mouse_19.tStart = t  # local t and not account for scr refresh
        mouse_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_19, 'tStartRefresh')  # time at next scr refresh
        mouse_19.status = STARTED
        mouse_19.mouseClock.reset()
        prevButtonState = mouse_19.getPressed()  # if button is down already this ISN'T a new click
    if mouse_19.status == STARTED:  # only update if started and not finished!
        buttons = mouse_19.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_17)
                    clickableList = continue_txt_17
                except:
                    clickableList = [continue_txt_17]
                for obj in clickableList:
                    if obj.contains(mouse_19):
                        gotValidClick = True
                        mouse_19.clicked_name.append(obj.name)
                x, y = mouse_19.getPos()
                mouse_19.x.append(x)
                mouse_19.y.append(y)
                buttons = mouse_19.getPressed()
                mouse_19.leftButton.append(buttons[0])
                mouse_19.midButton.append(buttons[1])
                mouse_19.rightButton.append(buttons[2])
                mouse_19.time.append(mouse_19.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    # *tobii_record* updates
    if tobii_record.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tobii_record.frameNStart = frameN  # exact frame index
        tobii_record.tStart = t  # local t and not account for scr refresh
        tobii_record.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tobii_record, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('tobii_record.started', t)
        tobii_record.status = STARTED
    if tobii_record.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tobii_record.tStartRefresh + 0-frameTolerance:
            # keep track of stop time/frame for later
            tobii_record.tStop = t  # not accounting for scr refresh
            tobii_record.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('tobii_record.stopped', t)
            tobii_record.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setup_cameraComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "setup_camera" ---
for thisComponent in setup_cameraComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_19.x', mouse_19.x)
thisExp.addData('mouse_19.y', mouse_19.y)
thisExp.addData('mouse_19.leftButton', mouse_19.leftButton)
thisExp.addData('mouse_19.midButton', mouse_19.midButton)
thisExp.addData('mouse_19.rightButton', mouse_19.rightButton)
thisExp.addData('mouse_19.time', mouse_19.time)
thisExp.addData('mouse_19.clicked_name', mouse_19.clicked_name)
thisExp.nextEntry()
# make sure the eyetracker recording stops
if tobii_record.status != FINISHED:
    tobii_record.status = FINISHED
# the Routine "setup_camera" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# define target for calibration
calibrationTarget = visual.TargetStim(win, 
    name='calibrationTarget',
    radius=10.0, fillColor='lime', borderColor='lime', lineWidth=10.0,
    innerRadius=3.0, innerFillColor='lime', innerBorderColor='lime', innerLineWidth=3.0,
    colorSpace='rgb', units=None
)
# define parameters for calibration
calibration = hardware.eyetracker.EyetrackerCalibration(win, 
    eyetracker, calibrationTarget,
    units=None, colorSpace='rgb',
    progressMode='time', targetDur=1.5, expandScale=1.5,
    targetLayout='THIRTEEN_POINTS', randomisePos=True, textColor='white',
    movementAnimation=True, targetDelay=1.0
)
# run calibration
calibration.run()
# clear any keypresses from during calibration so they don't interfere with the experiment
defaultKeyboard.clearEvents()
# the Routine "calibration" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# define target for validation
validationTarget = visual.TargetStim(win, 
    name='validationTarget',
    radius=10.0, fillColor='lime', borderColor='lime', lineWidth=10.0,
    innerRadius=3.0, innerFillColor='lime', innerBorderColor='lime', innerLineWidth=3.0,
    colorSpace='rgb', units=None
)
# define parameters for validation
validation = iohub.ValidationProcedure(win,
    target=validationTarget,
    gaze_cursor='green', 
    positions='THIRTEEN_POINTS', randomize_positions=True,
    expand_scale=1.5, target_duration=1.5,
    enable_position_animation=True, target_delay=1.0,
    progress_on_key=None, text_color='white',
    show_results_screen=True, save_results_screen=True,
    color_space='rgb', unit_type=None
)
# run validation
validation.run()
# clear any keypresses from during validation so they don't interfere with the experiment
defaultKeyboard.clearEvents()
# the Routine "validation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "demographics" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from mouse_visible_4
win.mouseVisible = True
# setup some python lists for storing info about the mouse_10
mouse_10.x = []
mouse_10.y = []
mouse_10.leftButton = []
mouse_10.midButton = []
mouse_10.rightButton = []
mouse_10.time = []
mouse_10.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
demographicsComponents = [demogr_txt, continue_txt_8, mouse_10]
for thisComponent in demographicsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "demographics" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *demogr_txt* updates
    if demogr_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demogr_txt.frameNStart = frameN  # exact frame index
        demogr_txt.tStart = t  # local t and not account for scr refresh
        demogr_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demogr_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'demogr_txt.started')
        demogr_txt.setAutoDraw(True)
    
    # *continue_txt_8* updates
    if continue_txt_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_8.frameNStart = frameN  # exact frame index
        continue_txt_8.tStart = t  # local t and not account for scr refresh
        continue_txt_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_8.started')
        continue_txt_8.setAutoDraw(True)
    # *mouse_10* updates
    if mouse_10.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_10.frameNStart = frameN  # exact frame index
        mouse_10.tStart = t  # local t and not account for scr refresh
        mouse_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_10, 'tStartRefresh')  # time at next scr refresh
        mouse_10.status = STARTED
        mouse_10.mouseClock.reset()
        prevButtonState = mouse_10.getPressed()  # if button is down already this ISN'T a new click
    if mouse_10.status == STARTED:  # only update if started and not finished!
        buttons = mouse_10.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_8)
                    clickableList = continue_txt_8
                except:
                    clickableList = [continue_txt_8]
                for obj in clickableList:
                    if obj.contains(mouse_10):
                        gotValidClick = True
                        mouse_10.clicked_name.append(obj.name)
                x, y = mouse_10.getPos()
                mouse_10.x.append(x)
                mouse_10.y.append(y)
                buttons = mouse_10.getPressed()
                mouse_10.leftButton.append(buttons[0])
                mouse_10.midButton.append(buttons[1])
                mouse_10.rightButton.append(buttons[2])
                mouse_10.time.append(mouse_10.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demographicsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "demographics" ---
for thisComponent in demographicsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_10.x', mouse_10.x)
thisExp.addData('mouse_10.y', mouse_10.y)
thisExp.addData('mouse_10.leftButton', mouse_10.leftButton)
thisExp.addData('mouse_10.midButton', mouse_10.midButton)
thisExp.addData('mouse_10.rightButton', mouse_10.rightButton)
thisExp.addData('mouse_10.time', mouse_10.time)
thisExp.addData('mouse_10.clicked_name', mouse_10.clicked_name)
thisExp.nextEntry()
# the Routine "demographics" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "age" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
age_slider.reset()
# setup some python lists for storing info about the mouse_4
mouse_4.x = []
mouse_4.y = []
mouse_4.leftButton = []
mouse_4.midButton = []
mouse_4.rightButton = []
mouse_4.time = []
mouse_4.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
ageComponents = [age_txt, age_slider, continue_txt_4, mouse_4]
for thisComponent in ageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "age" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *age_txt* updates
    if age_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        age_txt.frameNStart = frameN  # exact frame index
        age_txt.tStart = t  # local t and not account for scr refresh
        age_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(age_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'age_txt.started')
        age_txt.setAutoDraw(True)
    
    # *age_slider* updates
    if age_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        age_slider.frameNStart = frameN  # exact frame index
        age_slider.tStart = t  # local t and not account for scr refresh
        age_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(age_slider, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'age_slider.started')
        age_slider.setAutoDraw(True)
    
    # *continue_txt_4* updates
    if continue_txt_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_4.frameNStart = frameN  # exact frame index
        continue_txt_4.tStart = t  # local t and not account for scr refresh
        continue_txt_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_4.started')
        continue_txt_4.setAutoDraw(True)
    # *mouse_4* updates
    if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_4.frameNStart = frameN  # exact frame index
        mouse_4.tStart = t  # local t and not account for scr refresh
        mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
        mouse_4.status = STARTED
        mouse_4.mouseClock.reset()
        prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
    if mouse_4.status == STARTED:  # only update if started and not finished!
        buttons = mouse_4.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_4)
                    clickableList = continue_txt_4
                except:
                    clickableList = [continue_txt_4]
                for obj in clickableList:
                    if obj.contains(mouse_4):
                        gotValidClick = True
                        mouse_4.clicked_name.append(obj.name)
                x, y = mouse_4.getPos()
                mouse_4.x.append(x)
                mouse_4.y.append(y)
                buttons = mouse_4.getPressed()
                mouse_4.leftButton.append(buttons[0])
                mouse_4.midButton.append(buttons[1])
                mouse_4.rightButton.append(buttons[2])
                mouse_4.time.append(mouse_4.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "age" ---
for thisComponent in ageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('age_slider.response', age_slider.getRating())
thisExp.addData('age_slider.rt', age_slider.getRT())
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_4.x', mouse_4.x)
thisExp.addData('mouse_4.y', mouse_4.y)
thisExp.addData('mouse_4.leftButton', mouse_4.leftButton)
thisExp.addData('mouse_4.midButton', mouse_4.midButton)
thisExp.addData('mouse_4.rightButton', mouse_4.rightButton)
thisExp.addData('mouse_4.time', mouse_4.time)
thisExp.addData('mouse_4.clicked_name', mouse_4.clicked_name)
thisExp.nextEntry()
# the Routine "age" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "gender" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_5
mouse_5.x = []
mouse_5.y = []
mouse_5.leftButton = []
mouse_5.midButton = []
mouse_5.rightButton = []
mouse_5.time = []
mouse_5.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
genderComponents = [gender_txt, woman, man, nonbinary, other, mouse_5]
for thisComponent in genderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "gender" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *gender_txt* updates
    if gender_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gender_txt.frameNStart = frameN  # exact frame index
        gender_txt.tStart = t  # local t and not account for scr refresh
        gender_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gender_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'gender_txt.started')
        gender_txt.setAutoDraw(True)
    
    # *woman* updates
    if woman.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        woman.frameNStart = frameN  # exact frame index
        woman.tStart = t  # local t and not account for scr refresh
        woman.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(woman, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'woman.started')
        woman.setAutoDraw(True)
    
    # *man* updates
    if man.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        man.frameNStart = frameN  # exact frame index
        man.tStart = t  # local t and not account for scr refresh
        man.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(man, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'man.started')
        man.setAutoDraw(True)
    
    # *nonbinary* updates
    if nonbinary.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nonbinary.frameNStart = frameN  # exact frame index
        nonbinary.tStart = t  # local t and not account for scr refresh
        nonbinary.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nonbinary, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'nonbinary.started')
        nonbinary.setAutoDraw(True)
    
    # *other* updates
    if other.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        other.frameNStart = frameN  # exact frame index
        other.tStart = t  # local t and not account for scr refresh
        other.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(other, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'other.started')
        other.setAutoDraw(True)
    # *mouse_5* updates
    if mouse_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_5.frameNStart = frameN  # exact frame index
        mouse_5.tStart = t  # local t and not account for scr refresh
        mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_5, 'tStartRefresh')  # time at next scr refresh
        mouse_5.status = STARTED
        mouse_5.mouseClock.reset()
        prevButtonState = mouse_5.getPressed()  # if button is down already this ISN'T a new click
    if mouse_5.status == STARTED:  # only update if started and not finished!
        buttons = mouse_5.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([woman, man, nonbinary, other])
                    clickableList = [woman, man, nonbinary, other]
                except:
                    clickableList = [[woman, man, nonbinary, other]]
                for obj in clickableList:
                    if obj.contains(mouse_5):
                        gotValidClick = True
                        mouse_5.clicked_name.append(obj.name)
                x, y = mouse_5.getPos()
                mouse_5.x.append(x)
                mouse_5.y.append(y)
                buttons = mouse_5.getPressed()
                mouse_5.leftButton.append(buttons[0])
                mouse_5.midButton.append(buttons[1])
                mouse_5.rightButton.append(buttons[2])
                mouse_5.time.append(mouse_5.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in genderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "gender" ---
for thisComponent in genderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_5.x', mouse_5.x)
thisExp.addData('mouse_5.y', mouse_5.y)
thisExp.addData('mouse_5.leftButton', mouse_5.leftButton)
thisExp.addData('mouse_5.midButton', mouse_5.midButton)
thisExp.addData('mouse_5.rightButton', mouse_5.rightButton)
thisExp.addData('mouse_5.time', mouse_5.time)
thisExp.addData('mouse_5.clicked_name', mouse_5.clicked_name)
thisExp.nextEntry()
# the Routine "gender" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "handedness" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_6
mouse_6.x = []
mouse_6.y = []
mouse_6.leftButton = []
mouse_6.midButton = []
mouse_6.rightButton = []
mouse_6.time = []
mouse_6.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
handednessComponents = [handedness_txt, right_hand, left_hand, ambidx, mouse_6]
for thisComponent in handednessComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "handedness" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *handedness_txt* updates
    if handedness_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        handedness_txt.frameNStart = frameN  # exact frame index
        handedness_txt.tStart = t  # local t and not account for scr refresh
        handedness_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(handedness_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'handedness_txt.started')
        handedness_txt.setAutoDraw(True)
    
    # *right_hand* updates
    if right_hand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        right_hand.frameNStart = frameN  # exact frame index
        right_hand.tStart = t  # local t and not account for scr refresh
        right_hand.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(right_hand, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'right_hand.started')
        right_hand.setAutoDraw(True)
    
    # *left_hand* updates
    if left_hand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        left_hand.frameNStart = frameN  # exact frame index
        left_hand.tStart = t  # local t and not account for scr refresh
        left_hand.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(left_hand, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'left_hand.started')
        left_hand.setAutoDraw(True)
    
    # *ambidx* updates
    if ambidx.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ambidx.frameNStart = frameN  # exact frame index
        ambidx.tStart = t  # local t and not account for scr refresh
        ambidx.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ambidx, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ambidx.started')
        ambidx.setAutoDraw(True)
    # *mouse_6* updates
    if mouse_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_6.frameNStart = frameN  # exact frame index
        mouse_6.tStart = t  # local t and not account for scr refresh
        mouse_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_6, 'tStartRefresh')  # time at next scr refresh
        mouse_6.status = STARTED
        mouse_6.mouseClock.reset()
        prevButtonState = mouse_6.getPressed()  # if button is down already this ISN'T a new click
    if mouse_6.status == STARTED:  # only update if started and not finished!
        buttons = mouse_6.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([right_hand, left_hand, ambidx])
                    clickableList = [right_hand, left_hand, ambidx]
                except:
                    clickableList = [[right_hand, left_hand, ambidx]]
                for obj in clickableList:
                    if obj.contains(mouse_6):
                        gotValidClick = True
                        mouse_6.clicked_name.append(obj.name)
                x, y = mouse_6.getPos()
                mouse_6.x.append(x)
                mouse_6.y.append(y)
                buttons = mouse_6.getPressed()
                mouse_6.leftButton.append(buttons[0])
                mouse_6.midButton.append(buttons[1])
                mouse_6.rightButton.append(buttons[2])
                mouse_6.time.append(mouse_6.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in handednessComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "handedness" ---
for thisComponent in handednessComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_6.x', mouse_6.x)
thisExp.addData('mouse_6.y', mouse_6.y)
thisExp.addData('mouse_6.leftButton', mouse_6.leftButton)
thisExp.addData('mouse_6.midButton', mouse_6.midButton)
thisExp.addData('mouse_6.rightButton', mouse_6.rightButton)
thisExp.addData('mouse_6.time', mouse_6.time)
thisExp.addData('mouse_6.clicked_name', mouse_6.clicked_name)
thisExp.nextEntry()
# the Routine "handedness" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "pre_instr" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_22
mouse_22.x = []
mouse_22.y = []
mouse_22.leftButton = []
mouse_22.midButton = []
mouse_22.rightButton = []
mouse_22.time = []
mouse_22.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
pre_instrComponents = [pre_instr_txt, continue_txt_18, mouse_22]
for thisComponent in pre_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "pre_instr" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pre_instr_txt* updates
    if pre_instr_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pre_instr_txt.frameNStart = frameN  # exact frame index
        pre_instr_txt.tStart = t  # local t and not account for scr refresh
        pre_instr_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pre_instr_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pre_instr_txt.started')
        pre_instr_txt.setAutoDraw(True)
    
    # *continue_txt_18* updates
    if continue_txt_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_18.frameNStart = frameN  # exact frame index
        continue_txt_18.tStart = t  # local t and not account for scr refresh
        continue_txt_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_18, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_18.started')
        continue_txt_18.setAutoDraw(True)
    # *mouse_22* updates
    if mouse_22.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_22.frameNStart = frameN  # exact frame index
        mouse_22.tStart = t  # local t and not account for scr refresh
        mouse_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_22, 'tStartRefresh')  # time at next scr refresh
        mouse_22.status = STARTED
        mouse_22.mouseClock.reset()
        prevButtonState = mouse_22.getPressed()  # if button is down already this ISN'T a new click
    if mouse_22.status == STARTED:  # only update if started and not finished!
        buttons = mouse_22.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_18)
                    clickableList = continue_txt_18
                except:
                    clickableList = [continue_txt_18]
                for obj in clickableList:
                    if obj.contains(mouse_22):
                        gotValidClick = True
                        mouse_22.clicked_name.append(obj.name)
                x, y = mouse_22.getPos()
                mouse_22.x.append(x)
                mouse_22.y.append(y)
                buttons = mouse_22.getPressed()
                mouse_22.leftButton.append(buttons[0])
                mouse_22.midButton.append(buttons[1])
                mouse_22.rightButton.append(buttons[2])
                mouse_22.time.append(mouse_22.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pre_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "pre_instr" ---
for thisComponent in pre_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_22.x', mouse_22.x)
thisExp.addData('mouse_22.y', mouse_22.y)
thisExp.addData('mouse_22.leftButton', mouse_22.leftButton)
thisExp.addData('mouse_22.midButton', mouse_22.midButton)
thisExp.addData('mouse_22.rightButton', mouse_22.rightButton)
thisExp.addData('mouse_22.time', mouse_22.time)
thisExp.addData('mouse_22.clicked_name', mouse_22.clicked_name)
thisExp.nextEntry()
# the Routine "pre_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_2
mouse_2.x = []
mouse_2.y = []
mouse_2.leftButton = []
mouse_2.midButton = []
mouse_2.rightButton = []
mouse_2.time = []
mouse_2.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructions_1Components = [instruction_txt, continue_txt_2, mouse_2]
for thisComponent in instructions_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_txt* updates
    if instruction_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_txt.frameNStart = frameN  # exact frame index
        instruction_txt.tStart = t  # local t and not account for scr refresh
        instruction_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instruction_txt.started')
        instruction_txt.setAutoDraw(True)
    
    # *continue_txt_2* updates
    if continue_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_2.frameNStart = frameN  # exact frame index
        continue_txt_2.tStart = t  # local t and not account for scr refresh
        continue_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_2.started')
        continue_txt_2.setAutoDraw(True)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_2)
                    clickableList = continue_txt_2
                except:
                    clickableList = [continue_txt_2]
                for obj in clickableList:
                    if obj.contains(mouse_2):
                        gotValidClick = True
                        mouse_2.clicked_name.append(obj.name)
                x, y = mouse_2.getPos()
                mouse_2.x.append(x)
                mouse_2.y.append(y)
                buttons = mouse_2.getPressed()
                mouse_2.leftButton.append(buttons[0])
                mouse_2.midButton.append(buttons[1])
                mouse_2.rightButton.append(buttons[2])
                mouse_2.time.append(mouse_2.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_1" ---
for thisComponent in instructions_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from save_winsize
thisExp.addData('session_start', core.getTime())
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_2.x', mouse_2.x)
thisExp.addData('mouse_2.y', mouse_2.y)
thisExp.addData('mouse_2.leftButton', mouse_2.leftButton)
thisExp.addData('mouse_2.midButton', mouse_2.midButton)
thisExp.addData('mouse_2.rightButton', mouse_2.rightButton)
thisExp.addData('mouse_2.time', mouse_2.time)
thisExp.addData('mouse_2.clicked_name', mouse_2.clicked_name)
thisExp.nextEntry()
# the Routine "instructions_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_11
mouse_11.x = []
mouse_11.y = []
mouse_11.leftButton = []
mouse_11.midButton = []
mouse_11.rightButton = []
mouse_11.time = []
mouse_11.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructions_2Components = [example_r, instruction_txt_2, continue_txt_9, mouse_11]
for thisComponent in instructions_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *example_r* updates
    if example_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        example_r.frameNStart = frameN  # exact frame index
        example_r.tStart = t  # local t and not account for scr refresh
        example_r.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(example_r, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'example_r.started')
        example_r.setAutoDraw(True)
    
    # *instruction_txt_2* updates
    if instruction_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_txt_2.frameNStart = frameN  # exact frame index
        instruction_txt_2.tStart = t  # local t and not account for scr refresh
        instruction_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_txt_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instruction_txt_2.started')
        instruction_txt_2.setAutoDraw(True)
    
    # *continue_txt_9* updates
    if continue_txt_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_9.frameNStart = frameN  # exact frame index
        continue_txt_9.tStart = t  # local t and not account for scr refresh
        continue_txt_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_9.started')
        continue_txt_9.setAutoDraw(True)
    # *mouse_11* updates
    if mouse_11.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_11.frameNStart = frameN  # exact frame index
        mouse_11.tStart = t  # local t and not account for scr refresh
        mouse_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_11, 'tStartRefresh')  # time at next scr refresh
        mouse_11.status = STARTED
        mouse_11.mouseClock.reset()
        prevButtonState = mouse_11.getPressed()  # if button is down already this ISN'T a new click
    if mouse_11.status == STARTED:  # only update if started and not finished!
        buttons = mouse_11.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_9)
                    clickableList = continue_txt_9
                except:
                    clickableList = [continue_txt_9]
                for obj in clickableList:
                    if obj.contains(mouse_11):
                        gotValidClick = True
                        mouse_11.clicked_name.append(obj.name)
                x, y = mouse_11.getPos()
                mouse_11.x.append(x)
                mouse_11.y.append(y)
                buttons = mouse_11.getPressed()
                mouse_11.leftButton.append(buttons[0])
                mouse_11.midButton.append(buttons[1])
                mouse_11.rightButton.append(buttons[2])
                mouse_11.time.append(mouse_11.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_2" ---
for thisComponent in instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_11.x', mouse_11.x)
thisExp.addData('mouse_11.y', mouse_11.y)
thisExp.addData('mouse_11.leftButton', mouse_11.leftButton)
thisExp.addData('mouse_11.midButton', mouse_11.midButton)
thisExp.addData('mouse_11.rightButton', mouse_11.rightButton)
thisExp.addData('mouse_11.time', mouse_11.time)
thisExp.addData('mouse_11.clicked_name', mouse_11.clicked_name)
thisExp.nextEntry()
# the Routine "instructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions_3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_12
mouse_12.x = []
mouse_12.y = []
mouse_12.leftButton = []
mouse_12.midButton = []
mouse_12.rightButton = []
mouse_12.time = []
mouse_12.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructions_3Components = [example_l, instruction_txt_3, continue_txt_10, mouse_12]
for thisComponent in instructions_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *example_l* updates
    if example_l.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        example_l.frameNStart = frameN  # exact frame index
        example_l.tStart = t  # local t and not account for scr refresh
        example_l.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(example_l, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'example_l.started')
        example_l.setAutoDraw(True)
    
    # *instruction_txt_3* updates
    if instruction_txt_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_txt_3.frameNStart = frameN  # exact frame index
        instruction_txt_3.tStart = t  # local t and not account for scr refresh
        instruction_txt_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_txt_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instruction_txt_3.started')
        instruction_txt_3.setAutoDraw(True)
    
    # *continue_txt_10* updates
    if continue_txt_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_10.frameNStart = frameN  # exact frame index
        continue_txt_10.tStart = t  # local t and not account for scr refresh
        continue_txt_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_10, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_10.started')
        continue_txt_10.setAutoDraw(True)
    # *mouse_12* updates
    if mouse_12.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_12.frameNStart = frameN  # exact frame index
        mouse_12.tStart = t  # local t and not account for scr refresh
        mouse_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_12, 'tStartRefresh')  # time at next scr refresh
        mouse_12.status = STARTED
        mouse_12.mouseClock.reset()
        prevButtonState = mouse_12.getPressed()  # if button is down already this ISN'T a new click
    if mouse_12.status == STARTED:  # only update if started and not finished!
        buttons = mouse_12.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_10)
                    clickableList = continue_txt_10
                except:
                    clickableList = [continue_txt_10]
                for obj in clickableList:
                    if obj.contains(mouse_12):
                        gotValidClick = True
                        mouse_12.clicked_name.append(obj.name)
                x, y = mouse_12.getPos()
                mouse_12.x.append(x)
                mouse_12.y.append(y)
                buttons = mouse_12.getPressed()
                mouse_12.leftButton.append(buttons[0])
                mouse_12.midButton.append(buttons[1])
                mouse_12.rightButton.append(buttons[2])
                mouse_12.time.append(mouse_12.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_3" ---
for thisComponent in instructions_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_12.x', mouse_12.x)
thisExp.addData('mouse_12.y', mouse_12.y)
thisExp.addData('mouse_12.leftButton', mouse_12.leftButton)
thisExp.addData('mouse_12.midButton', mouse_12.midButton)
thisExp.addData('mouse_12.rightButton', mouse_12.rightButton)
thisExp.addData('mouse_12.time', mouse_12.time)
thisExp.addData('mouse_12.clicked_name', mouse_12.clicked_name)
thisExp.nextEntry()
# the Routine "instructions_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions_4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_13
mouse_13.x = []
mouse_13.y = []
mouse_13.leftButton = []
mouse_13.midButton = []
mouse_13.rightButton = []
mouse_13.time = []
mouse_13.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructions_4Components = [instruction_txt_4, continue_txt_11, mouse_13]
for thisComponent in instructions_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_txt_4* updates
    if instruction_txt_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_txt_4.frameNStart = frameN  # exact frame index
        instruction_txt_4.tStart = t  # local t and not account for scr refresh
        instruction_txt_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_txt_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instruction_txt_4.started')
        instruction_txt_4.setAutoDraw(True)
    
    # *continue_txt_11* updates
    if continue_txt_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_11.frameNStart = frameN  # exact frame index
        continue_txt_11.tStart = t  # local t and not account for scr refresh
        continue_txt_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_11, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_11.started')
        continue_txt_11.setAutoDraw(True)
    # *mouse_13* updates
    if mouse_13.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_13.frameNStart = frameN  # exact frame index
        mouse_13.tStart = t  # local t and not account for scr refresh
        mouse_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_13, 'tStartRefresh')  # time at next scr refresh
        mouse_13.status = STARTED
        mouse_13.mouseClock.reset()
        prevButtonState = mouse_13.getPressed()  # if button is down already this ISN'T a new click
    if mouse_13.status == STARTED:  # only update if started and not finished!
        buttons = mouse_13.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_11)
                    clickableList = continue_txt_11
                except:
                    clickableList = [continue_txt_11]
                for obj in clickableList:
                    if obj.contains(mouse_13):
                        gotValidClick = True
                        mouse_13.clicked_name.append(obj.name)
                x, y = mouse_13.getPos()
                mouse_13.x.append(x)
                mouse_13.y.append(y)
                buttons = mouse_13.getPressed()
                mouse_13.leftButton.append(buttons[0])
                mouse_13.midButton.append(buttons[1])
                mouse_13.rightButton.append(buttons[2])
                mouse_13.time.append(mouse_13.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_4" ---
for thisComponent in instructions_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_13.x', mouse_13.x)
thisExp.addData('mouse_13.y', mouse_13.y)
thisExp.addData('mouse_13.leftButton', mouse_13.leftButton)
thisExp.addData('mouse_13.midButton', mouse_13.midButton)
thisExp.addData('mouse_13.rightButton', mouse_13.rightButton)
thisExp.addData('mouse_13.time', mouse_13.time)
thisExp.addData('mouse_13.clicked_name', mouse_13.clicked_name)
thisExp.nextEntry()
# the Routine "instructions_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions_5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_36
mouse_36.x = []
mouse_36.y = []
mouse_36.leftButton = []
mouse_36.midButton = []
mouse_36.rightButton = []
mouse_36.time = []
mouse_36.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructions_5Components = [instruction_txt_5, continue_txt_32, mouse_36]
for thisComponent in instructions_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_5" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_txt_5* updates
    if instruction_txt_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_txt_5.frameNStart = frameN  # exact frame index
        instruction_txt_5.tStart = t  # local t and not account for scr refresh
        instruction_txt_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_txt_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instruction_txt_5.started')
        instruction_txt_5.setAutoDraw(True)
    
    # *continue_txt_32* updates
    if continue_txt_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_32.frameNStart = frameN  # exact frame index
        continue_txt_32.tStart = t  # local t and not account for scr refresh
        continue_txt_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_32, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_32.started')
        continue_txt_32.setAutoDraw(True)
    # *mouse_36* updates
    if mouse_36.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_36.frameNStart = frameN  # exact frame index
        mouse_36.tStart = t  # local t and not account for scr refresh
        mouse_36.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_36, 'tStartRefresh')  # time at next scr refresh
        mouse_36.status = STARTED
        mouse_36.mouseClock.reset()
        prevButtonState = mouse_36.getPressed()  # if button is down already this ISN'T a new click
    if mouse_36.status == STARTED:  # only update if started and not finished!
        buttons = mouse_36.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_11)
                    clickableList = continue_txt_11
                except:
                    clickableList = [continue_txt_11]
                for obj in clickableList:
                    if obj.contains(mouse_36):
                        gotValidClick = True
                        mouse_36.clicked_name.append(obj.name)
                x, y = mouse_36.getPos()
                mouse_36.x.append(x)
                mouse_36.y.append(y)
                buttons = mouse_36.getPressed()
                mouse_36.leftButton.append(buttons[0])
                mouse_36.midButton.append(buttons[1])
                mouse_36.rightButton.append(buttons[2])
                mouse_36.time.append(mouse_36.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_5" ---
for thisComponent in instructions_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_36.x', mouse_36.x)
thisExp.addData('mouse_36.y', mouse_36.y)
thisExp.addData('mouse_36.leftButton', mouse_36.leftButton)
thisExp.addData('mouse_36.midButton', mouse_36.midButton)
thisExp.addData('mouse_36.rightButton', mouse_36.rightButton)
thisExp.addData('mouse_36.time', mouse_36.time)
thisExp.addData('mouse_36.clicked_name', mouse_36.clicked_name)
thisExp.nextEntry()
# the Routine "instructions_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pregen_sequence_' + str(int(expInfo['participant'][-1])) + '.xlsx', selection='36:41'),
    seed=None, name='practice')
thisExp.addLoop(practice)  # add the loop to the experiment
thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in practice:
    currentLoop = practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "blink_practice" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_7
    marker_manager.set_value(5)
    timing.delay(100)
    marker_manager.set_value(0)
    
    # Run 'Begin Routine' code from code_5
    blink_practice = random.uniform(1.0, 2.0)
    
    text_2.setText('')
    # keep track of which components have finished
    blink_practiceComponents = [text_2]
    for thisComponent in blink_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blink_practice" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + blink_practice-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.stopped')
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blink_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blink_practice" ---
    for thisComponent in blink_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "blink_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "fix_practice" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from start_trial_practice
    marker_manager.set_value(10)
    timing.delay(100)
    marker_manager.set_value(0)
    
    
    # Run 'Begin Routine' code from mouse_visible_5
    win.mouseVisible = False
    mouse.setPos(newPos=(0, 0))
    # Run 'Begin Routine' code from set_contrast_side_2
    if eccentricity == -15:
        leftCont = baseContrast+contrastDelta
        rightCont = baseContrast
    elif eccentricity == 15:
        leftCont = baseContrast
        rightCont = baseContrast+contrastDelta
    
    signed_contrast=rightCont-leftCont
    
    
    # Save all these variables to the log
    thisExp.addData("signed_contrast", signed_contrast)
    thisExp.addData("leftCont", leftCont)
    thisExp.addData("rightCont", rightCont)
    fixation_5.setColor([1,1,1], colorSpace='rgb')
    fixation_5.setSize((0.75, 0.75))
    # Run 'Begin Routine' code from code_2
    fixation_start_elapsed = globalClock.getTime()      # seconds since experiment start
    fixation_start_lsl = local_clock()                  # LSL-aligned time
    thisExp.addData("fixation_tobii_start_elapsed", fixation_start_elapsed)
    thisExp.addData("fixation_tobii_start_lsl", fixation_start_lsl)
    # keep track of which components have finished
    fix_practiceComponents = [fixation_tobii_practice, fixation_5]
    for thisComponent in fix_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fix_practice" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from mouse_visible_5
        mouse.setPos(newPos=(0, 0))
        # *fixation_tobii_practice* updates
        if fixation_tobii_practice.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_tobii_practice.frameNStart = frameN  # exact frame index
            fixation_tobii_practice.tStart = t  # local t and not account for scr refresh
            fixation_tobii_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_tobii_practice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('fixation_tobii_practice.started', t)
            fixation_tobii_practice.status = STARTED
        if fixation_tobii_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_tobii_practice.tStartRefresh + q-frameTolerance:
                # keep track of stop time/frame for later
                fixation_tobii_practice.tStop = t  # not accounting for scr refresh
                fixation_tobii_practice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('fixation_tobii_practice.stopped', t)
                fixation_tobii_practice.status = FINISHED
        
        # *fixation_5* updates
        if fixation_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_5.frameNStart = frameN  # exact frame index
            fixation_5.tStart = t  # local t and not account for scr refresh
            fixation_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_5.started')
            fixation_5.setAutoDraw(True)
        if fixation_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_5.tStartRefresh + q-frameTolerance:
                # keep track of stop time/frame for later
                fixation_5.tStop = t  # not accounting for scr refresh
                fixation_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_5.stopped')
                fixation_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fix_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fix_practice" ---
    for thisComponent in fix_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if fixation_tobii_practice.status != FINISHED:
        fixation_tobii_practice.status = FINISHED
    # Run 'End Routine' code from code_2
    fixation_stop_elapsed = globalClock.getTime()
    fixation_stop_lsl = local_clock()
    
    # Save to data file
    thisExp.addData("fixation_tobii_stop_elapsed", fixation_stop_elapsed)
    thisExp.addData("fixation_tobii_stop_lsl", fixation_stop_lsl)
    # the Routine "fix_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial_practice" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from stimulus_onset_practice
    signed_contrast=rightCont-leftCont
    contrast_marker = 150 + round((signed_contrast/0.2)*50)
    
    marker_manager.set_value(contrast_marker)
    timing.delay(100)
    marker_manager.set_value(0)
    
    
    # Run 'Begin Routine' code from dragging_code_3
    mouse_21.setPos(newPos=(0, 0))
    
    r_lim_corr = 0.05
    l_lim_corr = -0.05
    r_lim_wrong = 1236
    l_lim_wrong = -1236
    
    mouserec = mouse_21.getPos()
    moved = False
    
    dot_trajectory = []
    
    trial_start = globalClock.getTime()
    trial_start_lsl = local_clock()
    thisExp.addData("trial_start_elapsed", trial_start)
    thisExp.addData("trial_start_lsl", trial_start_lsl)
    dot_3.setPos((618, 0))
    fixation_6.setColor([0,0,0], colorSpace='rgb')
    fixation_6.setSize((0.75, 0.75))
    grating_l_3.setContrast(leftCont)
    grating_l_3.setPos((-618, 0))
    grating_l_3.setPhase(random.random()*360)
    grating_r_3.setContrast(rightCont)
    grating_r_3.setPos((618, 0))
    grating_r_3.setPhase(random.random()*360)
    # setup some python lists for storing info about the mouse_21
    mouse_21.x = []
    mouse_21.y = []
    mouse_21.leftButton = []
    mouse_21.midButton = []
    mouse_21.rightButton = []
    mouse_21.time = []
    gotValidClick = False  # until a click is received
    sound_trial_start_3.setSound('5000', secs=0.1, hamming=True)
    sound_trial_start_3.setVolume(0.1, log=False)
    sound_no_resp_3.setSound('567', secs=0.5, hamming=True)
    sound_no_resp_3.setVolume(0.1, log=False)
    # keep track of which components have finished
    trial_practiceComponents = [stimulus_onset_practice_tobii, dot_3, fixation_6, grating_l_3, grating_r_3, mouse_21, sound_trial_start_3, sound_no_resp_3, response_practice_tobii]
    for thisComponent in trial_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial_practice" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *stimulus_onset_practice_tobii* updates
        if stimulus_onset_practice_tobii.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimulus_onset_practice_tobii.frameNStart = frameN  # exact frame index
            stimulus_onset_practice_tobii.tStart = t  # local t and not account for scr refresh
            stimulus_onset_practice_tobii.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimulus_onset_practice_tobii, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('stimulus_onset_practice_tobii.started', t)
            stimulus_onset_practice_tobii.status = STARTED
        if stimulus_onset_practice_tobii.status == STARTED:
            if bool(moved == True):
                # keep track of stop time/frame for later
                stimulus_onset_practice_tobii.tStop = t  # not accounting for scr refresh
                stimulus_onset_practice_tobii.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('stimulus_onset_practice_tobii.stopped', t)
                stimulus_onset_practice_tobii.status = FINISHED
        # Run 'Each Frame' code from dragging_code_3
        x = mouse_21.getPos()[0]
        #y = mouse.getPos()[1]
        
        if moved == False:
             mouseloc = mouse_21.getPos()
             if mouseloc[0] != mouserec[0] or mouseloc[1] != mouserec[1]:
                  moved = True
                  mouse_moved = globalClock.getTime()
                  mouse_moved_lsl = local_clock()
                  thisExp.addData("mouse_moved_elapsed", mouse_moved)
                  thisExp.addData("mouse_moved_lsl", mouse_moved_lsl)
                  thisExp.addData('reaction_time',round(t*1000))
        
        x_r = x + 618
        x_l = x - 618
        
        grating_r_3.pos = (x_r,0)
        grating_l_3.pos = (x_l,0)
        
        if grating_r_3.overlaps(dot_3):
            dot_3.pos = grating_r_3.pos
        
        elif grating_l_3.overlaps(dot_3):
            dot_3.pos = grating_l_3.pos
        
        dot_trajectory.append(dot_3.pos[0])
        
        if eccentricity > 0:
            if grating_r_3.pos[0] <= r_lim_corr:
                correct = 1
                timeout=0
                thisExp.addData("response_time", round(t*1000))
                marker_manager.set_value(32)   # RIGHT
                continueRoutine=False
            elif grating_r_3.pos[0] >= r_lim_wrong:
                correct = 0
                timeout=0
                thisExp.addData("response_time", round(t*1000))
                marker_manager.set_value(32)   # RIGHT
                continueRoutine=False
        elif eccentricity < 0:
            if grating_l_3.pos[0] >= l_lim_corr:
                correct = 1
                timeout=0
                thisExp.addData("response_time", round(t*1000))
                marker_manager.set_value(31)   # LEFT
                continueRoutine=False
            elif grating_l_3.pos[0] <= l_lim_wrong:
                correct = 0
                timeout=0
                thisExp.addData("response_time", round(t*1000))
                marker_manager.set_value(31)   # LEFT
                continueRoutine=False
        
        
        if sound_no_resp_3.status == STARTED:
            correct = 'NaN'
            timeout = 1
            marker_manager.set_value(35)   # timeout
        
        
        
        # *dot_3* updates
        if dot_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dot_3.frameNStart = frameN  # exact frame index
            dot_3.tStart = t  # local t and not account for scr refresh
            dot_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dot_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dot_3.started')
            dot_3.setAutoDraw(True)
        if dot_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dot_3.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                dot_3.tStop = t  # not accounting for scr refresh
                dot_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dot_3.stopped')
                dot_3.setAutoDraw(False)
        
        # *fixation_6* updates
        if fixation_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_6.frameNStart = frameN  # exact frame index
            fixation_6.tStart = t  # local t and not account for scr refresh
            fixation_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_6.started')
            fixation_6.setAutoDraw(True)
        if fixation_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_6.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                fixation_6.tStop = t  # not accounting for scr refresh
                fixation_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_6.stopped')
                fixation_6.setAutoDraw(False)
        
        # *grating_l_3* updates
        if grating_l_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            grating_l_3.frameNStart = frameN  # exact frame index
            grating_l_3.tStart = t  # local t and not account for scr refresh
            grating_l_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(grating_l_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'grating_l_3.started')
            grating_l_3.setAutoDraw(True)
        if grating_l_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > grating_l_3.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                grating_l_3.tStop = t  # not accounting for scr refresh
                grating_l_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'grating_l_3.stopped')
                grating_l_3.setAutoDraw(False)
        
        # *grating_r_3* updates
        if grating_r_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            grating_r_3.frameNStart = frameN  # exact frame index
            grating_r_3.tStart = t  # local t and not account for scr refresh
            grating_r_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(grating_r_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'grating_r_3.started')
            grating_r_3.setAutoDraw(True)
        if grating_r_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > grating_r_3.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                grating_r_3.tStop = t  # not accounting for scr refresh
                grating_r_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'grating_r_3.stopped')
                grating_r_3.setAutoDraw(False)
        # *mouse_21* updates
        if mouse_21.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_21.frameNStart = frameN  # exact frame index
            mouse_21.tStart = t  # local t and not account for scr refresh
            mouse_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_21, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_21.started', t)
            mouse_21.status = STARTED
            prevButtonState = mouse_21.getPressed()  # if button is down already this ISN'T a new click
        if mouse_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_21.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                mouse_21.tStop = t  # not accounting for scr refresh
                mouse_21.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_21.stopped', t)
                mouse_21.status = FINISHED
        if mouse_21.status == STARTED:  # only update if started and not finished!
            x, y = mouse_21.getPos()
            mouse_21.x.append(x)
            mouse_21.y.append(y)
            buttons = mouse_21.getPressed()
            mouse_21.leftButton.append(buttons[0])
            mouse_21.midButton.append(buttons[1])
            mouse_21.rightButton.append(buttons[2])
            mouse_21.time.append(globalClock.getTime())
        # start/stop sound_trial_start_3
        if sound_trial_start_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_trial_start_3.frameNStart = frameN  # exact frame index
            sound_trial_start_3.tStart = t  # local t and not account for scr refresh
            sound_trial_start_3.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_trial_start_3.started', tThisFlipGlobal)
            sound_trial_start_3.play(when=win)  # sync with win flip
        if sound_trial_start_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_trial_start_3.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                sound_trial_start_3.tStop = t  # not accounting for scr refresh
                sound_trial_start_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_trial_start_3.stopped')
                sound_trial_start_3.stop()
        # start/stop sound_no_resp_3
        if sound_no_resp_3.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            sound_no_resp_3.frameNStart = frameN  # exact frame index
            sound_no_resp_3.tStart = t  # local t and not account for scr refresh
            sound_no_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_no_resp_3.started', tThisFlipGlobal)
            sound_no_resp_3.play(when=win)  # sync with win flip
        if sound_no_resp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_no_resp_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                sound_no_resp_3.tStop = t  # not accounting for scr refresh
                sound_no_resp_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_no_resp_3.stopped')
                sound_no_resp_3.stop()
        # *response_practice_tobii* updates
        if response_practice_tobii.status == NOT_STARTED and moved == True:
            # keep track of start time/frame for later
            response_practice_tobii.frameNStart = frameN  # exact frame index
            response_practice_tobii.tStart = t  # local t and not account for scr refresh
            response_practice_tobii.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_practice_tobii, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('response_practice_tobii.started', t)
            response_practice_tobii.status = STARTED
        if response_practice_tobii.status == STARTED:
            if bool(continueRoutine == False):
                # keep track of stop time/frame for later
                response_practice_tobii.tStop = t  # not accounting for scr refresh
                response_practice_tobii.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('response_practice_tobii.stopped', t)
                response_practice_tobii.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_practice" ---
    for thisComponent in trial_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if stimulus_onset_practice_tobii.status != FINISHED:
        stimulus_onset_practice_tobii.status = FINISHED
    # Run 'End Routine' code from dragging_code_3
    end_trial = globalClock.getTime()
    end_trial_lsl = local_clock()
    thisExp.addData("trial_end_elapsed", end_trial)
    thisExp.addData("trial_end_lsl", end_trial_lsl)
    
    thisExp.addData("correct", correct)
    thisExp.addData('timeout', timeout)
    thisExp.addData("dot_trajectory", dot_trajectory)
    timing.delay(100)
    marker_manager.set_value(0)
    # store data for practice (TrialHandler)
    practice.addData('mouse_21.x', mouse_21.x)
    practice.addData('mouse_21.y', mouse_21.y)
    practice.addData('mouse_21.leftButton', mouse_21.leftButton)
    practice.addData('mouse_21.midButton', mouse_21.midButton)
    practice.addData('mouse_21.rightButton', mouse_21.rightButton)
    practice.addData('mouse_21.time', mouse_21.time)
    sound_trial_start_3.stop()  # ensure sound has stopped at end of routine
    sound_no_resp_3.stop()  # ensure sound has stopped at end of routine
    # make sure the eyetracker recording stops
    if response_practice_tobii.status != FINISHED:
        response_practice_tobii.status = FINISHED
    # the Routine "trial_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback_practice" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code_2
    mouse.setPos(newPos=(0, 0))
    
    if correct==1:
        fb_sound = "2000.wav"
        fb_sound_dur = 0.2
        fb_dur = 1
        fb_volume = 0.1
        marker_manager.set_value(41)
        timing.delay(100)
        marker_manager.set_value(0)
        
    elif correct==0:
        fb_sound = "whitenoise.wav"
        fb_sound_dur = 0.5
        fb_dur = 2
        fb_volume = 0.1
        marker_manager.set_value(42)
        timing.delay(100)
        marker_manager.set_value(0)
    
    else:
        fb_sound = 200
        fb_sound_dur = 0.1
        fb_dur = 1.5
        fb_volume = 0
        marker_manager.set_value(45)    
        timing.delay(100)
        marker_manager.set_value(0)
    
    feedback_sound_2.setSound(fb_sound, secs=fb_sound_dur, hamming=True)
    feedback_sound_2.setVolume(fb_volume, log=False)
    # Run 'Begin Routine' code from feedback_practice_timing
    # Feedback start: elapsed experiment time
    feedback_start = globalClock.getTime()
    
    # Feedback start: LSL-aligned time
    feedback_start_lsl = local_clock()
    
    thisExp.addData("feedback_start_elapsed", feedback_start)
    thisExp.addData("feedback_start_lsl", feedback_start_lsl)
    # keep track of which components have finished
    feedback_practiceComponents = [feedback_practice_tobii, feedback_sound_2, fixation_7]
    for thisComponent in feedback_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback_practice" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *feedback_practice_tobii* updates
        if feedback_practice_tobii.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_practice_tobii.frameNStart = frameN  # exact frame index
            feedback_practice_tobii.tStart = t  # local t and not account for scr refresh
            feedback_practice_tobii.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_practice_tobii, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('feedback_practice_tobii.started', t)
            feedback_practice_tobii.status = STARTED
        if feedback_practice_tobii.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_practice_tobii.tStartRefresh + fb_sound_dur-frameTolerance:
                # keep track of stop time/frame for later
                feedback_practice_tobii.tStop = t  # not accounting for scr refresh
                feedback_practice_tobii.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('feedback_practice_tobii.stopped', t)
                feedback_practice_tobii.status = FINISHED
        # Run 'Each Frame' code from feedback_code_2
        mouse.setPos(newPos=(0, 0))
        # start/stop feedback_sound_2
        if feedback_sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_sound_2.frameNStart = frameN  # exact frame index
            feedback_sound_2.tStart = t  # local t and not account for scr refresh
            feedback_sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('feedback_sound_2.started', tThisFlipGlobal)
            feedback_sound_2.play(when=win)  # sync with win flip
        if feedback_sound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_sound_2.tStartRefresh + fb_sound_dur-frameTolerance:
                # keep track of stop time/frame for later
                feedback_sound_2.tStop = t  # not accounting for scr refresh
                feedback_sound_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_sound_2.stopped')
                feedback_sound_2.stop()
        
        # *fixation_7* updates
        if fixation_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_7.frameNStart = frameN  # exact frame index
            fixation_7.tStart = t  # local t and not account for scr refresh
            fixation_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_7.started')
            fixation_7.setAutoDraw(True)
        if fixation_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_7.tStartRefresh + fb_dur-frameTolerance:
                # keep track of stop time/frame for later
                fixation_7.tStop = t  # not accounting for scr refresh
                fixation_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_7.stopped')
                fixation_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback_practice" ---
    for thisComponent in feedback_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if feedback_practice_tobii.status != FINISHED:
        feedback_practice_tobii.status = FINISHED
    feedback_sound_2.stop()  # ensure sound has stopped at end of routine
    # Run 'End Routine' code from feedback_practice_timing
    # Feedback stop: elapsed experiment time
    feedback_stop = globalClock.getTime()
    
    # Feedback stop: LSL-aligned time
    feedback_stop_lsl = local_clock()
    
    thisExp.addData("feedback_stop_elapsed", feedback_stop)
    thisExp.addData("feedback_stop_lsl", feedback_stop_lsl)
    # the Routine "feedback_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'practice'

# get names of stimulus parameters
if practice.trialList in ([], [None], None):
    params = []
else:
    params = practice.trialList[0].keys()
# save data for this loop
practice.saveAsExcel(filename + '.xlsx', sheetName='practice',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "start_session" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from mouse_visible_10
win.mouseVisible = True
# setup some python lists for storing info about the mouse_14
mouse_14.x = []
mouse_14.y = []
mouse_14.leftButton = []
mouse_14.midButton = []
mouse_14.rightButton = []
mouse_14.time = []
mouse_14.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
start_sessionComponents = [end_practice_txt, continue_txt_12, mouse_14]
for thisComponent in start_sessionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "start_session" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_practice_txt* updates
    if end_practice_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_practice_txt.frameNStart = frameN  # exact frame index
        end_practice_txt.tStart = t  # local t and not account for scr refresh
        end_practice_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_practice_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_practice_txt.started')
        end_practice_txt.setAutoDraw(True)
    
    # *continue_txt_12* updates
    if continue_txt_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_12.frameNStart = frameN  # exact frame index
        continue_txt_12.tStart = t  # local t and not account for scr refresh
        continue_txt_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_12, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_12.started')
        continue_txt_12.setAutoDraw(True)
    # *mouse_14* updates
    if mouse_14.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_14.frameNStart = frameN  # exact frame index
        mouse_14.tStart = t  # local t and not account for scr refresh
        mouse_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_14, 'tStartRefresh')  # time at next scr refresh
        mouse_14.status = STARTED
        mouse_14.mouseClock.reset()
        prevButtonState = mouse_14.getPressed()  # if button is down already this ISN'T a new click
    if mouse_14.status == STARTED:  # only update if started and not finished!
        buttons = mouse_14.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_12)
                    clickableList = continue_txt_12
                except:
                    clickableList = [continue_txt_12]
                for obj in clickableList:
                    if obj.contains(mouse_14):
                        gotValidClick = True
                        mouse_14.clicked_name.append(obj.name)
                x, y = mouse_14.getPos()
                mouse_14.x.append(x)
                mouse_14.y.append(y)
                buttons = mouse_14.getPressed()
                mouse_14.leftButton.append(buttons[0])
                mouse_14.midButton.append(buttons[1])
                mouse_14.rightButton.append(buttons[2])
                mouse_14.time.append(mouse_14.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_sessionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "start_session" ---
for thisComponent in start_sessionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_14.x', mouse_14.x)
thisExp.addData('mouse_14.y', mouse_14.y)
thisExp.addData('mouse_14.leftButton', mouse_14.leftButton)
thisExp.addData('mouse_14.midButton', mouse_14.midButton)
thisExp.addData('mouse_14.rightButton', mouse_14.rightButton)
thisExp.addData('mouse_14.time', mouse_14.time)
thisExp.addData('mouse_14.clicked_name', mouse_14.clicked_name)
thisExp.nextEntry()
# the Routine "start_session" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "start_reminder" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from start_session_time
win.mouseVisible = True
# setup some python lists for storing info about the mouse_37
mouse_37.x = []
mouse_37.y = []
mouse_37.leftButton = []
mouse_37.midButton = []
mouse_37.rightButton = []
mouse_37.time = []
mouse_37.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
start_reminderComponents = [instruction_txt_6, continue_txt_33, mouse_37]
for thisComponent in start_reminderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "start_reminder" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_txt_6* updates
    if instruction_txt_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_txt_6.frameNStart = frameN  # exact frame index
        instruction_txt_6.tStart = t  # local t and not account for scr refresh
        instruction_txt_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_txt_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instruction_txt_6.started')
        instruction_txt_6.setAutoDraw(True)
    
    # *continue_txt_33* updates
    if continue_txt_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_33.frameNStart = frameN  # exact frame index
        continue_txt_33.tStart = t  # local t and not account for scr refresh
        continue_txt_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_33, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_33.started')
        continue_txt_33.setAutoDraw(True)
    # *mouse_37* updates
    if mouse_37.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_37.frameNStart = frameN  # exact frame index
        mouse_37.tStart = t  # local t and not account for scr refresh
        mouse_37.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_37, 'tStartRefresh')  # time at next scr refresh
        mouse_37.status = STARTED
        mouse_37.mouseClock.reset()
        prevButtonState = mouse_37.getPressed()  # if button is down already this ISN'T a new click
    if mouse_37.status == STARTED:  # only update if started and not finished!
        buttons = mouse_37.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_11)
                    clickableList = continue_txt_11
                except:
                    clickableList = [continue_txt_11]
                for obj in clickableList:
                    if obj.contains(mouse_37):
                        gotValidClick = True
                        mouse_37.clicked_name.append(obj.name)
                x, y = mouse_37.getPos()
                mouse_37.x.append(x)
                mouse_37.y.append(y)
                buttons = mouse_37.getPressed()
                mouse_37.leftButton.append(buttons[0])
                mouse_37.midButton.append(buttons[1])
                mouse_37.rightButton.append(buttons[2])
                mouse_37.time.append(mouse_37.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_reminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "start_reminder" ---
for thisComponent in start_reminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from start_session_time
thisExp.addData('session_start', data.getDateStr())
marker_manager.set_value(90)
timing.delay(30)
marker_manager.set_value(0)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_37.x', mouse_37.x)
thisExp.addData('mouse_37.y', mouse_37.y)
thisExp.addData('mouse_37.leftButton', mouse_37.leftButton)
thisExp.addData('mouse_37.midButton', mouse_37.midButton)
thisExp.addData('mouse_37.rightButton', mouse_37.rightButton)
thisExp.addData('mouse_37.time', mouse_37.time)
thisExp.addData('mouse_37.clicked_name', mouse_37.clicked_name)
thisExp.nextEntry()
# the Routine "start_reminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pregen_sequence_' + str(int(expInfo['participant'][-1])) + '.xlsx', selection='0:10'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "blink" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_8
    marker_manager.set_value(5)
    timing.delay(100)
    marker_manager.set_value(0)
    
    # Run 'Begin Routine' code from code_6
    blink_trial = random.uniform(1.0, 2.0)
    
    
    text_3.setText('')
    # keep track of which components have finished
    blinkComponents = [text_3]
    for thisComponent in blinkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blink" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + blink_trial-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blinkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blink" ---
    for thisComponent in blinkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "blink" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "fix" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from start_trial
    marker_manager.set_value(10)
    timing.delay(100)
    marker_manager.set_value(0)
    
    # Run 'Begin Routine' code from mouse_visible
    win.mouseVisible = False
    mouse.setPos(newPos=(0, 0))
    
    # Run 'Begin Routine' code from set_contrast_side
    if eccentricity == -15:
        leftCont = baseContrast+contrastDelta
        rightCont = baseContrast
    elif eccentricity == 15:
        leftCont = baseContrast
        rightCont = baseContrast+contrastDelta
    
    signed_contrast=rightCont-leftCont
    
    # Save all these variables to the log
    thisExp.addData("signed_contrast", signed_contrast)
    thisExp.addData("leftCont", leftCont)
    thisExp.addData("rightCont", rightCont)
    
    #setup for el time triggers
    #fixation_2.elOnsetDetected = False
    #fixation_2.elOffsetDetected = False
    fixation_2.setColor([1,1,1], colorSpace='rgb')
    fixation_2.setSize((0.75, 0.75))
    # Run 'Begin Routine' code from timing_fixation
    fixation_start_elapsed = globalClock.getTime()      # seconds since experiment start
    fixation_start_lsl = local_clock()                  # LSL-aligned time
    thisExp.addData("fixation_tobii_start_elapsed", fixation_start_elapsed)
    thisExp.addData("fixation_tobii_start_lsl", fixation_start_lsl)
    # keep track of which components have finished
    fixComponents = [fixation_tobii, fixation_2]
    for thisComponent in fixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fix" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from mouse_visible
        mouse.setPos(newPos=(0, 0))
        # Run 'Each Frame' code from set_contrast_side
        #if fixation_2.tStartRefresh is not None and not fixation_2.elOnsetDetected:
            #el_tracker.sendMessage('fix_cross_ONSET')
            #fixation_2.elOnsetDetected = True
        
        #if fixation_2.tStopRefresh is not None and fixation_2.tStartRefresh is not None and not fixation_2.elOffsetDetected:
            #el_tracker.sendMessage('fix_cross_OFFSET')
            #fixation_2.elOffsetDetected = True 
        # *fixation_tobii* updates
        if fixation_tobii.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_tobii.frameNStart = frameN  # exact frame index
            fixation_tobii.tStart = t  # local t and not account for scr refresh
            fixation_tobii.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_tobii, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('fixation_tobii.started', t)
            fixation_tobii.status = STARTED
        if fixation_tobii.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_tobii.tStartRefresh + q-frameTolerance:
                # keep track of stop time/frame for later
                fixation_tobii.tStop = t  # not accounting for scr refresh
                fixation_tobii.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('fixation_tobii.stopped', t)
                fixation_tobii.status = FINISHED
        
        # *fixation_2* updates
        if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_2.frameNStart = frameN  # exact frame index
            fixation_2.tStart = t  # local t and not account for scr refresh
            fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_2.started')
            fixation_2.setAutoDraw(True)
        if fixation_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_2.tStartRefresh + q-frameTolerance:
                # keep track of stop time/frame for later
                fixation_2.tStop = t  # not accounting for scr refresh
                fixation_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_2.stopped')
                fixation_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fix" ---
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if fixation_tobii.status != FINISHED:
        fixation_tobii.status = FINISHED
    # Run 'End Routine' code from timing_fixation
    fixation_stop_elapsed = globalClock.getTime()
    fixation_stop_lsl = local_clock()
    
    # Save to data file
    thisExp.addData("fixation_tobii_stop_elapsed", fixation_stop_elapsed)
    thisExp.addData("fixation_tobii_stop_lsl", fixation_stop_lsl)
    # the Routine "fix" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from stimulus_onset
    signed_contrast=rightCont-leftCont
    contrast_marker = 150 + round((signed_contrast/0.2)*50)
    marker_manager.set_value(contrast_marker)
    timing.delay(100)
    marker_manager.set_value(0)
    
    
    # Run 'Begin Routine' code from dragging_code
    #reset mouse position
    mouse.setPos(newPos=(0, 0))
    
    #set thresholds for response recording for each stim side and corr/wrong
    r_lim_corr = 0.05
    l_lim_corr = -0.05
    r_lim_wrong = 1236
    l_lim_wrong = -1236
    
    #setup for later recording reactio time
    mouserec = mouse.getPos()
    moved = False
    
    #create empty list to later store dot coordinates
    dot_trajectory = []
    
    trial_start = globalClock.getTime()
    trial_start_lsl = local_clock()
    thisExp.addData("trial_start_elapsed", trial_start)
    thisExp.addData("trial_start_lsl", trial_start_lsl)
    
    #setup for el on/offset triggers
    #sound_trial_start.elOnsetDetected = False
    #sound_trial_start.elOffsetDetected = False
    
    #sound_no_resp.elOnsetDetected = False
    #sound_no_resp.elOffsetDetected = False
    dot.setPos((618, 0))
    grating_l.setContrast(leftCont)
    grating_l.setPos((-618, 0))
    grating_l.setPhase(random.random()*360)
    grating_r.setContrast(rightCont)
    grating_r.setPos((618, 0))
    grating_r.setPhase(random.random()*360)
    fixation.setColor([1,1,1], colorSpace='rgb')
    fixation.setSize((0.75, 0.75))
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    gotValidClick = False  # until a click is received
    sound_trial_start.setSound('5000', secs=0.1, hamming=True)
    sound_trial_start.setVolume(0.1, log=False)
    sound_no_resp.setSound('567', secs=0.5, hamming=True)
    sound_no_resp.setVolume(0.1, log=False)
    # keep track of which components have finished
    trialComponents = [stimulus_onset_tobii, dot, grating_l, grating_r, fixation, mouse, sound_trial_start, sound_no_resp, response_tobii]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *stimulus_onset_tobii* updates
        if stimulus_onset_tobii.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimulus_onset_tobii.frameNStart = frameN  # exact frame index
            stimulus_onset_tobii.tStart = t  # local t and not account for scr refresh
            stimulus_onset_tobii.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimulus_onset_tobii, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('stimulus_onset_tobii.started', t)
            stimulus_onset_tobii.status = STARTED
        if stimulus_onset_tobii.status == STARTED:
            if bool(moved == True):
                # keep track of stop time/frame for later
                stimulus_onset_tobii.tStop = t  # not accounting for scr refresh
                stimulus_onset_tobii.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('stimulus_onset_tobii.stopped', t)
                stimulus_onset_tobii.status = FINISHED
        # Run 'Each Frame' code from dragging_code
        #if sound_trial_start.tStartRefresh is not None and not sound_trial_start.elOnsetDetected:
            #el_tracker.sendMessage('signed_contrast %.2f' % signed_contrast)
            #el_tracker.sendMessage('stimOn')
            #el_tracker.sendMessage('sound_trial_start_ONSET')
            #sound_trial_start.elOnsetDetected = True
        
        #if sound_trial_start.tStopRefresh is not None and sound_trial_start.tStartRefresh is not None and not sound_trial_start.elOffsetDetected:
            #el_tracker.sendMessage('sound_trial_start_OFFSET')
            #sound_trial_start.elOffsetDetected = True 
        
        x = mouse.getPos()[0]
        
        if moved == False:
             mouseloc = mouse.getPos()
             if mouseloc[0] != mouserec[0] or mouseloc[1] != mouserec[1]:
                  moved = True
                  mouse_moved = globalClock.getTime()
                  mouse_moved_lsl = local_clock()
                  thisExp.addData("mouse_moved_elapsed", mouse_moved)
                  thisExp.addData("mouse_moved_lsl", mouse_moved_lsl)
                  thisExp.addData('reaction_time',round(t*1000))
                  #el_tracker.sendMessage('moveInit')
        
        x_r = x + 618
        x_l = x - 618
        
        grating_r.pos = (x_r,0)
        grating_l.pos = (x_l,0)
        
        if grating_r.overlaps(dot):
            dot.pos = grating_r.pos
        
        elif grating_l.overlaps(dot):
            dot.pos = grating_l.pos
        
        dot_trajectory.append(dot.pos[0])
        
        if eccentricity > 0:
            if grating_r.pos[0] <= r_lim_corr:
                correct = 1
                timeout=0
                response=1
                #el_tracker.sendMessage('response %i' % response)
                marker_manager.set_value(32)   # RIGHT
                thisExp.addData("response_time", round(t*1000))
                continueRoutine=False
            elif grating_r.pos[0] >= r_lim_wrong:
                correct = 0
                timeout=0
                response=-1
                #el_tracker.sendMessage('response %i' % response)
                marker_manager.set_value(32)   # RIGHT
                thisExp.addData("response_time", round(t*1000))
                continueRoutine=False
        elif eccentricity < 0:
            if grating_l.pos[0] >= l_lim_corr:
                correct = 1
                timeout=0
                response=-1
                #el_tracker.sendMessage('response %i' % response)
                marker_manager.set_value(31)   # LEFT
                thisExp.addData("response_time", round(t*1000))
                continueRoutine=False
            elif grating_l.pos[0] <= l_lim_wrong:
                correct = 0
                timeout=0
                response=1
                #el_tracker.sendMessage('response %i' % response)
                marker_manager.set_value(31)   # LEFT
                thisExp.addData("response_time", round(t*1000))
                continueRoutine=False
        
        
        if sound_no_resp.status == STARTED:
            correct = 'NaN'
            timeout = 1
            marker_manager.set_value(35)   # TIMEOUT
        
        
        #if sound_no_resp.tStartRefresh is not None and not sound_no_resp.elOnsetDetected:
            #el_tracker.sendMessage('timeout')
            #el_tracker.sendMessage('sound_no_resp_ONSET')
            #sound_no_resp.elOnsetDetected = True
        
        #if sound_no_resp.tStopRefresh is not None and sound_no_resp.tStartRefresh is not None and not sound_no_resp.elOffsetDetected:
            #el_tracker.sendMessage('sound_no_resp_OFFSET')
            #sound_no_resp.elOffsetDetected = True 
        
        
        # *dot* updates
        if dot.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dot.frameNStart = frameN  # exact frame index
            dot.tStart = t  # local t and not account for scr refresh
            dot.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dot, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dot.started')
            dot.setAutoDraw(True)
        if dot.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dot.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                dot.tStop = t  # not accounting for scr refresh
                dot.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dot.stopped')
                dot.setAutoDraw(False)
        
        # *grating_l* updates
        if grating_l.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            grating_l.frameNStart = frameN  # exact frame index
            grating_l.tStart = t  # local t and not account for scr refresh
            grating_l.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(grating_l, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'grating_l.started')
            grating_l.setAutoDraw(True)
        if grating_l.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > grating_l.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                grating_l.tStop = t  # not accounting for scr refresh
                grating_l.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'grating_l.stopped')
                grating_l.setAutoDraw(False)
        
        # *grating_r* updates
        if grating_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            grating_r.frameNStart = frameN  # exact frame index
            grating_r.tStart = t  # local t and not account for scr refresh
            grating_r.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(grating_r, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'grating_r.started')
            grating_r.setAutoDraw(True)
        if grating_r.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > grating_r.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                grating_r.tStop = t  # not accounting for scr refresh
                grating_r.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'grating_r.stopped')
                grating_r.setAutoDraw(False)
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation.started')
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.stopped')
                fixation.setAutoDraw(False)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                mouse.tStop = t  # not accounting for scr refresh
                mouse.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse.stopped', t)
                mouse.status = FINISHED
        if mouse.status == STARTED:  # only update if started and not finished!
            x, y = mouse.getPos()
            mouse.x.append(x)
            mouse.y.append(y)
            buttons = mouse.getPressed()
            mouse.leftButton.append(buttons[0])
            mouse.midButton.append(buttons[1])
            mouse.rightButton.append(buttons[2])
            mouse.time.append(globalClock.getTime())
        # start/stop sound_trial_start
        if sound_trial_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_trial_start.frameNStart = frameN  # exact frame index
            sound_trial_start.tStart = t  # local t and not account for scr refresh
            sound_trial_start.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_trial_start.started', tThisFlipGlobal)
            sound_trial_start.play(when=win)  # sync with win flip
        if sound_trial_start.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_trial_start.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                sound_trial_start.tStop = t  # not accounting for scr refresh
                sound_trial_start.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_trial_start.stopped')
                sound_trial_start.stop()
        # start/stop sound_no_resp
        if sound_no_resp.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            sound_no_resp.frameNStart = frameN  # exact frame index
            sound_no_resp.tStart = t  # local t and not account for scr refresh
            sound_no_resp.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_no_resp.started', tThisFlipGlobal)
            sound_no_resp.play(when=win)  # sync with win flip
        if sound_no_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_no_resp.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                sound_no_resp.tStop = t  # not accounting for scr refresh
                sound_no_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_no_resp.stopped')
                sound_no_resp.stop()
        # *response_tobii* updates
        if response_tobii.status == NOT_STARTED and moved == True:
            # keep track of start time/frame for later
            response_tobii.frameNStart = frameN  # exact frame index
            response_tobii.tStart = t  # local t and not account for scr refresh
            response_tobii.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_tobii, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('response_tobii.started', t)
            response_tobii.status = STARTED
        if response_tobii.status == STARTED:
            if bool(continueRoutine == False):
                # keep track of stop time/frame for later
                response_tobii.tStop = t  # not accounting for scr refresh
                response_tobii.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('response_tobii.stopped', t)
                response_tobii.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if stimulus_onset_tobii.status != FINISHED:
        stimulus_onset_tobii.status = FINISHED
    # Run 'End Routine' code from dragging_code
    end_trial = globalClock.getTime()
    end_trial_lsl = local_clock()
    thisExp.addData("trial_end_elapsed", end_trial)
    thisExp.addData("trial_end_lsl", end_trial_lsl)
    
    
    thisExp.addData("correct", correct)
    thisExp.addData('timeout', timeout)
    thisExp.addData("dot_trajectory", dot_trajectory)
    
    timing.delay(100)
    marker_manager.set_value(0)
    
    # store data for trials (TrialHandler)
    trials.addData('mouse.x', mouse.x)
    trials.addData('mouse.y', mouse.y)
    trials.addData('mouse.leftButton', mouse.leftButton)
    trials.addData('mouse.midButton', mouse.midButton)
    trials.addData('mouse.rightButton', mouse.rightButton)
    trials.addData('mouse.time', mouse.time)
    sound_trial_start.stop()  # ensure sound has stopped at end of routine
    sound_no_resp.stop()  # ensure sound has stopped at end of routine
    # make sure the eyetracker recording stops
    if response_tobii.status != FINISHED:
        response_tobii.status = FINISHED
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    mouse.setPos(newPos=(0, 0))
    
    #el_tracker.sendMessage('feedbackType %s' % correct)
    
    if correct==1:
        fb_sound = "2000.wav"
        fb_sound_dur = 0.2
        fb_dur = 1
        fb_volume = 0.1
        tot_points += 1
        marker_manager.set_value(41)
        timing.delay(100)
        marker_manager.set_value(0)
        
    elif correct==0:
        fb_sound = "whitenoise.wav"
        fb_sound_dur = 0.5
        fb_dur = 2
        fb_volume = 0.1
        marker_manager.set_value(42)
        timing.delay(100)
        marker_manager.set_value(0)
        
    else:
        fb_sound = 200
        fb_sound_dur = 0.1
        fb_dur = 1.5
        fb_volume = 0
        marker_manager.set_value(45)
        timing.delay(100)
        marker_manager.set_value(0)
        
    #fixation_3.elOnsetDetected = False
    #fixation_3.elOffsetDetected = False
    
    #feedback_sound.elOnsetDetected = False
    #feedback_sound.elOffsetDetected = False
    feedback_sound.setSound(fb_sound, secs=fb_sound_dur, hamming=True)
    feedback_sound.setVolume(fb_volume, log=False)
    # Run 'Begin Routine' code from feedback_timing
    # Feedback start: elapsed experiment time
    feedback_start = globalClock.getTime()
    
    # Feedback start: LSL-aligned time
    feedback_start_lsl = local_clock()
    
    thisExp.addData("feedback_start_elapsed", feedback_start)
    thisExp.addData("feedback_start_lsl", feedback_start_lsl)
    # keep track of which components have finished
    feedbackComponents = [feedback_tobii, feedback_sound, fixation_3]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *feedback_tobii* updates
        if feedback_tobii.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_tobii.frameNStart = frameN  # exact frame index
            feedback_tobii.tStart = t  # local t and not account for scr refresh
            feedback_tobii.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_tobii, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('feedback_tobii.started', t)
            feedback_tobii.status = STARTED
        if feedback_tobii.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_tobii.tStartRefresh + fb_sound_dur-frameTolerance:
                # keep track of stop time/frame for later
                feedback_tobii.tStop = t  # not accounting for scr refresh
                feedback_tobii.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('feedback_tobii.stopped', t)
                feedback_tobii.status = FINISHED
        # Run 'Each Frame' code from feedback_code
        mouse.setPos(newPos=(0, 0))
        
        #if fixation_3.tStartRefresh is not None and not fixation_3.elOnsetDetected:
            #el_tracker.sendMessage('%i %s_ONSET' % (int(round((globalClock.getTime()-fixation_3.tStartRefresh)*1000)),fixation_3.name))
            #fixation_3.elOnsetDetected = True
        
        #if fixation_3.tStopRefresh is not None and fixation_3.tStartRefresh is not None and not fixation_3.elOffsetDetected:
            #el_tracker.sendMessage('%i %s_OFFSET' % (int(round((globalClock.getTime()-fixation_3.tStopRefresh)*1000)),fixation_3.name))
            #fixation_3.elOffsetDetected = True 
        
        #if feedback_sound.tStartRefresh is not None and not feedback_sound.elOnsetDetected:
            #el_tracker.sendMessage('feedback_sound_ONSET')
            #feedback_sound.elOnsetDetected = True
        
        #if feedback_sound.tStopRefresh is not None and feedback_sound.tStartRefresh is not None and not feedback_sound.elOffsetDetected:
            #el_tracker.sendMessage('feedback_sound_OFFSET')
            #feedback_sound.elOffsetDetected = True 
        # start/stop feedback_sound
        if feedback_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_sound.frameNStart = frameN  # exact frame index
            feedback_sound.tStart = t  # local t and not account for scr refresh
            feedback_sound.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('feedback_sound.started', tThisFlipGlobal)
            feedback_sound.play(when=win)  # sync with win flip
        if feedback_sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_sound.tStartRefresh + fb_sound_dur-frameTolerance:
                # keep track of stop time/frame for later
                feedback_sound.tStop = t  # not accounting for scr refresh
                feedback_sound.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_sound.stopped')
                feedback_sound.stop()
        
        # *fixation_3* updates
        if fixation_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_3.frameNStart = frameN  # exact frame index
            fixation_3.tStart = t  # local t and not account for scr refresh
            fixation_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_3.started')
            fixation_3.setAutoDraw(True)
        if fixation_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_3.tStartRefresh + fb_dur-frameTolerance:
                # keep track of stop time/frame for later
                fixation_3.tStop = t  # not accounting for scr refresh
                fixation_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_3.stopped')
                fixation_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if feedback_tobii.status != FINISHED:
        feedback_tobii.status = FINISHED
    # Run 'End Routine' code from feedback_code
    
    
    
    feedback_sound.stop()  # ensure sound has stopped at end of routine
    # Run 'End Routine' code from feedback_timing
    # Feedback stop: elapsed experiment time
    feedback_stop = globalClock.getTime()
    
    # Feedback stop: LSL-aligned time
    feedback_stop_lsl = local_clock()
    
    thisExp.addData("feedback_stop_elapsed", feedback_stop)
    thisExp.addData("feedback_stop_lsl", feedback_stop_lsl)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "break_time" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from mouse_visible_8
win.mouseVisible = True
# Run 'Begin Routine' code from start_session_timer_3
marker_manager.set_value(90)
timing.delay(100)
marker_manager.set_value(0)

# setup some python lists for storing info about the mouse_34
mouse_34.x = []
mouse_34.y = []
mouse_34.leftButton = []
mouse_34.midButton = []
mouse_34.rightButton = []
mouse_34.time = []
mouse_34.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
break_timeComponents = [end_practice_txt_2, continue_txt_30, mouse_34]
for thisComponent in break_timeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "break_time" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_practice_txt_2* updates
    if end_practice_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_practice_txt_2.frameNStart = frameN  # exact frame index
        end_practice_txt_2.tStart = t  # local t and not account for scr refresh
        end_practice_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_practice_txt_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_practice_txt_2.started')
        end_practice_txt_2.setAutoDraw(True)
    
    # *continue_txt_30* updates
    if continue_txt_30.status == NOT_STARTED and tThisFlip >= 90-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_30.frameNStart = frameN  # exact frame index
        continue_txt_30.tStart = t  # local t and not account for scr refresh
        continue_txt_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_30, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_30.started')
        continue_txt_30.setAutoDraw(True)
    # *mouse_34* updates
    if mouse_34.status == NOT_STARTED and t >= 90-frameTolerance:
        # keep track of start time/frame for later
        mouse_34.frameNStart = frameN  # exact frame index
        mouse_34.tStart = t  # local t and not account for scr refresh
        mouse_34.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_34, 'tStartRefresh')  # time at next scr refresh
        mouse_34.status = STARTED
        mouse_34.mouseClock.reset()
        prevButtonState = mouse_34.getPressed()  # if button is down already this ISN'T a new click
    if mouse_34.status == STARTED:  # only update if started and not finished!
        buttons = mouse_34.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_12)
                    clickableList = continue_txt_12
                except:
                    clickableList = [continue_txt_12]
                for obj in clickableList:
                    if obj.contains(mouse_34):
                        gotValidClick = True
                        mouse_34.clicked_name.append(obj.name)
                x, y = mouse_34.getPos()
                mouse_34.x.append(x)
                mouse_34.y.append(y)
                buttons = mouse_34.getPressed()
                mouse_34.leftButton.append(buttons[0])
                mouse_34.midButton.append(buttons[1])
                mouse_34.rightButton.append(buttons[2])
                mouse_34.time.append(mouse_34.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_timeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "break_time" ---
for thisComponent in break_timeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_34.x', mouse_34.x)
thisExp.addData('mouse_34.y', mouse_34.y)
thisExp.addData('mouse_34.leftButton', mouse_34.leftButton)
thisExp.addData('mouse_34.midButton', mouse_34.midButton)
thisExp.addData('mouse_34.rightButton', mouse_34.rightButton)
thisExp.addData('mouse_34.time', mouse_34.time)
thisExp.addData('mouse_34.clicked_name', mouse_34.clicked_name)
thisExp.nextEntry()
# the Routine "break_time" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# define target for calibration
calibrationTarget = visual.TargetStim(win, 
    name='calibrationTarget',
    radius=10.0, fillColor='lime', borderColor='lime', lineWidth=10.0,
    innerRadius=3.0, innerFillColor='lime', innerBorderColor='lime', innerLineWidth=3.0,
    colorSpace='rgb', units=None
)
# define parameters for calibration
calibration = hardware.eyetracker.EyetrackerCalibration(win, 
    eyetracker, calibrationTarget,
    units=None, colorSpace='rgb',
    progressMode='time', targetDur=1.5, expandScale=1.5,
    targetLayout='THIRTEEN_POINTS', randomisePos=True, textColor='white',
    movementAnimation=True, targetDelay=1.0
)
# run calibration
calibration.run()
# clear any keypresses from during calibration so they don't interfere with the experiment
defaultKeyboard.clearEvents()
# the Routine "calibration" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# define target for validation
validationTarget = visual.TargetStim(win, 
    name='validationTarget',
    radius=10.0, fillColor='lime', borderColor='lime', lineWidth=10.0,
    innerRadius=3.0, innerFillColor='lime', innerBorderColor='lime', innerLineWidth=3.0,
    colorSpace='rgb', units=None
)
# define parameters for validation
validation = iohub.ValidationProcedure(win,
    target=validationTarget,
    gaze_cursor='green', 
    positions='THIRTEEN_POINTS', randomize_positions=True,
    expand_scale=1.5, target_duration=1.5,
    enable_position_animation=True, target_delay=1.0,
    progress_on_key=None, text_color='white',
    show_results_screen=True, save_results_screen=True,
    color_space='rgb', unit_type=None
)
# run validation
validation.run()
# clear any keypresses from during validation so they don't interfere with the experiment
defaultKeyboard.clearEvents()
# the Routine "validation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "start_after_break" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from mouse_visible_9
win.mouseVisible = True
# setup some python lists for storing info about the mouse_35
mouse_35.x = []
mouse_35.y = []
mouse_35.leftButton = []
mouse_35.midButton = []
mouse_35.rightButton = []
mouse_35.time = []
mouse_35.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
start_after_breakComponents = [end_practice_txt_3, continue_txt_31, mouse_35]
for thisComponent in start_after_breakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "start_after_break" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_practice_txt_3* updates
    if end_practice_txt_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_practice_txt_3.frameNStart = frameN  # exact frame index
        end_practice_txt_3.tStart = t  # local t and not account for scr refresh
        end_practice_txt_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_practice_txt_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_practice_txt_3.started')
        end_practice_txt_3.setAutoDraw(True)
    
    # *continue_txt_31* updates
    if continue_txt_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_31.frameNStart = frameN  # exact frame index
        continue_txt_31.tStart = t  # local t and not account for scr refresh
        continue_txt_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_31, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_31.started')
        continue_txt_31.setAutoDraw(True)
    # *mouse_35* updates
    if mouse_35.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_35.frameNStart = frameN  # exact frame index
        mouse_35.tStart = t  # local t and not account for scr refresh
        mouse_35.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_35, 'tStartRefresh')  # time at next scr refresh
        mouse_35.status = STARTED
        mouse_35.mouseClock.reset()
        prevButtonState = mouse_35.getPressed()  # if button is down already this ISN'T a new click
    if mouse_35.status == STARTED:  # only update if started and not finished!
        buttons = mouse_35.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_12)
                    clickableList = continue_txt_12
                except:
                    clickableList = [continue_txt_12]
                for obj in clickableList:
                    if obj.contains(mouse_35):
                        gotValidClick = True
                        mouse_35.clicked_name.append(obj.name)
                x, y = mouse_35.getPos()
                mouse_35.x.append(x)
                mouse_35.y.append(y)
                buttons = mouse_35.getPressed()
                mouse_35.leftButton.append(buttons[0])
                mouse_35.midButton.append(buttons[1])
                mouse_35.rightButton.append(buttons[2])
                mouse_35.time.append(mouse_35.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_after_breakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "start_after_break" ---
for thisComponent in start_after_breakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from start_session_timer_4
thisExp.addData('session_start', data.getDateStr())
marker_manager.set_value(90)
timing.delay(30)
marker_manager.set_value(0)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_35.x', mouse_35.x)
thisExp.addData('mouse_35.y', mouse_35.y)
thisExp.addData('mouse_35.leftButton', mouse_35.leftButton)
thisExp.addData('mouse_35.midButton', mouse_35.midButton)
thisExp.addData('mouse_35.rightButton', mouse_35.rightButton)
thisExp.addData('mouse_35.time', mouse_35.time)
thisExp.addData('mouse_35.clicked_name', mouse_35.clicked_name)
thisExp.nextEntry()
# the Routine "start_after_break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pregen_sequence_' + str(int(expInfo['participant'][-1])) + '.xlsx', selection='300:310'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "blink" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_8
    marker_manager.set_value(5)
    timing.delay(100)
    marker_manager.set_value(0)
    
    # Run 'Begin Routine' code from code_6
    blink_trial = random.uniform(1.0, 2.0)
    
    
    text_3.setText('')
    # keep track of which components have finished
    blinkComponents = [text_3]
    for thisComponent in blinkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blink" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + blink_trial-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blinkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blink" ---
    for thisComponent in blinkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "blink" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "fix" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from start_trial
    marker_manager.set_value(10)
    timing.delay(100)
    marker_manager.set_value(0)
    
    # Run 'Begin Routine' code from mouse_visible
    win.mouseVisible = False
    mouse.setPos(newPos=(0, 0))
    
    # Run 'Begin Routine' code from set_contrast_side
    if eccentricity == -15:
        leftCont = baseContrast+contrastDelta
        rightCont = baseContrast
    elif eccentricity == 15:
        leftCont = baseContrast
        rightCont = baseContrast+contrastDelta
    
    signed_contrast=rightCont-leftCont
    
    # Save all these variables to the log
    thisExp.addData("signed_contrast", signed_contrast)
    thisExp.addData("leftCont", leftCont)
    thisExp.addData("rightCont", rightCont)
    
    #setup for el time triggers
    #fixation_2.elOnsetDetected = False
    #fixation_2.elOffsetDetected = False
    fixation_2.setColor([1,1,1], colorSpace='rgb')
    fixation_2.setSize((0.75, 0.75))
    # Run 'Begin Routine' code from timing_fixation
    fixation_start_elapsed = globalClock.getTime()      # seconds since experiment start
    fixation_start_lsl = local_clock()                  # LSL-aligned time
    thisExp.addData("fixation_tobii_start_elapsed", fixation_start_elapsed)
    thisExp.addData("fixation_tobii_start_lsl", fixation_start_lsl)
    # keep track of which components have finished
    fixComponents = [fixation_tobii, fixation_2]
    for thisComponent in fixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fix" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from mouse_visible
        mouse.setPos(newPos=(0, 0))
        # Run 'Each Frame' code from set_contrast_side
        #if fixation_2.tStartRefresh is not None and not fixation_2.elOnsetDetected:
            #el_tracker.sendMessage('fix_cross_ONSET')
            #fixation_2.elOnsetDetected = True
        
        #if fixation_2.tStopRefresh is not None and fixation_2.tStartRefresh is not None and not fixation_2.elOffsetDetected:
            #el_tracker.sendMessage('fix_cross_OFFSET')
            #fixation_2.elOffsetDetected = True 
        # *fixation_tobii* updates
        if fixation_tobii.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_tobii.frameNStart = frameN  # exact frame index
            fixation_tobii.tStart = t  # local t and not account for scr refresh
            fixation_tobii.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_tobii, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('fixation_tobii.started', t)
            fixation_tobii.status = STARTED
        if fixation_tobii.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_tobii.tStartRefresh + q-frameTolerance:
                # keep track of stop time/frame for later
                fixation_tobii.tStop = t  # not accounting for scr refresh
                fixation_tobii.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('fixation_tobii.stopped', t)
                fixation_tobii.status = FINISHED
        
        # *fixation_2* updates
        if fixation_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_2.frameNStart = frameN  # exact frame index
            fixation_2.tStart = t  # local t and not account for scr refresh
            fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_2.started')
            fixation_2.setAutoDraw(True)
        if fixation_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_2.tStartRefresh + q-frameTolerance:
                # keep track of stop time/frame for later
                fixation_2.tStop = t  # not accounting for scr refresh
                fixation_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_2.stopped')
                fixation_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fix" ---
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if fixation_tobii.status != FINISHED:
        fixation_tobii.status = FINISHED
    # Run 'End Routine' code from timing_fixation
    fixation_stop_elapsed = globalClock.getTime()
    fixation_stop_lsl = local_clock()
    
    # Save to data file
    thisExp.addData("fixation_tobii_stop_elapsed", fixation_stop_elapsed)
    thisExp.addData("fixation_tobii_stop_lsl", fixation_stop_lsl)
    # the Routine "fix" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from stimulus_onset
    signed_contrast=rightCont-leftCont
    contrast_marker = 150 + round((signed_contrast/0.2)*50)
    marker_manager.set_value(contrast_marker)
    timing.delay(100)
    marker_manager.set_value(0)
    
    
    # Run 'Begin Routine' code from dragging_code
    #reset mouse position
    mouse.setPos(newPos=(0, 0))
    
    #set thresholds for response recording for each stim side and corr/wrong
    r_lim_corr = 0.05
    l_lim_corr = -0.05
    r_lim_wrong = 1236
    l_lim_wrong = -1236
    
    #setup for later recording reactio time
    mouserec = mouse.getPos()
    moved = False
    
    #create empty list to later store dot coordinates
    dot_trajectory = []
    
    trial_start = globalClock.getTime()
    trial_start_lsl = local_clock()
    thisExp.addData("trial_start_elapsed", trial_start)
    thisExp.addData("trial_start_lsl", trial_start_lsl)
    
    #setup for el on/offset triggers
    #sound_trial_start.elOnsetDetected = False
    #sound_trial_start.elOffsetDetected = False
    
    #sound_no_resp.elOnsetDetected = False
    #sound_no_resp.elOffsetDetected = False
    dot.setPos((618, 0))
    grating_l.setContrast(leftCont)
    grating_l.setPos((-618, 0))
    grating_l.setPhase(random.random()*360)
    grating_r.setContrast(rightCont)
    grating_r.setPos((618, 0))
    grating_r.setPhase(random.random()*360)
    fixation.setColor([1,1,1], colorSpace='rgb')
    fixation.setSize((0.75, 0.75))
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    gotValidClick = False  # until a click is received
    sound_trial_start.setSound('5000', secs=0.1, hamming=True)
    sound_trial_start.setVolume(0.1, log=False)
    sound_no_resp.setSound('567', secs=0.5, hamming=True)
    sound_no_resp.setVolume(0.1, log=False)
    # keep track of which components have finished
    trialComponents = [stimulus_onset_tobii, dot, grating_l, grating_r, fixation, mouse, sound_trial_start, sound_no_resp, response_tobii]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *stimulus_onset_tobii* updates
        if stimulus_onset_tobii.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimulus_onset_tobii.frameNStart = frameN  # exact frame index
            stimulus_onset_tobii.tStart = t  # local t and not account for scr refresh
            stimulus_onset_tobii.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimulus_onset_tobii, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('stimulus_onset_tobii.started', t)
            stimulus_onset_tobii.status = STARTED
        if stimulus_onset_tobii.status == STARTED:
            if bool(moved == True):
                # keep track of stop time/frame for later
                stimulus_onset_tobii.tStop = t  # not accounting for scr refresh
                stimulus_onset_tobii.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('stimulus_onset_tobii.stopped', t)
                stimulus_onset_tobii.status = FINISHED
        # Run 'Each Frame' code from dragging_code
        #if sound_trial_start.tStartRefresh is not None and not sound_trial_start.elOnsetDetected:
            #el_tracker.sendMessage('signed_contrast %.2f' % signed_contrast)
            #el_tracker.sendMessage('stimOn')
            #el_tracker.sendMessage('sound_trial_start_ONSET')
            #sound_trial_start.elOnsetDetected = True
        
        #if sound_trial_start.tStopRefresh is not None and sound_trial_start.tStartRefresh is not None and not sound_trial_start.elOffsetDetected:
            #el_tracker.sendMessage('sound_trial_start_OFFSET')
            #sound_trial_start.elOffsetDetected = True 
        
        x = mouse.getPos()[0]
        
        if moved == False:
             mouseloc = mouse.getPos()
             if mouseloc[0] != mouserec[0] or mouseloc[1] != mouserec[1]:
                  moved = True
                  mouse_moved = globalClock.getTime()
                  mouse_moved_lsl = local_clock()
                  thisExp.addData("mouse_moved_elapsed", mouse_moved)
                  thisExp.addData("mouse_moved_lsl", mouse_moved_lsl)
                  thisExp.addData('reaction_time',round(t*1000))
                  #el_tracker.sendMessage('moveInit')
        
        x_r = x + 618
        x_l = x - 618
        
        grating_r.pos = (x_r,0)
        grating_l.pos = (x_l,0)
        
        if grating_r.overlaps(dot):
            dot.pos = grating_r.pos
        
        elif grating_l.overlaps(dot):
            dot.pos = grating_l.pos
        
        dot_trajectory.append(dot.pos[0])
        
        if eccentricity > 0:
            if grating_r.pos[0] <= r_lim_corr:
                correct = 1
                timeout=0
                response=1
                #el_tracker.sendMessage('response %i' % response)
                marker_manager.set_value(32)   # RIGHT
                thisExp.addData("response_time", round(t*1000))
                continueRoutine=False
            elif grating_r.pos[0] >= r_lim_wrong:
                correct = 0
                timeout=0
                response=-1
                #el_tracker.sendMessage('response %i' % response)
                marker_manager.set_value(32)   # RIGHT
                thisExp.addData("response_time", round(t*1000))
                continueRoutine=False
        elif eccentricity < 0:
            if grating_l.pos[0] >= l_lim_corr:
                correct = 1
                timeout=0
                response=-1
                #el_tracker.sendMessage('response %i' % response)
                marker_manager.set_value(31)   # LEFT
                thisExp.addData("response_time", round(t*1000))
                continueRoutine=False
            elif grating_l.pos[0] <= l_lim_wrong:
                correct = 0
                timeout=0
                response=1
                #el_tracker.sendMessage('response %i' % response)
                marker_manager.set_value(31)   # LEFT
                thisExp.addData("response_time", round(t*1000))
                continueRoutine=False
        
        
        if sound_no_resp.status == STARTED:
            correct = 'NaN'
            timeout = 1
            marker_manager.set_value(35)   # TIMEOUT
        
        
        #if sound_no_resp.tStartRefresh is not None and not sound_no_resp.elOnsetDetected:
            #el_tracker.sendMessage('timeout')
            #el_tracker.sendMessage('sound_no_resp_ONSET')
            #sound_no_resp.elOnsetDetected = True
        
        #if sound_no_resp.tStopRefresh is not None and sound_no_resp.tStartRefresh is not None and not sound_no_resp.elOffsetDetected:
            #el_tracker.sendMessage('sound_no_resp_OFFSET')
            #sound_no_resp.elOffsetDetected = True 
        
        
        # *dot* updates
        if dot.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dot.frameNStart = frameN  # exact frame index
            dot.tStart = t  # local t and not account for scr refresh
            dot.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dot, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dot.started')
            dot.setAutoDraw(True)
        if dot.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dot.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                dot.tStop = t  # not accounting for scr refresh
                dot.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dot.stopped')
                dot.setAutoDraw(False)
        
        # *grating_l* updates
        if grating_l.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            grating_l.frameNStart = frameN  # exact frame index
            grating_l.tStart = t  # local t and not account for scr refresh
            grating_l.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(grating_l, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'grating_l.started')
            grating_l.setAutoDraw(True)
        if grating_l.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > grating_l.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                grating_l.tStop = t  # not accounting for scr refresh
                grating_l.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'grating_l.stopped')
                grating_l.setAutoDraw(False)
        
        # *grating_r* updates
        if grating_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            grating_r.frameNStart = frameN  # exact frame index
            grating_r.tStart = t  # local t and not account for scr refresh
            grating_r.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(grating_r, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'grating_r.started')
            grating_r.setAutoDraw(True)
        if grating_r.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > grating_r.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                grating_r.tStop = t  # not accounting for scr refresh
                grating_r.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'grating_r.stopped')
                grating_r.setAutoDraw(False)
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation.started')
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.stopped')
                fixation.setAutoDraw(False)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                mouse.tStop = t  # not accounting for scr refresh
                mouse.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse.stopped', t)
                mouse.status = FINISHED
        if mouse.status == STARTED:  # only update if started and not finished!
            x, y = mouse.getPos()
            mouse.x.append(x)
            mouse.y.append(y)
            buttons = mouse.getPressed()
            mouse.leftButton.append(buttons[0])
            mouse.midButton.append(buttons[1])
            mouse.rightButton.append(buttons[2])
            mouse.time.append(globalClock.getTime())
        # start/stop sound_trial_start
        if sound_trial_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_trial_start.frameNStart = frameN  # exact frame index
            sound_trial_start.tStart = t  # local t and not account for scr refresh
            sound_trial_start.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_trial_start.started', tThisFlipGlobal)
            sound_trial_start.play(when=win)  # sync with win flip
        if sound_trial_start.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_trial_start.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                sound_trial_start.tStop = t  # not accounting for scr refresh
                sound_trial_start.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_trial_start.stopped')
                sound_trial_start.stop()
        # start/stop sound_no_resp
        if sound_no_resp.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            sound_no_resp.frameNStart = frameN  # exact frame index
            sound_no_resp.tStart = t  # local t and not account for scr refresh
            sound_no_resp.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_no_resp.started', tThisFlipGlobal)
            sound_no_resp.play(when=win)  # sync with win flip
        if sound_no_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_no_resp.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                sound_no_resp.tStop = t  # not accounting for scr refresh
                sound_no_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_no_resp.stopped')
                sound_no_resp.stop()
        # *response_tobii* updates
        if response_tobii.status == NOT_STARTED and moved == True:
            # keep track of start time/frame for later
            response_tobii.frameNStart = frameN  # exact frame index
            response_tobii.tStart = t  # local t and not account for scr refresh
            response_tobii.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_tobii, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('response_tobii.started', t)
            response_tobii.status = STARTED
        if response_tobii.status == STARTED:
            if bool(continueRoutine == False):
                # keep track of stop time/frame for later
                response_tobii.tStop = t  # not accounting for scr refresh
                response_tobii.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('response_tobii.stopped', t)
                response_tobii.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if stimulus_onset_tobii.status != FINISHED:
        stimulus_onset_tobii.status = FINISHED
    # Run 'End Routine' code from dragging_code
    end_trial = globalClock.getTime()
    end_trial_lsl = local_clock()
    thisExp.addData("trial_end_elapsed", end_trial)
    thisExp.addData("trial_end_lsl", end_trial_lsl)
    
    
    thisExp.addData("correct", correct)
    thisExp.addData('timeout', timeout)
    thisExp.addData("dot_trajectory", dot_trajectory)
    
    timing.delay(100)
    marker_manager.set_value(0)
    
    # store data for trials_2 (TrialHandler)
    trials_2.addData('mouse.x', mouse.x)
    trials_2.addData('mouse.y', mouse.y)
    trials_2.addData('mouse.leftButton', mouse.leftButton)
    trials_2.addData('mouse.midButton', mouse.midButton)
    trials_2.addData('mouse.rightButton', mouse.rightButton)
    trials_2.addData('mouse.time', mouse.time)
    sound_trial_start.stop()  # ensure sound has stopped at end of routine
    sound_no_resp.stop()  # ensure sound has stopped at end of routine
    # make sure the eyetracker recording stops
    if response_tobii.status != FINISHED:
        response_tobii.status = FINISHED
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    mouse.setPos(newPos=(0, 0))
    
    #el_tracker.sendMessage('feedbackType %s' % correct)
    
    if correct==1:
        fb_sound = "2000.wav"
        fb_sound_dur = 0.2
        fb_dur = 1
        fb_volume = 0.1
        tot_points += 1
        marker_manager.set_value(41)
        timing.delay(100)
        marker_manager.set_value(0)
        
    elif correct==0:
        fb_sound = "whitenoise.wav"
        fb_sound_dur = 0.5
        fb_dur = 2
        fb_volume = 0.1
        marker_manager.set_value(42)
        timing.delay(100)
        marker_manager.set_value(0)
        
    else:
        fb_sound = 200
        fb_sound_dur = 0.1
        fb_dur = 1.5
        fb_volume = 0
        marker_manager.set_value(45)
        timing.delay(100)
        marker_manager.set_value(0)
        
    #fixation_3.elOnsetDetected = False
    #fixation_3.elOffsetDetected = False
    
    #feedback_sound.elOnsetDetected = False
    #feedback_sound.elOffsetDetected = False
    feedback_sound.setSound(fb_sound, secs=fb_sound_dur, hamming=True)
    feedback_sound.setVolume(fb_volume, log=False)
    # Run 'Begin Routine' code from feedback_timing
    # Feedback start: elapsed experiment time
    feedback_start = globalClock.getTime()
    
    # Feedback start: LSL-aligned time
    feedback_start_lsl = local_clock()
    
    thisExp.addData("feedback_start_elapsed", feedback_start)
    thisExp.addData("feedback_start_lsl", feedback_start_lsl)
    # keep track of which components have finished
    feedbackComponents = [feedback_tobii, feedback_sound, fixation_3]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *feedback_tobii* updates
        if feedback_tobii.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_tobii.frameNStart = frameN  # exact frame index
            feedback_tobii.tStart = t  # local t and not account for scr refresh
            feedback_tobii.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_tobii, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('feedback_tobii.started', t)
            feedback_tobii.status = STARTED
        if feedback_tobii.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_tobii.tStartRefresh + fb_sound_dur-frameTolerance:
                # keep track of stop time/frame for later
                feedback_tobii.tStop = t  # not accounting for scr refresh
                feedback_tobii.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('feedback_tobii.stopped', t)
                feedback_tobii.status = FINISHED
        # Run 'Each Frame' code from feedback_code
        mouse.setPos(newPos=(0, 0))
        
        #if fixation_3.tStartRefresh is not None and not fixation_3.elOnsetDetected:
            #el_tracker.sendMessage('%i %s_ONSET' % (int(round((globalClock.getTime()-fixation_3.tStartRefresh)*1000)),fixation_3.name))
            #fixation_3.elOnsetDetected = True
        
        #if fixation_3.tStopRefresh is not None and fixation_3.tStartRefresh is not None and not fixation_3.elOffsetDetected:
            #el_tracker.sendMessage('%i %s_OFFSET' % (int(round((globalClock.getTime()-fixation_3.tStopRefresh)*1000)),fixation_3.name))
            #fixation_3.elOffsetDetected = True 
        
        #if feedback_sound.tStartRefresh is not None and not feedback_sound.elOnsetDetected:
            #el_tracker.sendMessage('feedback_sound_ONSET')
            #feedback_sound.elOnsetDetected = True
        
        #if feedback_sound.tStopRefresh is not None and feedback_sound.tStartRefresh is not None and not feedback_sound.elOffsetDetected:
            #el_tracker.sendMessage('feedback_sound_OFFSET')
            #feedback_sound.elOffsetDetected = True 
        # start/stop feedback_sound
        if feedback_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_sound.frameNStart = frameN  # exact frame index
            feedback_sound.tStart = t  # local t and not account for scr refresh
            feedback_sound.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('feedback_sound.started', tThisFlipGlobal)
            feedback_sound.play(when=win)  # sync with win flip
        if feedback_sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_sound.tStartRefresh + fb_sound_dur-frameTolerance:
                # keep track of stop time/frame for later
                feedback_sound.tStop = t  # not accounting for scr refresh
                feedback_sound.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_sound.stopped')
                feedback_sound.stop()
        
        # *fixation_3* updates
        if fixation_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_3.frameNStart = frameN  # exact frame index
            fixation_3.tStart = t  # local t and not account for scr refresh
            fixation_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_3.started')
            fixation_3.setAutoDraw(True)
        if fixation_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_3.tStartRefresh + fb_dur-frameTolerance:
                # keep track of stop time/frame for later
                fixation_3.tStop = t  # not accounting for scr refresh
                fixation_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_3.stopped')
                fixation_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if feedback_tobii.status != FINISHED:
        feedback_tobii.status = FINISHED
    # Run 'End Routine' code from feedback_code
    
    
    
    feedback_sound.stop()  # ensure sound has stopped at end of routine
    # Run 'End Routine' code from feedback_timing
    # Feedback stop: elapsed experiment time
    feedback_stop = globalClock.getTime()
    
    # Feedback stop: LSL-aligned time
    feedback_stop_lsl = local_clock()
    
    thisExp.addData("feedback_stop_elapsed", feedback_stop)
    thisExp.addData("feedback_stop_lsl", feedback_stop_lsl)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'

# get names of stimulus parameters
if trials_2.trialList in ([], [None], None):
    params = []
else:
    params = trials_2.trialList[0].keys()
# save data for this loop
trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "record_delay" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_4
marker_manager.set_value(90)
timing.delay(100)
marker_manager.set_value(0)
# keep track of which components have finished
record_delayComponents = [blank_txt]
for thisComponent in record_delayComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "record_delay" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blank_txt* updates
    if blank_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blank_txt.frameNStart = frameN  # exact frame index
        blank_txt.tStart = t  # local t and not account for scr refresh
        blank_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'blank_txt.started')
        blank_txt.setAutoDraw(True)
    if blank_txt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blank_txt.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            blank_txt.tStop = t  # not accounting for scr refresh
            blank_txt.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_txt.stopped')
            blank_txt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in record_delayComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "record_delay" ---
for thisComponent in record_delayComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "end_task" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from mouse_visible_7
win.mouseVisible = True
# Run 'Begin Routine' code from end_session_timer_2
thisExp.addData('session_end', data.getDateStr())

thisExp.addData('total_points', tot_points)

tobii_stop_elapsed = globalClock.getTime()
tobii_stop_lsl = local_clock()
thisExp.addData("tobii_record_stop_elapsed", tobii_stop_elapsed)
thisExp.addData("tobii_record_stop_lsl", tobii_stop_lsl)
# setup some python lists for storing info about the mouse_26
mouse_26.x = []
mouse_26.y = []
mouse_26.leftButton = []
mouse_26.midButton = []
mouse_26.rightButton = []
mouse_26.time = []
mouse_26.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
end_taskComponents = [end_task_txt, continue_txt_22, mouse_26, tobii_stop]
for thisComponent in end_taskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "end_task" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_task_txt* updates
    if end_task_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_task_txt.frameNStart = frameN  # exact frame index
        end_task_txt.tStart = t  # local t and not account for scr refresh
        end_task_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_task_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_task_txt.started')
        end_task_txt.setAutoDraw(True)
    
    # *continue_txt_22* updates
    if continue_txt_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_22.frameNStart = frameN  # exact frame index
        continue_txt_22.tStart = t  # local t and not account for scr refresh
        continue_txt_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_22, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_22.started')
        continue_txt_22.setAutoDraw(True)
    # *mouse_26* updates
    if mouse_26.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_26.frameNStart = frameN  # exact frame index
        mouse_26.tStart = t  # local t and not account for scr refresh
        mouse_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_26, 'tStartRefresh')  # time at next scr refresh
        mouse_26.status = STARTED
        mouse_26.mouseClock.reset()
        prevButtonState = mouse_26.getPressed()  # if button is down already this ISN'T a new click
    if mouse_26.status == STARTED:  # only update if started and not finished!
        buttons = mouse_26.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_22)
                    clickableList = continue_txt_22
                except:
                    clickableList = [continue_txt_22]
                for obj in clickableList:
                    if obj.contains(mouse_26):
                        gotValidClick = True
                        mouse_26.clicked_name.append(obj.name)
                x, y = mouse_26.getPos()
                mouse_26.x.append(x)
                mouse_26.y.append(y)
                buttons = mouse_26.getPressed()
                mouse_26.leftButton.append(buttons[0])
                mouse_26.midButton.append(buttons[1])
                mouse_26.rightButton.append(buttons[2])
                mouse_26.time.append(mouse_26.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    # *tobii_stop* updates
    if tobii_stop.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tobii_stop.frameNStart = frameN  # exact frame index
        tobii_stop.tStart = t  # local t and not account for scr refresh
        tobii_stop.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tobii_stop, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('tobii_stop.started', t)
        tobii_stop.status = STARTED
    if tobii_stop.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tobii_stop.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            tobii_stop.tStop = t  # not accounting for scr refresh
            tobii_stop.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('tobii_stop.stopped', t)
            tobii_stop.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_taskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end_task" ---
for thisComponent in end_taskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_26.x', mouse_26.x)
thisExp.addData('mouse_26.y', mouse_26.y)
thisExp.addData('mouse_26.leftButton', mouse_26.leftButton)
thisExp.addData('mouse_26.midButton', mouse_26.midButton)
thisExp.addData('mouse_26.rightButton', mouse_26.rightButton)
thisExp.addData('mouse_26.time', mouse_26.time)
thisExp.addData('mouse_26.clicked_name', mouse_26.clicked_name)
thisExp.nextEntry()
# make sure the eyetracker recording stops
if tobii_stop.status != FINISHED:
    tobii_stop.status = FINISHED
# the Routine "end_task" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "question1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
textbox1.reset()
# setup some python lists for storing info about the mouse_27
mouse_27.x = []
mouse_27.y = []
mouse_27.leftButton = []
mouse_27.midButton = []
mouse_27.rightButton = []
mouse_27.time = []
mouse_27.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
question1Components = [q1_txt, textbox1, continue_txt_23, mouse_27]
for thisComponent in question1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "question1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *q1_txt* updates
    if q1_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        q1_txt.frameNStart = frameN  # exact frame index
        q1_txt.tStart = t  # local t and not account for scr refresh
        q1_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(q1_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'q1_txt.started')
        q1_txt.setAutoDraw(True)
    
    # *textbox1* updates
    if textbox1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox1.frameNStart = frameN  # exact frame index
        textbox1.tStart = t  # local t and not account for scr refresh
        textbox1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox1.started')
        textbox1.setAutoDraw(True)
    
    # *continue_txt_23* updates
    if continue_txt_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_23.frameNStart = frameN  # exact frame index
        continue_txt_23.tStart = t  # local t and not account for scr refresh
        continue_txt_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_23, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_23.started')
        continue_txt_23.setAutoDraw(True)
    # *mouse_27* updates
    if mouse_27.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_27.frameNStart = frameN  # exact frame index
        mouse_27.tStart = t  # local t and not account for scr refresh
        mouse_27.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_27, 'tStartRefresh')  # time at next scr refresh
        mouse_27.status = STARTED
        mouse_27.mouseClock.reset()
        prevButtonState = mouse_27.getPressed()  # if button is down already this ISN'T a new click
    if mouse_27.status == STARTED:  # only update if started and not finished!
        buttons = mouse_27.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_23)
                    clickableList = continue_txt_23
                except:
                    clickableList = [continue_txt_23]
                for obj in clickableList:
                    if obj.contains(mouse_27):
                        gotValidClick = True
                        mouse_27.clicked_name.append(obj.name)
                x, y = mouse_27.getPos()
                mouse_27.x.append(x)
                mouse_27.y.append(y)
                buttons = mouse_27.getPressed()
                mouse_27.leftButton.append(buttons[0])
                mouse_27.midButton.append(buttons[1])
                mouse_27.rightButton.append(buttons[2])
                mouse_27.time.append(mouse_27.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in question1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "question1" ---
for thisComponent in question1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textbox1.text',textbox1.text)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_27.x', mouse_27.x)
thisExp.addData('mouse_27.y', mouse_27.y)
thisExp.addData('mouse_27.leftButton', mouse_27.leftButton)
thisExp.addData('mouse_27.midButton', mouse_27.midButton)
thisExp.addData('mouse_27.rightButton', mouse_27.rightButton)
thisExp.addData('mouse_27.time', mouse_27.time)
thisExp.addData('mouse_27.clicked_name', mouse_27.clicked_name)
thisExp.nextEntry()
# the Routine "question1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "question2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
textbox2.reset()
# setup some python lists for storing info about the mouse_28
mouse_28.x = []
mouse_28.y = []
mouse_28.leftButton = []
mouse_28.midButton = []
mouse_28.rightButton = []
mouse_28.time = []
mouse_28.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
question2Components = [q2_txt, textbox2, continue_txt_24, mouse_28]
for thisComponent in question2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "question2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *q2_txt* updates
    if q2_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        q2_txt.frameNStart = frameN  # exact frame index
        q2_txt.tStart = t  # local t and not account for scr refresh
        q2_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(q2_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'q2_txt.started')
        q2_txt.setAutoDraw(True)
    
    # *textbox2* updates
    if textbox2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox2.frameNStart = frameN  # exact frame index
        textbox2.tStart = t  # local t and not account for scr refresh
        textbox2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox2.started')
        textbox2.setAutoDraw(True)
    
    # *continue_txt_24* updates
    if continue_txt_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_24.frameNStart = frameN  # exact frame index
        continue_txt_24.tStart = t  # local t and not account for scr refresh
        continue_txt_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_24, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_24.started')
        continue_txt_24.setAutoDraw(True)
    # *mouse_28* updates
    if mouse_28.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_28.frameNStart = frameN  # exact frame index
        mouse_28.tStart = t  # local t and not account for scr refresh
        mouse_28.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_28, 'tStartRefresh')  # time at next scr refresh
        mouse_28.status = STARTED
        mouse_28.mouseClock.reset()
        prevButtonState = mouse_28.getPressed()  # if button is down already this ISN'T a new click
    if mouse_28.status == STARTED:  # only update if started and not finished!
        buttons = mouse_28.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_24)
                    clickableList = continue_txt_24
                except:
                    clickableList = [continue_txt_24]
                for obj in clickableList:
                    if obj.contains(mouse_28):
                        gotValidClick = True
                        mouse_28.clicked_name.append(obj.name)
                x, y = mouse_28.getPos()
                mouse_28.x.append(x)
                mouse_28.y.append(y)
                buttons = mouse_28.getPressed()
                mouse_28.leftButton.append(buttons[0])
                mouse_28.midButton.append(buttons[1])
                mouse_28.rightButton.append(buttons[2])
                mouse_28.time.append(mouse_28.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in question2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "question2" ---
for thisComponent in question2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textbox2.text',textbox2.text)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_28.x', mouse_28.x)
thisExp.addData('mouse_28.y', mouse_28.y)
thisExp.addData('mouse_28.leftButton', mouse_28.leftButton)
thisExp.addData('mouse_28.midButton', mouse_28.midButton)
thisExp.addData('mouse_28.rightButton', mouse_28.rightButton)
thisExp.addData('mouse_28.time', mouse_28.time)
thisExp.addData('mouse_28.clicked_name', mouse_28.clicked_name)
thisExp.nextEntry()
# the Routine "question2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "question3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
textbox3.reset()
# setup some python lists for storing info about the mouse_29
mouse_29.x = []
mouse_29.y = []
mouse_29.leftButton = []
mouse_29.midButton = []
mouse_29.rightButton = []
mouse_29.time = []
mouse_29.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
question3Components = [q3_txt, textbox3, continue_txt_25, mouse_29]
for thisComponent in question3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "question3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *q3_txt* updates
    if q3_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        q3_txt.frameNStart = frameN  # exact frame index
        q3_txt.tStart = t  # local t and not account for scr refresh
        q3_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(q3_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'q3_txt.started')
        q3_txt.setAutoDraw(True)
    
    # *textbox3* updates
    if textbox3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox3.frameNStart = frameN  # exact frame index
        textbox3.tStart = t  # local t and not account for scr refresh
        textbox3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox3.started')
        textbox3.setAutoDraw(True)
    
    # *continue_txt_25* updates
    if continue_txt_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_25.frameNStart = frameN  # exact frame index
        continue_txt_25.tStart = t  # local t and not account for scr refresh
        continue_txt_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_25, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_25.started')
        continue_txt_25.setAutoDraw(True)
    # *mouse_29* updates
    if mouse_29.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_29.frameNStart = frameN  # exact frame index
        mouse_29.tStart = t  # local t and not account for scr refresh
        mouse_29.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_29, 'tStartRefresh')  # time at next scr refresh
        mouse_29.status = STARTED
        mouse_29.mouseClock.reset()
        prevButtonState = mouse_29.getPressed()  # if button is down already this ISN'T a new click
    if mouse_29.status == STARTED:  # only update if started and not finished!
        buttons = mouse_29.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_25)
                    clickableList = continue_txt_25
                except:
                    clickableList = [continue_txt_25]
                for obj in clickableList:
                    if obj.contains(mouse_29):
                        gotValidClick = True
                        mouse_29.clicked_name.append(obj.name)
                x, y = mouse_29.getPos()
                mouse_29.x.append(x)
                mouse_29.y.append(y)
                buttons = mouse_29.getPressed()
                mouse_29.leftButton.append(buttons[0])
                mouse_29.midButton.append(buttons[1])
                mouse_29.rightButton.append(buttons[2])
                mouse_29.time.append(mouse_29.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in question3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "question3" ---
for thisComponent in question3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textbox3.text',textbox3.text)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_29.x', mouse_29.x)
thisExp.addData('mouse_29.y', mouse_29.y)
thisExp.addData('mouse_29.leftButton', mouse_29.leftButton)
thisExp.addData('mouse_29.midButton', mouse_29.midButton)
thisExp.addData('mouse_29.rightButton', mouse_29.rightButton)
thisExp.addData('mouse_29.time', mouse_29.time)
thisExp.addData('mouse_29.clicked_name', mouse_29.clicked_name)
thisExp.nextEntry()
# the Routine "question3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "question4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
textbox4.reset()
# setup some python lists for storing info about the mouse_30
mouse_30.x = []
mouse_30.y = []
mouse_30.leftButton = []
mouse_30.midButton = []
mouse_30.rightButton = []
mouse_30.time = []
mouse_30.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
question4Components = [q4_txt, textbox4, continue_txt_26, mouse_30]
for thisComponent in question4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "question4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *q4_txt* updates
    if q4_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        q4_txt.frameNStart = frameN  # exact frame index
        q4_txt.tStart = t  # local t and not account for scr refresh
        q4_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(q4_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'q4_txt.started')
        q4_txt.setAutoDraw(True)
    
    # *textbox4* updates
    if textbox4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox4.frameNStart = frameN  # exact frame index
        textbox4.tStart = t  # local t and not account for scr refresh
        textbox4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox4.started')
        textbox4.setAutoDraw(True)
    
    # *continue_txt_26* updates
    if continue_txt_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_26.frameNStart = frameN  # exact frame index
        continue_txt_26.tStart = t  # local t and not account for scr refresh
        continue_txt_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_26, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_26.started')
        continue_txt_26.setAutoDraw(True)
    # *mouse_30* updates
    if mouse_30.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_30.frameNStart = frameN  # exact frame index
        mouse_30.tStart = t  # local t and not account for scr refresh
        mouse_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_30, 'tStartRefresh')  # time at next scr refresh
        mouse_30.status = STARTED
        mouse_30.mouseClock.reset()
        prevButtonState = mouse_30.getPressed()  # if button is down already this ISN'T a new click
    if mouse_30.status == STARTED:  # only update if started and not finished!
        buttons = mouse_30.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_26)
                    clickableList = continue_txt_26
                except:
                    clickableList = [continue_txt_26]
                for obj in clickableList:
                    if obj.contains(mouse_30):
                        gotValidClick = True
                        mouse_30.clicked_name.append(obj.name)
                x, y = mouse_30.getPos()
                mouse_30.x.append(x)
                mouse_30.y.append(y)
                buttons = mouse_30.getPressed()
                mouse_30.leftButton.append(buttons[0])
                mouse_30.midButton.append(buttons[1])
                mouse_30.rightButton.append(buttons[2])
                mouse_30.time.append(mouse_30.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in question4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "question4" ---
for thisComponent in question4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textbox4.text',textbox4.text)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_30.x', mouse_30.x)
thisExp.addData('mouse_30.y', mouse_30.y)
thisExp.addData('mouse_30.leftButton', mouse_30.leftButton)
thisExp.addData('mouse_30.midButton', mouse_30.midButton)
thisExp.addData('mouse_30.rightButton', mouse_30.rightButton)
thisExp.addData('mouse_30.time', mouse_30.time)
thisExp.addData('mouse_30.clicked_name', mouse_30.clicked_name)
thisExp.nextEntry()
# the Routine "question4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "question5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
textbox5.reset()
# setup some python lists for storing info about the mouse_33
mouse_33.x = []
mouse_33.y = []
mouse_33.leftButton = []
mouse_33.midButton = []
mouse_33.rightButton = []
mouse_33.time = []
mouse_33.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
question5Components = [q5_txt, textbox5, continue_txt_29, mouse_33]
for thisComponent in question5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "question5" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *q5_txt* updates
    if q5_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        q5_txt.frameNStart = frameN  # exact frame index
        q5_txt.tStart = t  # local t and not account for scr refresh
        q5_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(q5_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'q5_txt.started')
        q5_txt.setAutoDraw(True)
    
    # *textbox5* updates
    if textbox5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox5.frameNStart = frameN  # exact frame index
        textbox5.tStart = t  # local t and not account for scr refresh
        textbox5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textbox5.started')
        textbox5.setAutoDraw(True)
    
    # *continue_txt_29* updates
    if continue_txt_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_29.frameNStart = frameN  # exact frame index
        continue_txt_29.tStart = t  # local t and not account for scr refresh
        continue_txt_29.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_29, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_29.started')
        continue_txt_29.setAutoDraw(True)
    # *mouse_33* updates
    if mouse_33.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_33.frameNStart = frameN  # exact frame index
        mouse_33.tStart = t  # local t and not account for scr refresh
        mouse_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_33, 'tStartRefresh')  # time at next scr refresh
        mouse_33.status = STARTED
        mouse_33.mouseClock.reset()
        prevButtonState = mouse_33.getPressed()  # if button is down already this ISN'T a new click
    if mouse_33.status == STARTED:  # only update if started and not finished!
        buttons = mouse_33.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_29)
                    clickableList = continue_txt_29
                except:
                    clickableList = [continue_txt_29]
                for obj in clickableList:
                    if obj.contains(mouse_33):
                        gotValidClick = True
                        mouse_33.clicked_name.append(obj.name)
                x, y = mouse_33.getPos()
                mouse_33.x.append(x)
                mouse_33.y.append(y)
                buttons = mouse_33.getPressed()
                mouse_33.leftButton.append(buttons[0])
                mouse_33.midButton.append(buttons[1])
                mouse_33.rightButton.append(buttons[2])
                mouse_33.time.append(mouse_33.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in question5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "question5" ---
for thisComponent in question5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textbox5.text',textbox5.text)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_33.x', mouse_33.x)
thisExp.addData('mouse_33.y', mouse_33.y)
thisExp.addData('mouse_33.leftButton', mouse_33.leftButton)
thisExp.addData('mouse_33.midButton', mouse_33.midButton)
thisExp.addData('mouse_33.rightButton', mouse_33.rightButton)
thisExp.addData('mouse_33.time', mouse_33.time)
thisExp.addData('mouse_33.clicked_name', mouse_33.clicked_name)
thisExp.nextEntry()
# the Routine "question5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "end_exp" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
end_exp_txt.setText(f'You have reached the end of the experiment. \n\n You collected {str(tot_points)} points out of 600. \n Thank you very much for participating! \n\n Once you have closed the experiment, you can leave the room. \n The experimenter will then give you more information and answer any questions you may have. \n\n Click Finish to save your data and exit the experiment.')
# setup some python lists for storing info about the mouse_31
mouse_31.x = []
mouse_31.y = []
mouse_31.leftButton = []
mouse_31.midButton = []
mouse_31.rightButton = []
mouse_31.time = []
mouse_31.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
end_expComponents = [end_exp_txt, continue_txt_27, mouse_31]
for thisComponent in end_expComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "end_exp" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_exp_txt* updates
    if end_exp_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_exp_txt.frameNStart = frameN  # exact frame index
        end_exp_txt.tStart = t  # local t and not account for scr refresh
        end_exp_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_exp_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_exp_txt.started')
        end_exp_txt.setAutoDraw(True)
    
    # *continue_txt_27* updates
    if continue_txt_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_txt_27.frameNStart = frameN  # exact frame index
        continue_txt_27.tStart = t  # local t and not account for scr refresh
        continue_txt_27.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_txt_27, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'continue_txt_27.started')
        continue_txt_27.setAutoDraw(True)
    # *mouse_31* updates
    if mouse_31.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_31.frameNStart = frameN  # exact frame index
        mouse_31.tStart = t  # local t and not account for scr refresh
        mouse_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_31, 'tStartRefresh')  # time at next scr refresh
        mouse_31.status = STARTED
        mouse_31.mouseClock.reset()
        prevButtonState = mouse_31.getPressed()  # if button is down already this ISN'T a new click
    if mouse_31.status == STARTED:  # only update if started and not finished!
        buttons = mouse_31.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(continue_txt_27)
                    clickableList = continue_txt_27
                except:
                    clickableList = [continue_txt_27]
                for obj in clickableList:
                    if obj.contains(mouse_31):
                        gotValidClick = True
                        mouse_31.clicked_name.append(obj.name)
                x, y = mouse_31.getPos()
                mouse_31.x.append(x)
                mouse_31.y.append(y)
                buttons = mouse_31.getPressed()
                mouse_31.leftButton.append(buttons[0])
                mouse_31.midButton.append(buttons[1])
                mouse_31.rightButton.append(buttons[2])
                mouse_31.time.append(mouse_31.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_expComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end_exp" ---
for thisComponent in end_expComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_31.x', mouse_31.x)
thisExp.addData('mouse_31.y', mouse_31.y)
thisExp.addData('mouse_31.leftButton', mouse_31.leftButton)
thisExp.addData('mouse_31.midButton', mouse_31.midButton)
thisExp.addData('mouse_31.rightButton', mouse_31.rightButton)
thisExp.addData('mouse_31.time', mouse_31.time)
thisExp.addData('mouse_31.clicked_name', mouse_31.clicked_name)
thisExp.nextEntry()
# the Routine "end_exp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# Run 'End Experiment' code from code_3
# Save the marker table. In the current example:
# - The filename of the marker table is the same as the default data filename, 
#   appended with '_marker_table'. 
# - The location of the marker table is the same as the location of the other 
#   data (in the data folder in the current working directory). 
# - Additional information is saved in the header of the marker table file, 
#   namely the participant and experiment name.
cur_filename =  expInfo['participant'] + '_' + expName + '_' + expInfo['date'] + '_marker_table'
cur_location = os.getcwd() + '\data'
cur_more_info = {'participant': expInfo['participant'], 'experiment': expName}
marker_manager.save_marker_table(cur_filename, cur_location, cur_more_info)

# Close marker device.
marker_manager.close()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
