#import needed libraries
import pyautogui as pg
import time

#making empty lists to use later
old=[]
clicks=[]
#a list of the location of the white squares while on full screen
squars=[(750,320),(950,320),(1150,320),
        (750,520),(950,520),(1150,520),
        (750,720),(950,720),(1150,720)]

#location of the yellow start button 960-655

#filling the old array with False
for i in range(0,9):
    old.append(False)

#scan the boxes for white and save it to the clicks array
def scanning(timer):
    while timer<5: #it keeps checking until it doesnt find anything for the set diuration
        time.sleep(0.1)
        timer+=1
        for i in range(9):
            if pg.pixel(squars[i][0],squars[i][1])[0]>200:#check if that square is white
                timer=0 #to reset the timer if a square was white
                if old[i]==False: #check if the sqare was white last time to not add it again
                    clicks.append(i)
                    old[i]=True

        #check if the sqare is not white anymore
        for i in range(9):
           if pg.pixel(squars[i][0],squars[i][1])[0]<200:
                old[i]=False

#a function to click on the squars saved from scanning function
def clickk():
    for i in clicks:
        pg.click(squars[i][0],squars[i][1])
    for i in range(len(clicks)):
        clicks.pop(0)

#main function
def main():
    time.sleep(2)
    #a while loop to check for the yellow start button
    while True:
        if pg.pixel(960,655)==(255,209,84):
            pg.click(960,655)
            break
    time.sleep(0.4)
    timer=0
    #a while loop to keep repeating the code foreach level
    while True:
        scanning(timer)
        clickk()
        time.sleep(0.1)

#running main funtion
main()