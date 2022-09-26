# main.py

'''
title: Cannon Operator
Author: Parth Sakpal
date-created: 2022-09-23
'''

import math
## -- SUBROUTINES -- #

def titleScreen():
    print("""
    Cannons!!
    
    1. Scenario 1
    2. Scenario 2 
    3. Scenario 3
    """)

    SCENARIO = input("select your input: ")
    SCENARIO = checkInt(SCENARIO)

    if SCENARIO > 0 and SCENARIO < 4:
        return SCENARIO
    else:
        print("enter valid option")
        return titleScreen()





def checkInt(NUM):

    if NUM.isnumeric():
        return int(NUM)
    else:
        print("please enter a valid number")
        NEW_NUM = input("Please enter the value again: ")
        return checkInt(NEW_NUM)

def height():
    """
    asks user for distance above the water (height)
    :return: int
    """
    DISTANCE = input("what the distance of the cannon above the water? (m): ")
    DISTANCE = checkInt(DISTANCE)
    return DISTANCE

def Speed():

    """
    asks user for speed
    :return: int
    """
    SPEED = input("what's the speed (m/s) : ")
    SPEED = checkInt(SPEED)
    return SPEED



def Scenario_1(SPEED, HEIGHT):


    """
    CALCULATES SCENARIO 1
    :param SPEED: int
    :param HEIGHT: int
    :return: int
    """


    TIME = math.sqrt(2 * HEIGHT / 9.81)

    DISTANCE_X = SPEED * TIME
    DISTANCE_X = round(DISTANCE_X, 2)

    print(DISTANCE_X)




### --- MAIN PROGRAM CODE --- ###

if __name__ == "__main__":

    Option = titleScreen()
    print(Option)

    SPEED_G = Speed()
    HEIGHT_G = height()

    #Scenario_1(SPEED_G, HEIGHT_G) '''' SCENARIO ONE WORKS ''''



#INPUTS#

#PROCESSING#

#OUTPUTS#