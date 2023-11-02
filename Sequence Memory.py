import pyautogui as pg
import time


old=[]
clicks=[]
squars=[(750,320),(950,320),(1150,320),
        (750,520),(950,520),(1150,520),
        (750,720),(950,720),(1150,720)]
# 750-320 starting position full screen
# 750-430 starting position normal
# 250-450 starting position left half
#960-655 yello r255
for i in range(0,9):
    old.append(False)

def scanning(timer):
    while timer<15:
        time.sleep(0.1)
        timer+=1
        for i in range(9):
            if pg.pixel(squars[i][0],squars[i][1])[0]>200:
                print('found a pixle')
                timer=0
                if old[i]==False:
                    clicks.append(i)
                    print('appened')
                    old[i]=True

        for i in range(9):
           if pg.pixel(squars[i][0],squars[i][1])[0]<200:
                old[i]=False

def clickk():
    print(clicks)
    for i in clicks:
        pg.click(squars[i][0],squars[i][1])
    for i in range(len(clicks)):
        clicks.pop(0)


def main():
    time.sleep(2)
    while True:
        if pg.pixel(960,655)==(255,209,84):
            pg.click(960,655)
            break
    time.sleep(0.4)
    timer=0
    while True:
        scanning(timer)
        clickk()
        time.sleep(0.1)

main()