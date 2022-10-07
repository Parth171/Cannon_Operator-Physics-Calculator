# main.py

'''
title: Cannon Operator
Author: Parth Sakpal
date-created: 2022-09-23
'''

## -- IMPORT LIBRARIES -- ##
import math

RUN = 1


## -- SUBROUTINES -- #


def checkInt(NUM):
    if NUM.isnumeric():  # Checks if the value entered is an integer
        return int(NUM)
    else:
        print("Please enter a valid number.")
        NEW_NUM = input(
            "Please enter the value again: ")  # Asks user to input the value again if it isn't a valid input
        return checkInt(NEW_NUM)  # Checks the validity of the new input


### -- INPUTS -- ##

def titleScreen():
    """

    Presents user with the four scenario options and prompts user to choose one of the options
    :return: int
    """

    # Prints the menu presented to the user #
    print("""
    Welcome to Navy Cannon Operator!
    Please choose the scenario that you wish to calculate.  

    Scenario 1. Calculates the horizontal distance the cannonball travels when it is shot horizontal to the water. 
    ____
    |   \
    |    \
    |     \

    Scenario 2. Calculates the horizontal distance the cannonball travels when it is shot parabolic to another ship of the same height.
       ___
      /   \
     /     \
    /       \

    Scenario 3. Calculates the horizontal distance the cannonball travels when it is shot parabolic to another smaller ship. 
      ___
     /   \
    |     \
    |      \

    Scenario 4. Calculates the angle the cannon must be shot in order to successfully hit a fighter jet.
       ____
      /
     /
    /

    """)

    SCENARIO = input("Select your desired scenario (1-4): ")
    SCENARIO = checkInt(SCENARIO)  # Checks to see if the input is an integer

    if SCENARIO > 0 and SCENARIO < 5:  # Checks to see if the input is a valid input from the menu presented
        return SCENARIO
    else:
        print("Enter an option from the menu presented.")
        return titleScreen()  # Asks user for the input again if the input they provided was not valid.


def Height():
    """
    Asks user for distance above the water (height)
    :return: int
    """
    HEIGHT = input("What is the height of the cannon? (m): ")
    HEIGHT = checkInt(HEIGHT)  # Checks to see if the input is an integer
    return HEIGHT


def Speed():
    """
    Asks user for speed the cannonball leaves the cannon at (m/s)
    :return: int
    """
    SPEED = input("What's the initial speed the cannonball? (m/s): ")
    SPEED = checkInt(SPEED)  # Checks to see if the input is an integer
    return SPEED


def Angle():
    """
    Asks user for the angle the cannon was launched at (in degrees)
    :return: int
    """
    ANGLE = input("Enter the angle the cannon is fired at (in degrees): ")
    ANGLE = checkInt(ANGLE)  # Checks to see if the input is an integer
    if ANGLE > 90 or ANGLE == 90:  # Checks to see if the angle entered is 90 or more
        print(
            "Make sure your angle is less than 90 degrees, or you will hit your own ship")  # If the angle entered is 90 or above, it informs the user that they will hit their own ship.
        print(
            "Enter the value again")  # Prompts user to enter the angle again if the angle they originally entered was 90 or above.
        return Angle()
    return ANGLE


def Distance_X():
    """
    Asks the user how far the fighter jet is from the their ship (Horizontal distance between ship and fighter jet)
    :return: int
    """

    DISTANCE_X = input("How far is the fighter jet from your ship in meters? (Horizontal Distance): ")
    DISTANCE_X = checkInt(DISTANCE_X)  # Checks to see if the input is an integer
    return DISTANCE_X


def Distance_Y():
    """
    Asks the user how much higher the fighter jet is compared to the ship in meters (Vertical Distance)
    :return:
    """

    DISTANCE_Y = input("How much higher is the fighter jet compared to your ship in meters? (Vertical Distance): ")
    DISTANCE_Y = checkInt(DISTANCE_Y)  # Checks to see if the input is an integer
    return (DISTANCE_Y)


## -- PROCESSING -- ##

def Scenario_1(SPEED, HEIGHT):
    """
    CALCULATES SCENARIO 1
    :param SPEED: int
    :param HEIGHT: int
    :return: float
    """

    TIME = math.sqrt(2 * HEIGHT / 9.81)  # Calculates the time value

    DISTANCE_X = SPEED * TIME  # Calculates the horizontal distance
    DISTANCE_X = round(DISTANCE_X, 2)  # Rounds the distance to the nearest hundredth
    print("The total distance the cannonball traveled is", DISTANCE_X, "meters.")
    return DISTANCE_X


