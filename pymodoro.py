import time, os, shutil

def mainMenu():
    os.system("clear")
    termSize = {}
    [termSize['width'], termSize['length']] = shutil.get_terminal_size()
    printTopQuarter("Welcome to Pymodoro!", termSize)
    return termSize

def options(termSize):
    workTimer = printCenteredWithInput("How long should work periods be?", termSize)
    breakTimer = printCenteredWithInput("How long should break periods be?", termSize)
    timers = [workTimer, breakTimer]
    timers = optionsQuickPick(timers)
    return timers

def optionsQuickPick(timers):
    timers[0] = 25 if timers[0] == '' else timers[0]
    timers[1] = 5 if timers[1] == '' else timers[1]
    return timers

def printTopQuarter(text, size):
    print("\n" * int(size['length'] / 4))
    print(text.center(size['width']))

def printCentered(text, size):
    print(text.center(size['width']))

def printCenteredWithInput(text, size):
    return input(text.center(size['width'])).center(size['width'])

def runClock(timerLength, termSize, nextClockType):
    endTime = time.time() + timerLength
    while time.time() < endTime:
        runOneSecond(endTime, termSize)
    for x in range(0, 5):
        fiveBeeps()
    clockExpired(nextClockType, termSize)

def fiveBeeps():
    print("\a")
    time.sleep(0.15)

def runOneSecond(endTime, termSize):
    timer = setTimer(endTime)
    clock = setClock(timer)
    os.system("clear")
    printTopQuarter(clock, termSize)
    time.sleep(1)

def setTimer(endTime):
    now = time.time()
    return round(endTime - now)

def setClock(timer):
    if(timer % 60 == 0):
        clock = str(int(timer / 60)) + ":00"
    elif(timer % 60 < 10):
        clock = str(int(timer / 60)) + ":0" + str(timer % 60)
    else:
        clock = str(int(timer / 60)) + ":" + str(timer % 60)
    return clock

def clockExpired(nextClockType, termSize):
    os.system("clear")
    timerUpMsg1 = "Time is up!"
    if nextClockType == "break":
        timerUpMsg2 = "Take a break!"
    elif nextClockType == "pomodoro":
        timerUpMsg2 = "Get to Work!"
    timerUpMsg3 = "Press Enter to begin " + nextClockType + " clock."
    printTopQuarter(timerUpMsg1, termSize)
    printCentered(timerUpMsg2, termSize)
    printCentered(timerUpMsg3, termSize)
    print("\n")
    printCenteredWithInput("Press ENTER", termSize)

def startUp():
    termSize = mainMenu()
    timers = options(termSize)
    return [termSize, timers]

def runTimers(timers, termSize):
    workTimer = int(float(timers[0]) * 60)
    breakTimer = int(float(timers[1]) * 60)
    runClock(workTimer, termSize, "break")
    runClock(breakTimer, termSize, "pomodoro")

def runPymodoro():
    [termSize, timers] = startUp()
    while True:
        runTimers(timers, termSize)

runPymodoro()
