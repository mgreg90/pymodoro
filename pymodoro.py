import time, os, shutil

timerLength = 25 * 60
endTime = time.time() + timerLength
(termWidth, termLength) = shutil.get_terminal_size()
while time.time() < endTime:
    now = time.time()
    timer = round(endTime - now)
    if(timer % 60 == 0):
        clock = str(int(timer / 60)) + ":00"
    else:
        clock = str(int(timer / 60)) + ":" + str(timer % 60)
    os.system("clear")
    print("\n" * int(termLength / 4))
    print(clock.center(termWidth))
    time.sleep(1)