def Scenario_2(SPEED, ANGLE):
    """
    CALCULATES SCENARIO 2
    :param SPEED: int
    :param ANGLE: int
    :return: float
    """

    ANGLE_RADS = math.radians(ANGLE)  # converts angle to radians for easier calculation
    SPEED_Y = SPEED * math.sin(ANGLE_RADS)  # Calculates the initial vertical speed
    SPEED_X = SPEED * math.cos(ANGLE_RADS)  # Calculates the initial horizontal speed
    TIME_TOTAL = SPEED_Y / 9.81 * 2  # Calculates the time
    DISTANCE_X = TIME_TOTAL * SPEED_X  # Calculates the horizontal distance
    DISTANCE_X = round(DISTANCE_X, 2)  # Rounds the distance to the nearest hundredth
    print("The total distance the cannonball traveled is", DISTANCE_X, "meters.")
    return DISTANCE_X


def Scenario_3(SPEED, ANGLE, HEIGHT):
    """
    CALCULATES SCENARIO 3
    :param SPEED: int
    :param ANGLE: int
    :param HEIGHT: int
    :return: float
    """
    HEIGHT = HEIGHT * -1  # Since the cannonball is being shot below its origin, it turns the height negative for easier calculation
    ANGLE_RADS = math.radians(ANGLE)  # converts angle to radians for easier calculation
    SPEED_Y = SPEED * math.sin(ANGLE_RADS)  # Calculates the initial vertical speed
    SPEED_X = SPEED * math.cos(ANGLE_RADS)  # Calculates the initial horizontal speed
    VELOCITY_Y_FINAL = (math.sqrt(SPEED_Y ** 2 + 2 * (-9.81) * (HEIGHT))) * -1  # Calculates the final vertical speed

    TIME = (VELOCITY_Y_FINAL - SPEED_Y) / -9.81  # Calculates the time

    DISTANCE = TIME * SPEED_X
    DISTANCE = round(DISTANCE, 2)
    print("The total distance the cannonball traveled is", DISTANCE, "meters.")
    return DISTANCE


def Scenario_4(DISTANCE_X, DISTANCE_Y):
    """
    Calculates the angle the cannon must be fired to hit the fighter jet
    :param DISTANCE_X: int
    :param DISTANCE_Y: int
    :return: float
    """
    ANGLE = math.atan(DISTANCE_Y / DISTANCE_X)
    ANGLE = math.degrees(ANGLE)
    ANGLE = round(ANGLE, 2)
    print("Shoot the cannon at a", ANGLE, "degree angle to successfully hit the enemy fighter jet")
    return ANGLE


def Again():
    """
    Asks your if they want to run the program again
    :return: int
    """

    AGAIN = input("Would you like to make another calculation? (Y/N): ")

    if AGAIN == "Y" or AGAIN == "y":
        return 1
    elif AGAIN == "N" or AGAIN == "n":
        return 2
    else:
        print("Please enter either 'y' for yes, or 'n' for no.")
        return Again()


### --- MAIN PROGRAM CODE --- ###

if __name__ == "__main__":

    while RUN == 1:

        ## -- INPUTS -- ##
        Option = titleScreen()

        ## -- PROCESSING -- ##
        if Option == 1:
            print("""

You chose Scenario 1.

In this scenario, you must provide the speed the cannonball leaves the cannon at, 
as well as the height of the cannon to determine the distance the cannonball
travels. 

                """)
            SPEED_G = Speed()
            HEIGHT_G = Height()
            Scenario_1(SPEED_G, HEIGHT_G)
        elif Option == 2:
            print("""
You chose Scenario 2.

In this scenario, you must provide the speed the ball leaves the cannon 
at, as well as the angle the cannon is fired at to determine the distance the
cannonball travels. 


            """)
            SPEED_G = Speed()
            ANGLE_G = Angle()
            Scenario_2(SPEED_G, ANGLE_G)
        elif Option == 3:
            print("""
You chose Scenario 3.

In this scenario, you must provide the speed the ball leaves the cannon at,
the angle the cannon is fired at, and the height of the cannon to determine
the distance the cannonball travels. 

            """)
            SPEED_G = Speed()
            ANGLE_G = Angle()
            HEIGHT_G = Height()
            Scenario_3(SPEED_G, ANGLE_G, HEIGHT_G)
        else:
            print("""
You chose Scenario 4.
THERE IS A FIGHTER JET COMING YOUR WAY!!

In this scenario, you must enter how far the fighter jet is away from your
ship, as well as how high the fighter jet is compared to your ship to determine
the angle you must fire the cannon to successfully hit the fighter jet.


            """)
            DISTANCE_X_G = Distance_X()
            DISTANCE_Y_G = Distance_Y()
            Scenario_4(DISTANCE_X_G, DISTANCE_Y_G)

        AGAIN_G = Again()

        if AGAIN_G == 1:
            RUN = 1
        else:
            print("Thanks for visiting Navy Cannon Operator!")
            RUN = 0





