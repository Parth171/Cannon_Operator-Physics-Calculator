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


'''
def checkFloat(NUM):

    if isinstance(NUM, float):
        return float(NUM)
    else:
        print("please enter a valid number")
        NEW_NUM = input("Please enter the value again: ")
        return checkFloat(NEW_NUM)

    print(NUM)

'''


def checkInt(NUM):

    if NUM.isnumeric():
        return int(NUM)
    else:
        print("please enter a valid number")
        NEW_NUM = input("Please enter the value again: ")
        return checkInt(NEW_NUM)

def Height():
    """
    asks user for distance above the water (height)
    :return: int
    """
    HEIGHT = input("what the distance of the cannon above the water? (m): ")
    HEIGHT = checkInt(HEIGHT)
    return HEIGHT

def Speed():

    """
    asks user for speed
    :return: int
    """
    SPEED = input("what's the speed (m/s) : ")
    SPEED = checkInt(SPEED)
    return SPEED

def Angle():
    """
    asks user for the angle the cannon was lauched at
    :return: int
    """
    ANGLE = input("Enter the angle the cannon is fired at: ")
    ANGLE = checkInt(ANGLE)
    if ANGLE > 90 or ANGLE == 90:
        print("Make sure your angle is less than 90 degrees, or you will hit your own ship")
        print("Enter the value again")
        return Angle()
    return ANGLE

def Scenario_1(SPEED, HEIGHT):


    """
    CALCULATES SCENARIO 1
    :param SPEED: int
    :param HEIGHT: int
    :return: float
    """


    TIME = math.sqrt(2 * HEIGHT / 9.81)

    DISTANCE_X = SPEED * TIME
    DISTANCE_X = round(DISTANCE_X, 2)
    print(DISTANCE_X)
    return DISTANCE_X


def Scenario_2(SPEED, ANGLE):

    """
    CALCULATES SCENARIO 2
    :param SPEED: int
    :param ANGLE: int
    :return: float
    """

    ANGLE_RADS = math.radians(ANGLE) # converts angle to radians for easier calculation
    SPEED_Y = SPEED * math.sin(ANGLE_RADS)
    SPEED_X = SPEED * math.cos(ANGLE_RADS)
    TIME_TOTAL = SPEED_Y / 9.81 * 2
    DISTANCE_X = TIME_TOTAL * SPEED_X
    DISTANCE_X = round(DISTANCE_X, 2)
    print(DISTANCE_X)
    return DISTANCE_X





### --- MAIN PROGRAM CODE --- ###

if __name__ == "__main__":

    Option = titleScreen()
    print(Option)

    ANGLE_G = Angle()
    SPEED_G = Speed()
    #HEIGHT_G = Height()

    #Scenario_2(SPEED_G, ANGLE_G) ''''####SCENARIO TWO WORKS####''''

    #Scenario_1(SPEED_G, HEIGHT_G) '''' ####SCENARIO ONE WORKS#### ''''




#INPUTS#

#PROCESSING#

#OUTPUTS#