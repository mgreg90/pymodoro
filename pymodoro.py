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
    return timers

def printTopQuarter(text, size):
    print("\n" * int(size['length'] / 4))
    print(text.center(size['width']))

def printCentered(text, size):
    print(text.center(size['width']))

def printCenteredWithInput(text, size):
    return input(text.center(size['width']))

def runClock(length, nextClockType):
    timerLength = length
    endTime = time.time() + timerLength
    while time.time() < endTime:
        now = time.time()
        timer = round(endTime - now)
        if(timer % 60 == 0):
            clock = str(int(timer / 60)) + ":00"
        elif(timer % 60 < 10):
            clock = str(int(timer / 60)) + ":0" + str(timer % 60)
        else:
            clock = str(int(timer / 60)) + ":" + str(timer % 60)
        os.system("clear")
        printTopQuarter(clock, termSize)
        time.sleep(1)
    for x in range(0, 5):
        print("\a")
        time.sleep(0.15)
    os.system("clear")

    timerUpMsg1 = "Time is up!"
    timerUpMsg2 = "Press Enter to begin " + nextClockType + " clock."
    printTopQuarter(timerUpMsg1, termSize)
    printCentered(timerUpMsg2, termSize)
    printCenteredWithInput("Press ENTER", termSize)

while True:
    termSize = mainMenu()
    timers = options(termSize)
    print(timers)
    input()
    workTimer = timers[0]
    breakTimer = timers[1]
    runClock(int(float(workTimer) * 60), "break")
    runClock(int(float(breakTimer) * 60), "pomodoro")
