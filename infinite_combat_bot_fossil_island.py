import pyautogui
import time


#This bot is an infinite combat bot in the fossil island cavern
#This code should be run after the ten mins of crabs attacking me are done

for number in range(10000):
    #first click up the stairs after code starts
    pyautogui.click(x=326, y=535, duration =5.75)

    #next click is up the rope
    pyautogui.click(x=163, y=381, duration =5.75)

    #click down the cavern
    pyautogui.click(x=329, y=454, duration =5.75)

    #click down the stairs
    pyautogui.click(x=646, y=471, duration =5.75)

    #click back to starting position
    pyautogui.click(x=358, y=356, duration =5.75)


    #---------From this point on I have to burn ten mins without logging out-------

    #click on special attack
    pyautogui.click(x=623, y=157, duration =35.33)

    #click on skills tab
    pyautogui.click(x=582, y=842, duration =240.33)

    #click on skills tab again
    pyautogui.click(x=582, y=842, duration =5.33)

    #click on special attack
    pyautogui.click(x=623, y=157, duration =35.33)

    time.sleep(45)









