#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on January 12, 2021, at 17:30
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

msg=''


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'آزمون استروپ استاندارد'  # from the Builder filename that created this script
expInfo = {'نام': '', 'نام خانوادگی': '', 'کلاس': '', 'سن': '', 'چندمین بار است که در این تست شرکت می کنید': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['نام'], expInfo['نام خانوادگی'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\pythonproject\\stroopexperiment\\stroopExperiment_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructionPractice"
instructionPracticeClock = core.Clock()
instrTxt1 = visual.TextStim(win=win, name='instrTxt1',
    text='این بخش تمرینی است تا با آزمون آشنا شوید\n\nبخاطر داشته باش، واژه ها را در نظر نگیر و \nرنگها را انتخاب کن\n\n\nبرای ادامه شروع را انتخاب کنید\nESC=خروج',
    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);
imgStart1 = visual.ImageStim(
    win=win,
    name='imgStart1', units='pix', 
    image='Start.jpg', mask=None,
    ori=0, pos=[0, -310], size=[125, 125],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
resBegin1 = event.Mouse(win=win)
x, y = [None, None]
resBegin1.mouseClock = core.Clock()

# Initialize components for Routine "trial"
trialClock = core.Clock()
targetTxt = visual.TextStim(win=win, name='targetTxt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);
imgRed = visual.ImageStim(
    win=win,
    name='imgRed', units='pix', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
imgBlue = visual.ImageStim(
    win=win,
    name='imgBlue', units='pix', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
imgGreen = visual.ImageStim(
    win=win,
    name='imgGreen', units='pix', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
imgYellow = visual.ImageStim(
    win=win,
    name='imgYellow', units='pix', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
#msg variable just needs some value at start

msg=''
feedbackTxt = visual.TextStim(win=win, name='feedbackTxt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-1.0);

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
instrTxt = visual.TextStim(win=win, name='instrTxt',
    text='برای مواجهه با یک آزمون چالشی جدید آماده ای؟\n\nبخاطر داشته باش، واژه ها را در نظر نگیر و \nرنگها را انتخاب کن\n\n\nبرای ادامه شروع را انتخاب کنید\n',
    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);
imgStart = visual.ImageStim(
    win=win,
    name='imgStart', units='pix', 
    image='Start.jpg', mask=None,
    ori=0, pos=[0, -310], size=[125, 125],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
resBegin = event.Mouse(win=win)
x, y = [None, None]
resBegin.mouseClock = core.Clock()

# Initialize components for Routine "trial"
trialClock = core.Clock()
targetTxt = visual.TextStim(win=win, name='targetTxt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);
imgRed = visual.ImageStim(
    win=win,
    name='imgRed', units='pix', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
imgBlue = visual.ImageStim(
    win=win,
    name='imgBlue', units='pix', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
imgGreen = visual.ImageStim(
    win=win,
    name='imgGreen', units='pix', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
imgYellow = visual.ImageStim(
    win=win,
    name='imgYellow', units='pix', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanksText = visual.TextStim(win=win, name='thanksText',
    text='پایان آزمون\n\nاز شما بسیار سپاسگزاریم!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructionPractice"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the resBegin1
resBegin1.x = []
resBegin1.y = []
resBegin1.leftButton = []
resBegin1.midButton = []
resBegin1.rightButton = []
resBegin1.time = []
resBegin1.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructionPracticeComponents = [instrTxt1, imgStart1, resBegin1]
for thisComponent in instructionPracticeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionPracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructionPractice"-------
while continueRoutine:
    # get current time
    t = instructionPracticeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionPracticeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrTxt1* updates
    if instrTxt1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrTxt1.frameNStart = frameN  # exact frame index
        instrTxt1.tStart = t  # local t and not account for scr refresh
        instrTxt1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrTxt1, 'tStartRefresh')  # time at next scr refresh
        instrTxt1.setAutoDraw(True)
    
    # *imgStart1* updates
    if imgStart1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        imgStart1.frameNStart = frameN  # exact frame index
        imgStart1.tStart = t  # local t and not account for scr refresh
        imgStart1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imgStart1, 'tStartRefresh')  # time at next scr refresh
        imgStart1.setAutoDraw(True)
    # *resBegin1* updates
    if resBegin1.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resBegin1.frameNStart = frameN  # exact frame index
        resBegin1.tStart = t  # local t and not account for scr refresh
        resBegin1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resBegin1, 'tStartRefresh')  # time at next scr refresh
        resBegin1.status = STARTED
        resBegin1.mouseClock.reset()
        prevButtonState = resBegin1.getPressed()  # if button is down already this ISN'T a new click
    if resBegin1.status == STARTED:  # only update if started and not finished!
        buttons = resBegin1.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [imgStart]:
                    if obj.contains(resBegin1):
                        gotValidClick = True
                        resBegin1.clicked_name.append(obj.name)
                x, y = resBegin1.getPos()
                resBegin1.x.append(x)
                resBegin1.y.append(y)
                buttons = resBegin1.getPressed()
                resBegin1.leftButton.append(buttons[0])
                resBegin1.midButton.append(buttons[1])
                resBegin1.rightButton.append(buttons[2])
                resBegin1.time.append(resBegin1.mouseClock.getTime())
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionPracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructionPractice"-------
for thisComponent in instructionPracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instrTxt1.started', instrTxt1.tStartRefresh)
thisExp.addData('instrTxt1.stopped', instrTxt1.tStopRefresh)
thisExp.addData('imgStart1.started', imgStart1.tStartRefresh)
thisExp.addData('imgStart1.stopped', imgStart1.tStopRefresh)
# store data for thisExp (ExperimentHandler)
if len(resBegin1.x): thisExp.addData('resBegin1.x', resBegin1.x[0])
if len(resBegin1.y): thisExp.addData('resBegin1.y', resBegin1.y[0])
if len(resBegin1.leftButton): thisExp.addData('resBegin1.leftButton', resBegin1.leftButton[0])
if len(resBegin1.midButton): thisExp.addData('resBegin1.midButton', resBegin1.midButton[0])
if len(resBegin1.rightButton): thisExp.addData('resBegin1.rightButton', resBegin1.rightButton[0])
if len(resBegin1.time): thisExp.addData('resBegin1.time', resBegin1.time[0])
if len(resBegin1.clicked_name): thisExp.addData('resBegin1.clicked_name', resBegin1.clicked_name[0])
thisExp.addData('resBegin1.started', resBegin1.tStart)
thisExp.addData('resBegin1.stopped', resBegin1.tStop)
thisExp.nextEntry()
# the Routine "instructionPractice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practisTrials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice.xlsx'),
    seed=None, name='practisTrials')
thisExp.addLoop(practisTrials)  # add the loop to the experiment
thisPractisTrial = practisTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractisTrial.rgb)
if thisPractisTrial != None:
    for paramName in thisPractisTrial:
        exec('{} = thisPractisTrial[paramName]'.format(paramName))

for thisPractisTrial in practisTrials:
    currentLoop = practisTrials
    # abbreviate parameter names if possible (e.g. rgb = thisPractisTrial.rgb)
    if thisPractisTrial != None:
        for paramName in thisPractisTrial:
            exec('{} = thisPractisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    targetTxt.setColor(colour, colorSpace='rgb')
    targetTxt.setText(word)
    imgRed.setOpacity(1)
    imgRed.setPos((-250, -200))
    imgRed.setSize([125, 125])
    imgRed.setOri(0)
    imgRed.setImage('Red.jpg')
    imgBlue.setOpacity(1)
    imgBlue.setPos((-100, -200))
    imgBlue.setSize([125, 125])
    imgBlue.setOri(1)
    imgBlue.setImage('Blue.jpg')
    imgGreen.setOpacity(1)
    imgGreen.setPos((50, -200))
    imgGreen.setSize([125, 125])
    imgGreen.setOri(2)
    imgGreen.setImage('Green.jpg')
    imgYellow.setOpacity(1)
    imgYellow.setPos((200, -200))
    imgYellow.setSize([125, 125])
    imgYellow.setOri(3)
    imgYellow.setImage('Yellow.jpg')
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    trialComponents = [targetTxt, imgRed, imgBlue, imgGreen, imgYellow, mouse]
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
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *targetTxt* updates
        if targetTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            targetTxt.frameNStart = frameN  # exact frame index
            targetTxt.tStart = t  # local t and not account for scr refresh
            targetTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(targetTxt, 'tStartRefresh')  # time at next scr refresh
            targetTxt.setAutoDraw(True)
        if targetTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > targetTxt.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                targetTxt.tStop = t  # not accounting for scr refresh
                targetTxt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(targetTxt, 'tStopRefresh')  # time at next scr refresh
                targetTxt.setAutoDraw(False)
        
        # *imgRed* updates
        if imgRed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imgRed.frameNStart = frameN  # exact frame index
            imgRed.tStart = t  # local t and not account for scr refresh
            imgRed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imgRed, 'tStartRefresh')  # time at next scr refresh
            imgRed.setAutoDraw(True)
        if imgRed.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imgRed.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imgRed.tStop = t  # not accounting for scr refresh
                imgRed.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imgRed, 'tStopRefresh')  # time at next scr refresh
                imgRed.setAutoDraw(False)
        
        # *imgBlue* updates
        if imgBlue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imgBlue.frameNStart = frameN  # exact frame index
            imgBlue.tStart = t  # local t and not account for scr refresh
            imgBlue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imgBlue, 'tStartRefresh')  # time at next scr refresh
            imgBlue.setAutoDraw(True)
        if imgBlue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imgBlue.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imgBlue.tStop = t  # not accounting for scr refresh
                imgBlue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imgBlue, 'tStopRefresh')  # time at next scr refresh
                imgBlue.setAutoDraw(False)
        
        # *imgGreen* updates
        if imgGreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imgGreen.frameNStart = frameN  # exact frame index
            imgGreen.tStart = t  # local t and not account for scr refresh
            imgGreen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imgGreen, 'tStartRefresh')  # time at next scr refresh
            imgGreen.setAutoDraw(True)
        if imgGreen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imgGreen.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imgGreen.tStop = t  # not accounting for scr refresh
                imgGreen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imgGreen, 'tStopRefresh')  # time at next scr refresh
                imgGreen.setAutoDraw(False)
        
        # *imgYellow* updates
        if imgYellow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imgYellow.frameNStart = frameN  # exact frame index
            imgYellow.tStart = t  # local t and not account for scr refresh
            imgYellow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imgYellow, 'tStartRefresh')  # time at next scr refresh
            imgYellow.setAutoDraw(True)
        if imgYellow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imgYellow.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imgYellow.tStop = t  # not accounting for scr refresh
                imgYellow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imgYellow, 'tStopRefresh')  # time at next scr refresh
                imgYellow.setAutoDraw(False)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                mouse.tStop = t  # not accounting for scr refresh
                mouse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse, 'tStopRefresh')  # time at next scr refresh
                mouse.status = FINISHED
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [imgRed, imgBlue, imgGreen, imgYellow]:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practisTrials.addData('targetTxt.started', targetTxt.tStartRefresh)
    practisTrials.addData('targetTxt.stopped', targetTxt.tStopRefresh)
    practisTrials.addData('imgRed.started', imgRed.tStartRefresh)
    practisTrials.addData('imgRed.stopped', imgRed.tStopRefresh)
    practisTrials.addData('imgBlue.started', imgBlue.tStartRefresh)
    practisTrials.addData('imgBlue.stopped', imgBlue.tStopRefresh)
    practisTrials.addData('imgGreen.started', imgGreen.tStartRefresh)
    practisTrials.addData('imgGreen.stopped', imgGreen.tStopRefresh)
    practisTrials.addData('imgYellow.started', imgYellow.tStartRefresh)
    practisTrials.addData('imgYellow.stopped', imgYellow.tStopRefresh)
    # store data for practisTrials (TrialHandler)
    if len(mouse.x): practisTrials.addData('mouse.x', mouse.x[0])
    if len(mouse.y): practisTrials.addData('mouse.y', mouse.y[0])
    if len(mouse.leftButton): practisTrials.addData('mouse.leftButton', mouse.leftButton[0])
    if len(mouse.midButton): practisTrials.addData('mouse.midButton', mouse.midButton[0])
    if len(mouse.rightButton): practisTrials.addData('mouse.rightButton', mouse.rightButton[0])
    if len(mouse.time): practisTrials.addData('mouse.time', mouse.time[0])
    if len(mouse.clicked_name): practisTrials.addData('mouse.clicked_name', mouse.clicked_name[0])
    practisTrials.addData('mouse.started', mouse.tStart)
    practisTrials.addData('mouse.stopped', mouse.tStop)
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    
    
    ttext='img'+targetTxt.color
    t=ttext
    t=t.lower()
    if mouse.clicked_name:
      mous=mouse.clicked_name
      m=mous[-1]
      m=m.lower()
      if m==t : #stored on last run routine
        msg='آفرین, زمان=%.3f' % mouse.time[-1]
      else:
        msg='وای! دقت لطفا!'
    feedbackTxt.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [feedbackTxt]
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
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbackTxt* updates
        if feedbackTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbackTxt.frameNStart = frameN  # exact frame index
            feedbackTxt.tStart = t  # local t and not account for scr refresh
            feedbackTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackTxt, 'tStartRefresh')  # time at next scr refresh
            feedbackTxt.setAutoDraw(True)
        if feedbackTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackTxt.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedbackTxt.tStop = t  # not accounting for scr refresh
                feedbackTxt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedbackTxt, 'tStopRefresh')  # time at next scr refresh
                feedbackTxt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practisTrials.addData('feedbackTxt.started', feedbackTxt.tStartRefresh)
    practisTrials.addData('feedbackTxt.stopped', feedbackTxt.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'practisTrials'

# get names of stimulus parameters
if practisTrials.trialList in ([], [None], None):
    params = []
else:
    params = practisTrials.trialList[0].keys()
# save data for this loop
practisTrials.saveAsExcel(filename + '.xlsx', sheetName='practisTrials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
practisTrials.saveAsText(filename + 'practisTrials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "instruction"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the resBegin
resBegin.x = []
resBegin.y = []
resBegin.leftButton = []
resBegin.midButton = []
resBegin.rightButton = []
resBegin.time = []
resBegin.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructionComponents = [instrTxt, imgStart, resBegin]
for thisComponent in instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrTxt* updates
    if instrTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrTxt.frameNStart = frameN  # exact frame index
        instrTxt.tStart = t  # local t and not account for scr refresh
        instrTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrTxt, 'tStartRefresh')  # time at next scr refresh
        instrTxt.setAutoDraw(True)
    
    # *imgStart* updates
    if imgStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        imgStart.frameNStart = frameN  # exact frame index
        imgStart.tStart = t  # local t and not account for scr refresh
        imgStart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imgStart, 'tStartRefresh')  # time at next scr refresh
        imgStart.setAutoDraw(True)
    # *resBegin* updates
    if resBegin.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resBegin.frameNStart = frameN  # exact frame index
        resBegin.tStart = t  # local t and not account for scr refresh
        resBegin.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resBegin, 'tStartRefresh')  # time at next scr refresh
        resBegin.status = STARTED
        resBegin.mouseClock.reset()
        prevButtonState = resBegin.getPressed()  # if button is down already this ISN'T a new click
    if resBegin.status == STARTED:  # only update if started and not finished!
        buttons = resBegin.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [imgStart]:
                    if obj.contains(resBegin):
                        gotValidClick = True
                        resBegin.clicked_name.append(obj.name)
                x, y = resBegin.getPos()
                resBegin.x.append(x)
                resBegin.y.append(y)
                buttons = resBegin.getPressed()
                resBegin.leftButton.append(buttons[0])
                resBegin.midButton.append(buttons[1])
                resBegin.rightButton.append(buttons[2])
                resBegin.time.append(resBegin.mouseClock.getTime())
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instrTxt.started', instrTxt.tStartRefresh)
thisExp.addData('instrTxt.stopped', instrTxt.tStopRefresh)
thisExp.addData('imgStart.started', imgStart.tStartRefresh)
thisExp.addData('imgStart.stopped', imgStart.tStopRefresh)
# store data for thisExp (ExperimentHandler)
if len(resBegin.x): thisExp.addData('resBegin.x', resBegin.x[0])
if len(resBegin.y): thisExp.addData('resBegin.y', resBegin.y[0])
if len(resBegin.leftButton): thisExp.addData('resBegin.leftButton', resBegin.leftButton[0])
if len(resBegin.midButton): thisExp.addData('resBegin.midButton', resBegin.midButton[0])
if len(resBegin.rightButton): thisExp.addData('resBegin.rightButton', resBegin.rightButton[0])
if len(resBegin.time): thisExp.addData('resBegin.time', resBegin.time[0])
if len(resBegin.clicked_name): thisExp.addData('resBegin.clicked_name', resBegin.clicked_name[0])
thisExp.addData('resBegin.started', resBegin.tStart)
thisExp.addData('resBegin.stopped', resBegin.tStop)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=6, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
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
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    targetTxt.setColor(colour, colorSpace='rgb')
    targetTxt.setText(word)
    imgRed.setOpacity(1)
    imgRed.setPos((-250, -200))
    imgRed.setSize([125, 125])
    imgRed.setOri(0)
    imgRed.setImage('Red.jpg')
    imgBlue.setOpacity(1)
    imgBlue.setPos((-100, -200))
    imgBlue.setSize([125, 125])
    imgBlue.setOri(1)
    imgBlue.setImage('Blue.jpg')
    imgGreen.setOpacity(1)
    imgGreen.setPos((50, -200))
    imgGreen.setSize([125, 125])
    imgGreen.setOri(2)
    imgGreen.setImage('Green.jpg')
    imgYellow.setOpacity(1)
    imgYellow.setPos((200, -200))
    imgYellow.setSize([125, 125])
    imgYellow.setOri(3)
    imgYellow.setImage('Yellow.jpg')
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    trialComponents = [targetTxt, imgRed, imgBlue, imgGreen, imgYellow, mouse]
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
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *targetTxt* updates
        if targetTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            targetTxt.frameNStart = frameN  # exact frame index
            targetTxt.tStart = t  # local t and not account for scr refresh
            targetTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(targetTxt, 'tStartRefresh')  # time at next scr refresh
            targetTxt.setAutoDraw(True)
        if targetTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > targetTxt.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                targetTxt.tStop = t  # not accounting for scr refresh
                targetTxt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(targetTxt, 'tStopRefresh')  # time at next scr refresh
                targetTxt.setAutoDraw(False)
        
        # *imgRed* updates
        if imgRed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imgRed.frameNStart = frameN  # exact frame index
            imgRed.tStart = t  # local t and not account for scr refresh
            imgRed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imgRed, 'tStartRefresh')  # time at next scr refresh
            imgRed.setAutoDraw(True)
        if imgRed.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imgRed.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imgRed.tStop = t  # not accounting for scr refresh
                imgRed.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imgRed, 'tStopRefresh')  # time at next scr refresh
                imgRed.setAutoDraw(False)
        
        # *imgBlue* updates
        if imgBlue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imgBlue.frameNStart = frameN  # exact frame index
            imgBlue.tStart = t  # local t and not account for scr refresh
            imgBlue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imgBlue, 'tStartRefresh')  # time at next scr refresh
            imgBlue.setAutoDraw(True)
        if imgBlue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imgBlue.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imgBlue.tStop = t  # not accounting for scr refresh
                imgBlue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imgBlue, 'tStopRefresh')  # time at next scr refresh
                imgBlue.setAutoDraw(False)
        
        # *imgGreen* updates
        if imgGreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imgGreen.frameNStart = frameN  # exact frame index
            imgGreen.tStart = t  # local t and not account for scr refresh
            imgGreen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imgGreen, 'tStartRefresh')  # time at next scr refresh
            imgGreen.setAutoDraw(True)
        if imgGreen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imgGreen.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imgGreen.tStop = t  # not accounting for scr refresh
                imgGreen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imgGreen, 'tStopRefresh')  # time at next scr refresh
                imgGreen.setAutoDraw(False)
        
        # *imgYellow* updates
        if imgYellow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imgYellow.frameNStart = frameN  # exact frame index
            imgYellow.tStart = t  # local t and not account for scr refresh
            imgYellow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imgYellow, 'tStartRefresh')  # time at next scr refresh
            imgYellow.setAutoDraw(True)
        if imgYellow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imgYellow.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imgYellow.tStop = t  # not accounting for scr refresh
                imgYellow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imgYellow, 'tStopRefresh')  # time at next scr refresh
                imgYellow.setAutoDraw(False)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                mouse.tStop = t  # not accounting for scr refresh
                mouse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse, 'tStopRefresh')  # time at next scr refresh
                mouse.status = FINISHED
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [imgRed, imgBlue, imgGreen, imgYellow]:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('targetTxt.started', targetTxt.tStartRefresh)
    trials.addData('targetTxt.stopped', targetTxt.tStopRefresh)
    trials.addData('imgRed.started', imgRed.tStartRefresh)
    trials.addData('imgRed.stopped', imgRed.tStopRefresh)
    trials.addData('imgBlue.started', imgBlue.tStartRefresh)
    trials.addData('imgBlue.stopped', imgBlue.tStopRefresh)
    trials.addData('imgGreen.started', imgGreen.tStartRefresh)
    trials.addData('imgGreen.stopped', imgGreen.tStopRefresh)
    trials.addData('imgYellow.started', imgYellow.tStartRefresh)
    trials.addData('imgYellow.stopped', imgYellow.tStopRefresh)
    # store data for trials (TrialHandler)
    if len(mouse.x): trials.addData('mouse.x', mouse.x[0])
    if len(mouse.y): trials.addData('mouse.y', mouse.y[0])
    if len(mouse.leftButton): trials.addData('mouse.leftButton', mouse.leftButton[0])
    if len(mouse.midButton): trials.addData('mouse.midButton', mouse.midButton[0])
    if len(mouse.rightButton): trials.addData('mouse.rightButton', mouse.rightButton[0])
    if len(mouse.time): trials.addData('mouse.time', mouse.time[0])
    if len(mouse.clicked_name): trials.addData('mouse.clicked_name', mouse.clicked_name[0])
    trials.addData('mouse.started', mouse.tStart)
    trials.addData('mouse.stopped', mouse.tStop)
    thisExp.nextEntry()
    
# completed 6 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thanksText]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksText* updates
    if thanksText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanksText.frameNStart = frameN  # exact frame index
        thanksText.tStart = t  # local t and not account for scr refresh
        thanksText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanksText, 'tStartRefresh')  # time at next scr refresh
        thanksText.setAutoDraw(True)
    if thanksText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanksText.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            thanksText.tStop = t  # not accounting for scr refresh
            thanksText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanksText, 'tStopRefresh')  # time at next scr refresh
            thanksText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
