/******************************** 
 * Stroopexperiment_Online Test *
 ********************************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'stroopExperiment_Online';  // from the Builder filename that created this script
let expInfo = {'نام': '', 'نام خانوادگی': '', 'کلاس': '', 'سن': '', 'چندمین بار است که در این تست شرکت می کنید': '001'};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructionRoutineBegin());
flowScheduler.add(instructionRoutineEachFrame());
flowScheduler.add(instructionRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(thanksRoutineBegin());
flowScheduler.add(thanksRoutineEachFrame());
flowScheduler.add(thanksRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'Red.jpg', 'path': 'Red.jpg'},
    {'name': 'Green.jpg', 'path': 'Green.jpg'},
    {'name': 'Blue.jpg', 'path': 'Blue.jpg'},
    {'name': 'Yellow.jpg', 'path': 'Yellow.jpg'},
    {'name': 'conditions.xlsx', 'path': 'conditions.xlsx'},
    {'name': 'Start.jpg', 'path': 'Start.jpg'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.10';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var instructionClock;
var instrTxt;
var imgStart;
var resBegin;
var trialClock;
var targetTxt;
var imgRed;
var imgBlue;
var imgGreen;
var imgYellow;
var mouse;
var thanksClock;
var thanksText;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instruction"
  instructionClock = new util.Clock();
  instrTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrTxt',
    text: 'برای مواجهه با یک آزمون چالشی جدید آماده ای؟\n\nبخاطر داشته باش، واژه ها را در نظر نگیر و \nرنگها را انتخاب کن\n\n\nبرای ادامه شروع را انتخاب کنید\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1, 1, 1]),  opacity: 1,
    depth: 0.0 
  });
  
  imgStart = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imgStart', units : 'pix', 
    image : 'Start.jpg', mask : undefined,
    ori : 0, pos : [0, (- 310)], size : [125, 125],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  resBegin = new core.Mouse({
    win: psychoJS.window,
  });
  resBegin.mouseClock = new util.Clock();
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  targetTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'targetTxt',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  imgRed = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imgRed', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  imgBlue = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imgBlue', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  imgGreen = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imgGreen', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  imgYellow = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imgYellow', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Initialize components for Routine "thanks"
  thanksClock = new util.Clock();
  thanksText = new visual.TextStim({
    win: psychoJS.window,
    name: 'thanksText',
    text: 'پایان آزمون\n\nاز شما بسیار سپاسگزاریم!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color([1, 1, 1]),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var gotValidClick;
var instructionComponents;
function instructionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instruction'-------
    t = 0;
    instructionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the resBegin
    // current position of the mouse:
    resBegin.x = [];
    resBegin.y = [];
    resBegin.leftButton = [];
    resBegin.midButton = [];
    resBegin.rightButton = [];
    resBegin.time = [];
    resBegin.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    instructionComponents = [];
    instructionComponents.push(instrTxt);
    instructionComponents.push(imgStart);
    instructionComponents.push(resBegin);
    
    instructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function instructionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instruction'-------
    // get current time
    t = instructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instrTxt* updates
    if (t >= 0.0 && instrTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrTxt.tStart = t;  // (not accounting for frame time here)
      instrTxt.frameNStart = frameN;  // exact frame index
      
      instrTxt.setAutoDraw(true);
    }

    
    // *imgStart* updates
    if (t >= 0.0 && imgStart.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imgStart.tStart = t;  // (not accounting for frame time here)
      imgStart.frameNStart = frameN;  // exact frame index
      
      imgStart.setAutoDraw(true);
    }

    // *resBegin* updates
    if (t >= 0.0 && resBegin.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resBegin.tStart = t;  // (not accounting for frame time here)
      resBegin.frameNStart = frameN;  // exact frame index
      
      resBegin.status = PsychoJS.Status.STARTED;
      resBegin.mouseClock.reset();
      prevButtonState = resBegin.getPressed();  // if button is down already this ISN'T a new click
      }
    if (resBegin.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = resBegin.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = resBegin.getPos();
          resBegin.x.push(_mouseXYs[0]);
          resBegin.y.push(_mouseXYs[1]);
          resBegin.leftButton.push(_mouseButtons[0]);
          resBegin.midButton.push(_mouseButtons[1]);
          resBegin.rightButton.push(_mouseButtons[2]);
          resBegin.time.push(resBegin.mouseClock.getTime());
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [imgStart]) {
            if (obj.contains(resBegin)) {
              gotValidClick = true;
              resBegin.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instruction'-------
    instructionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    if (resBegin.x) {  psychoJS.experiment.addData('resBegin.x', resBegin.x[0])};
    if (resBegin.y) {  psychoJS.experiment.addData('resBegin.y', resBegin.y[0])};
    if (resBegin.leftButton) {  psychoJS.experiment.addData('resBegin.leftButton', resBegin.leftButton[0])};
    if (resBegin.midButton) {  psychoJS.experiment.addData('resBegin.midButton', resBegin.midButton[0])};
    if (resBegin.rightButton) {  psychoJS.experiment.addData('resBegin.rightButton', resBegin.rightButton[0])};
    if (resBegin.time) {  psychoJS.experiment.addData('resBegin.time', resBegin.time[0])};
    if (resBegin.clicked_name) {  psychoJS.experiment.addData('resBegin.clicked_name', resBegin.clicked_name[0])};
    
    // the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials;
var currentLoop;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 6, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'conditions.xlsx',
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials.forEach(function() {
    const snapshot = trials.getSnapshot();

    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(trialRoutineBegin(snapshot));
    trialsLoopScheduler.add(trialRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(trialRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var trialComponents;
function trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    targetTxt.setColor(new util.Color(colour));
    targetTxt.setText(word);
    imgRed.setOpacity(1);
    imgRed.setPos([(- 250), (- 150)]);
    imgRed.setSize([100, 100]);
    imgRed.setOri(0);
    imgRed.setImage('Red.jpg');
    imgBlue.setOpacity(1);
    imgBlue.setPos([(- 100), (- 150)]);
    imgBlue.setSize([100, 100]);
    imgBlue.setOri(0);
    imgBlue.setImage('Blue.jpg');
    imgGreen.setOpacity(1);
    imgGreen.setPos([50, (- 150)]);
    imgGreen.setSize([100, 100]);
    imgGreen.setOri(0);
    imgGreen.setImage('Green.jpg');
    imgYellow.setOpacity(1);
    imgYellow.setPos([200, (- 150)]);
    imgYellow.setSize([100, 100]);
    imgYellow.setOri(0);
    imgYellow.setImage('Yellow.jpg');
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(targetTxt);
    trialComponents.push(imgRed);
    trialComponents.push(imgBlue);
    trialComponents.push(imgGreen);
    trialComponents.push(imgYellow);
    trialComponents.push(mouse);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trial'-------
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *targetTxt* updates
    if (t >= 0.0 && targetTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      targetTxt.tStart = t;  // (not accounting for frame time here)
      targetTxt.frameNStart = frameN;  // exact frame index
      
      targetTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((targetTxt.status === PsychoJS.Status.STARTED || targetTxt.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      targetTxt.setAutoDraw(false);
    }
    
    // *imgRed* updates
    if (t >= 0.0 && imgRed.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imgRed.tStart = t;  // (not accounting for frame time here)
      imgRed.frameNStart = frameN;  // exact frame index
      
      imgRed.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((imgRed.status === PsychoJS.Status.STARTED || imgRed.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      imgRed.setAutoDraw(false);
    }
    
    // *imgBlue* updates
    if (t >= 0.0 && imgBlue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imgBlue.tStart = t;  // (not accounting for frame time here)
      imgBlue.frameNStart = frameN;  // exact frame index
      
      imgBlue.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((imgBlue.status === PsychoJS.Status.STARTED || imgBlue.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      imgBlue.setAutoDraw(false);
    }
    
    // *imgGreen* updates
    if (t >= 0.0 && imgGreen.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imgGreen.tStart = t;  // (not accounting for frame time here)
      imgGreen.frameNStart = frameN;  // exact frame index
      
      imgGreen.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((imgGreen.status === PsychoJS.Status.STARTED || imgGreen.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      imgGreen.setAutoDraw(false);
    }
    
    // *imgYellow* updates
    if (t >= 0.0 && imgYellow.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imgYellow.tStart = t;  // (not accounting for frame time here)
      imgYellow.frameNStart = frameN;  // exact frame index
      
      imgYellow.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((imgYellow.status === PsychoJS.Status.STARTED || imgYellow.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      imgYellow.setAutoDraw(false);
    }
    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((mouse.status === PsychoJS.Status.STARTED || mouse.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      mouse.status = PsychoJS.Status.FINISHED;
  }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse.getPos();
          mouse.x.push(_mouseXYs[0]);
          mouse.y.push(_mouseXYs[1]);
          mouse.leftButton.push(_mouseButtons[0]);
          mouse.midButton.push(_mouseButtons[1]);
          mouse.rightButton.push(_mouseButtons[2]);
          mouse.time.push(mouse.mouseClock.getTime());
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [imgRed, imgBlue, imgGreen, imgYellow]) {
            if (obj.contains(mouse)) {
              gotValidClick = true;
              mouse.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial'-------
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    if (mouse.x) {  psychoJS.experiment.addData('mouse.x', mouse.x[0])};
    if (mouse.y) {  psychoJS.experiment.addData('mouse.y', mouse.y[0])};
    if (mouse.leftButton) {  psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton[0])};
    if (mouse.midButton) {  psychoJS.experiment.addData('mouse.midButton', mouse.midButton[0])};
    if (mouse.rightButton) {  psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton[0])};
    if (mouse.time) {  psychoJS.experiment.addData('mouse.time', mouse.time[0])};
    if (mouse.clicked_name) {  psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name[0])};
    
    return Scheduler.Event.NEXT;
  };
}


var thanksComponents;
function thanksRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'thanks'-------
    t = 0;
    thanksClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    thanksComponents = [];
    thanksComponents.push(thanksText);
    
    thanksComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function thanksRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'thanks'-------
    // get current time
    t = thanksClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *thanksText* updates
    if (t >= 0.0 && thanksText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      thanksText.tStart = t;  // (not accounting for frame time here)
      thanksText.frameNStart = frameN;  // exact frame index
      
      thanksText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((thanksText.status === PsychoJS.Status.STARTED || thanksText.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      thanksText.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    thanksComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function thanksRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'thanks'-------
    thanksComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
