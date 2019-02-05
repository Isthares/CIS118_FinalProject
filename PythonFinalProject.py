# File Name: PythonFinalProject.py
# Author: Esther Heralta Espinosa
# Date: 11/20/17
# Description of the program: FinalProject - Number Guessing Game                            
"""
Initially, the user has to decide which mode is he/she going to play. There are two options: 
the user plays against the computer (User Mode) or the computer plays against the user (Computer 
Mode). In the first scenario, the computer picks a number between 1 and 100, and the user has to 
guess that number. In the second scenario, user and computer trade places. That is, the computer 
picks a number between 1 and 100, and the user has to guess that number. The last option is Exit 
the game.


* First Scenario: User plays against the Computer
-------------------------------------------------
The game offers three different game options: Easy Mode, Difficult Mode, and Challenging Mode. 
It also offers the Exit option, just in case the user wants to come back to the first menu and 
chose among User Mode, Computer Mode, or Exit Game.

-   Easy Mode:

    o   In this mode, the user has unlimited attempts to try to guess the number picked by the 
        computer.
    o   First, the computer picks a number between 1 and 100.
    o   Second, the user enters a number between 1 and 100 in order to guess the number picked by 
        the computer. It is also offered the option to exit the easy mode.
    o   If the number entered is not correct, a message of invalid option is shown and the user 
        has the option of entering a valid number again.  This step will be repeated until getting 
        a valid number.
    o   After entering a valid number, it is checked if the user wants to exit the easy mode or wants 
        to keep playing. In the first case, a message of Exit User Mode is shown and the first menu 
        (User Mode, Computer Mode, or Exit Game) is displayed. In the second case, it is compared the 
        user’s number and the computer’s numbers. 
        •   If both numbers are equal, that means that the user has guessed the number. So, the number 
            of tries is incremented and two messages are displayed: one indicating the user that has 
            won and the other one showing how many tries took him/her to guess the number. After that, 
            User Mode menu is shown letting the user choosing among the different options (Easy Mode, 
            Difficult Mode, Challenging Mode, or Exit User Mode). 
        •   If both numbers are not equal, another comparison is carried out, if the user’s number is 
            greater than the computer’s number. If it is greater, a message indicating that the number 
            entered is too high is shown. On the contrary, it is not greater, a message indicating that 
            the number entered is too low is shown. After that, the number of tries is incremented and 
            a message indicating the number of tries so far is displayed. At this point, the game gives 
            the option to keep playing or exit the easy mode. This process will be repeated until the 
            user guesses the number or decides to exit the easy mode.

-   Difficult Mode:

    o   In this mode the user has a limited attempts to try to guess the number picked by the computer.
    o   First, the computer picks a number between 1 and 100.
    o   Second, the user enters a number between 1 and 100 in order to guess the number picked by the 
        computer. It is also offered the option to exit the difficult mode.
    o   If the number entered is not correct, a message of invalid option is shown and the user has 
        the option of entering a valid number again.  This step will be repeated until getting a valid 
        number.
    o   After entering a valid number, it is checked if the user wants to exit the difficult mode or 
        wants to play. In the first case, a message of Exit User Mode is shown and the first menu (User 
        Mode, Computer Mode, or Exit Game) is displayed. In the second case, it is compared the user’s 
        number and the computer’s numbers. 
        •   If both numbers are equal, that means that the user has guessed the number. So, the number 
            of tries is incremented and two messages are displayed: one indicating the user that has 
            won and the other one showing how many tries took the him/her to guess the number. After 
            that, User Mode menu is shown letting the user choosing among the different options (Easy 
            Mode, Difficult Mode, Challenging Mode, or Exit User Mode). 
        •   If both numbers are not equal, another comparison is carried out, if the user’s number is 
            greater than the computer’s number. If it is greater, a message indicating that the number 
            entered is too high is shown. On the contrary, it is not greater, a message indicating that 
            the number entered is too low is shown. After that, number of tries is incremented and a 
            message indicating the number of tries so far is displayed. 
    o   Next step is checking if the number of tries is the same that the maximum number of tries that 
        the user has to guess the number.  If both are the same number, it means that no more guesses 
        left. It is displayed a message telling the user that no tries left and the User Mode menu is 
        shown letting the user choosing among the different options (Easy Mode, Difficult Mode, 
        Challenging Mode, or Exit User Mode). However, if both numbers differ, a message of how many 
        tries left is shown and the game gives the option to keep playing or exit the difficult mode. 
        This process will be repeated until no more tries left or the user decides to exit the difficult 
        mode.

-   Challenging Mode:

    o   In this mode the user has a limited time to try to guess the number picked by the computer.
    o   First, the computer picks a number between 1 and 100.
    o   Second, a time limit is set.
    o   Third, the user enters a number between 1 and 100 in order to guess the number picked by the 
        computer. It is also offered the option to exit the challenging mode.
    o   If the number entered is not correct, a message of invalid option is shown and the user has 
        the option of entering a valid number again.  This step will be repeated until getting a valid 
        number.
    o   After entering a valid number, it is checked if the user wants to exit the challenging mode or 
        wants to play. In the first case, a message of Exit User Mode is shown and the first menu (User 
        Mode, Computer Mode, or Exit Game) is displayed. In the second case, it is compared the user’s 
        number and the computer’s numbers. 
    o   After entering a valid number, it is checked if the user wants to exit the challenging mode or 
        wants to play. In the first case, a message of Exit User Mode is shown and the first menu (User 
        Mode, Computer Mode, or Exit Game) is displayed. In the second case, it is compared the user’s 
        number and the computer’s numbers. 
        •   If both numbers are equal, that means that the user has guessed the number. So, the number 
            of tries is incremented and two messages are displayed: one indicating the user that has won 
            and the other one showing how many tries took him/her to guess the number. After that, User 
            Mode menu is shown letting the user choosing among the different options (Easy Mode, Difficult 
            Mode, Challenging Mode, or Exit User Mode). 
        •   If both numbers are not equal, another comparison is carried out, if the user’s number is 
            greater than the computer’s number. If it is greater, a message indicating that the number 
            entered is too high is shown. On the contrary, it is not greater, a message indicating that 
            the number entered is too low is shown. After that, the number of tries is incremented and a 
            message indicating the number of tries so far is displayed. 
    o   Next step is checking if time is up.  If time is up, a message indicating it is displayed and 
        the User Mode menu is shown letting the user choosing among the different options (Easy Mode, 
        Difficult Mode, Challenging Mode, or Exit User Mode). If time is not up, the game gives the option 
        to keep playing or exit the challenging mode. This process will be repeated until the time is up 
        or the user decides to exit the challenging mode.

-   Exit User Mode:

    o   A message of Exit User Mode is shown and the user comes back to the first menu (User Mode, 
        Computer Mode, or Exit Game).


* Second Scenario: Computer plays against the User
--------------------------------------------------
o   The game offers two different game options: play or exit. In the second case, an exit message is shown 
    and the user is addressed to the first menu (User Mode, Computer Mode, or Exit Game). In the first case, 
    the user chose the number that the computer has to guess. If the number entered is not correct, a message 
    of invalid option is shown and the user has the option of entering a valid number again.  This step will 
    be repeated until getting a valid number.
o   Once the number is valid, it is checked if the user wants to exit the computer mode or wants to play. In 
    the first case, a message of Exit Computer Mode is shown and the first menu (User Mode, Computer Mode, or 
    Exit Game) is displayed. In the second case, the computer picks a number and both numbers, the user one 
    and the computer one, are displayed. 
o   Next step is comparing the user’s number and the computer’s numbers. 
    •   If both numbers are equal that means that the computer has guessed the number. So, the number of tries 
        is incremented and two messages are displayed: one indicating that the computer has won and the other 
        one showing how many tries took the computer to guess the number. After that, the first menu (User Mode, 
        Computer Mode, or Exit Game) is displayed.
    •   If both numbers differ, another comparison is carried out, if the computer’s number is greater than the 
        user’s number. If it is greater, the number of tries is incremented and tries are displayed on a message. 
        Then, the value of the range is changed. The end value of the range is now the computer’s number because 
        it is greater than the user’s number.
        On the contrary, if it is not greater, the number of tries is incremented and tries are displayed on a 
        message. Then, the value of the range is changed. The initial value of the range is now the computer’s 
        number because it is less than the user’s number.
o   The game prompts to keep playing or exit the computer mode. If the option is exit, a message of exit is shown 
    and the first menu (User Mode, Computer Mode, or Exit Game) is displayed. In the case of keep playing, the 
    game gives the option to the computer to keep guessing. This process will be repeated until computer guesses 
    the number or decides to exit the computer mode.
"""

# ---------------------------------- Libraries ----------------------------------
import random # random module
import time # time module
# -------------------------------------------------------------------------------

# ---------------------------------- Functions ----------------------------------
# welcome message
def welcome():
    """ Display a welcome message """
    print()
    print("----------- Welcome to the Number Guessing Game!! -----------")
    print()
    print("Let's start!!")
 

# display initial menu: computer <-> user
def initialMenu ():
    """ Display Initial Menu: computer vs user or user vs computer """
    print()
    print("Which mode do you want to play?")
    print("  * User Mode - you play against the computer (you have to guess)             (1)")
    print("  * Computer Mode - the computer plays against you (computer has to guess)    (2)")
    print("  * Exit Game                                                                 (3)")
    print()


# display Main Menu 
def mainMenu():
    """ Display Main Menu """
    print()
    print("Menu options: ")
    print("  * Easy Mode            (1)")
    print("  * Difficult Mode       (2)")
    print("  * Challenging Mode     (3)")
    print("  * Exit User Mode       (4)")
    print()


# prompt the user to enter a menu option
def getMenuOption():
    """ Prompt the user to enter a Menu option """
    return (input("Please, enter an option: "))


# check if the option entered is valid
def isValidInitOption (op):
    """ Check that the user has introduced a valid option """
    if (op == '1') or (op == '2') or (op == '3'):
        return True
    else:
        return False


# check if the main menu option chosen by the user is valid
def isValidOption(op):
    """ Check if the option entered by the user is valid """
    if (op == '1') or (op == '2') or (op == '3') or (op == '4'):
        return True
    else:
        return False


# display a message of invalid option
def displayMessageInvalidOption(option):
    """ Display a message of invalid option chosen """
    print()
    print("The option", option, "is not valid.")
    print("Please, select a valid option.")
    print()


# get a valid option from the user
def getValidOption(isValid, option):
    """ check if the option is valid and prompt the user to enter a correct option in case it is not """
    while (isValid == False): 
        displayMessageInvalidOption(option) # display a message of invalid option
        mainMenu() # display Main Menu 
        option = getMenuOption() # prompt the user to enter a main menu option
        isValid = isValidOption(option) # check if the main menu option chosen by the user is valid
    else:
        return option


# display the menu and returns the option chosen by the user
def getOption():
    """ Display the menu and returns the option chosen by the user """
    mainMenu() # display Main Menu 
    op = getMenuOption() # prompt the user to enter a main menu option
    isValid = isValidOption(op) # check if the main menu option chosen by the user is valid
    option = getValidOption(isValid, op) # get a valid option from the user
    return option


# get a valid option from the user
def getValidInitOption(isValid, op):
    """ check if the option is valid and prompt the user to enter a correct option in case it is not """
    while (isValid == False):
        displayMessageInvalidOption(op) # display a message of invalid option
        initialMenu() # display Initial Menu 
        op = getMenuOption() # prompt the user to enter a initial menu option
        isValid = isValidInitOption(op) # check if the initial menu option chosen by the user is valid
    else:
        return op


# display the initial menu and returns the option chosen by the user
def getInitOption ():
    """" Display the initial menu and returns the option chosen by the user """
    initialMenu() # display Initial Menu 
    op = getMenuOption() # prompt the user to enter a initial menu option
    isValid = isValidInitOption(op) # check if the initial menu option chosen by the user is valid
    option = getValidInitOption(isValid, op) # get a valid option from the user
    return option


# display an Exit Message
def exitGame():
    """ Display a GoodBye message and Exit the game """
    print()
    print()
    print("------------------------- Exit Game -------------------------")
    #print("Hope to play again soon!!")
    print()


# display welcome message: User Mode
def displayMessageWelcomeUserMode():
    """ Display a welcome User Mode message """
    print()
    print()
    print("------------------------ User  Mode -------------------------")


# display message: Exit User Mode
def displayMessageExitUserMode():
    """ Display a message indicating that the user exit the user mode """
    print()
    print()
    print("---------------------- Exit User Mode -----------------------")
    print()


# display message: Easy Mode
def displayMessageWelcomeEasyMode():
    """ Display a welcome Easy Mode message """
    print()
    print()
    print("------------------------- Easy Mode -------------------------")
    print()
    print("****** You have unlimited attempts to guess the number ******")


# display message: Difficult Mode
def displayMessageWelomeDifficultMode():
    """ Display a welcome Difficult Mode message """
    print()
    print()
    print("----------------------- Difficult Mode ----------------------")
    print()
    print("********* You have 10 attempts to guess the number **********")


# display message: Challlenging Mode
def displayMessageWelcomeChallengingMode():
    """ Display a welcome Challenging Mode message """
    print()
    print()
    print("---------------------- Challenging Mode ---------------------")
    print()
    print("********** You have 60 seconds to guess the number **********")


# display welcome message: Computer Mode
def displayMessageWelcomeComputerMode():
    """ Display a welcome Computer Mode message """
    print()
    print()
    print("---------------------- Computer  Mode -----------------------")
    print()
    print("** The computer has unlimited attempts to guess the number **")


# display message: Exit Computer Mode
def displayMessageExitComputerMode():
    """ Display a message indicating that the user exit the computer mode """
    print()
    print()
    print("-------------------- Exit Computer Mode ---------------------")
    print()
# -------------------------------------------------------------------------------

# ---------------------------- Mode Functions -----------------------------------
# returns a random number between start and end
def pickRandomNumber(start, end):
    """ Pick a random number between start and end """
    return (random.randint(start, end))


# display Easy Mode Menu
def easyModeMenu():
    """ Display Easy Mode Menu """
    print()
    print("Menu options: ")
    print("  * Choose a number between 1 and 100")
    print("  * Exit Easy Mode (0)") 
    print()


# display Difficult Mode Menu
def difficultModeMenu():
    """ Display Difficult Mode Menu """
    print()
    print("Menu options: ")
    print("  * Choose a number between 1 and 100")
    print("  * Exit Difficult Mode (0)") 
    print()


# display Challenging Mode Menu
def challengingModeMenu():
    """ Display Challenging Mode Menu """
    print()
    print("Menu options: ")
    print("  * Choose a number between 1 and 100")
    print("  * Exit Challenging Mode (0)") 
    print()


# check if the option entered could be converted to int
def isPossibleConvert (op):
    """ Check if the option entered can be converted to int """
    found = 0
    for i in range (0,101,1):
        if (op == str(i)):
            found = 1
            break
    if (found == 1):
        return True
    else:
        return False
        

# check if the mode menu option chosen by the user is valid
def isModeValidOption(op):
    """ Check if the option entered by the user is valid """
    if ((op >= 1) and (op <= 100)) or (op == 0):
        return True
    else:
        return False


# get a valid option from the user
def getValidOptionMode(isValid, option, mode):
    """ check if the option is valid and prompt the user to enter a correct option """
    while (isValid == False): 
        displayMessageInvalidOption(option) # display a message of invalid option

        if (mode == "easy"):
            easyModeMenu() # display Easy Mode Menu
        elif (mode == "difficult"):
            difficultModeMenu() # display Difficult Mode Menu
        elif (mode == "challenging"):
            challengingModeMenu() # display Challenging Mode Menu
            
        option = getMenuOption() # prompt the user to enter a mode menu option
        if (isPossibleConvert(option)):
            op = int(option)
            isValid = isModeValidOption(op) # check if the mode menu option chosen by the user is valid
    else:
        return int(option)


# display mode menu and returns the option chosen by the user
def getOptionMode(mode):
    """ Display the mode menu and returns the option chosen by the user """
    if (mode == "easy"):
        easyModeMenu() # display Easy Mode Menu
    elif (mode == "difficult"):
        difficultModeMenu() # display Difficult Mode Menu
    elif (mode == "challenging"):
        challengingModeMenu() # display Challenging Mode Menu
        
    op = getMenuOption()  # prompt the user to enter a mode menu option
    if (isPossibleConvert(op)):
        option = int(op)
        isValid = isModeValidOption(option) # check if the mode menu option chosen by the user is valid
        if (not isValid):
            option = getValidOptionMode(isValid, op, mode) # get a valid option from the user
    else:
       option = getValidOptionMode(False, op, mode) # get a valid option from the user 
    return option


# check if computer's number is equals to user's number
def equalsNumbers (num_computer, num_user):
    """ Check if the number picked by the computer is the same that the number picked by the user """
    if (num_computer == num_user):
        return True
    else:
        return False


# check if user's number is greater than computer's number
def isGreater (num_computer, num_user):
    """ Check if the number entered by the user is greater than the number picked by the computer """
    if (num_user > num_computer):
        return True
    else:
        return False


# check if number of tries are equals to the maximun tries (Difficult Mode)
def isMaxTries (tries, max_tries):
    """ Check if the number of tries is equals to the maximun tries that the user has """
    if (tries == max_tries):
        return True
    else:
        return False


# display message: congratulations you guessed the number
def displayMessageWinner ():
    """ Display a message indicating the user that he/she has won """
    print()
    print("···· You have guessed the number! You WON! ····")
    print()
    

# display a message: tries that took the user to win
def displayMessageTriesToWin (tries):
    """ Display a message of the number of tries that took the user to win """
    print("···· It took you", tries, "tries to win. Well done!! ····")
    print()


# display message: too low
def displayMessageTooLow ():
    """ Display a message indicating that the number is too low """
    print()
    print("···· The number entered is lower than the one you have to guess. Try it again! ····")
    #print("                   ···· Try it again! ····")
    print()


# display message: too high
def displayMessageTooHigh ():
    """ Display a message indicating that the number is too high """
    print()
    print("···· The number entered is higher than the one you have to guess. Try it again! ····")
    #print("                   ···· Try it again! ····")
    print()


# display message of tries so far
def displayMessageTries (tries):
    """ Display a message with the number of times that the user has guessed the number """
    print("···· Number of tries so far:",tries,"····")


# display message of how many tries left 
def displayMessageTriesLeft (tries, max_tries):
    """ Display a message with the number of tries left that the user has to guess the number """
    print()
    if (max_tries - tries == 1):
        print("···· This is your last chance to guess the number! ····")
    else:
        print("···· You have", max_tries - tries, "tries left ····")


# display message: no more tries left
def displayMessageNoTriesLeft ():
    """ Display a message indicating that there are not more tries """
    print()
    print("···· No more tries left. GAME OVER!! ····")
    print()


# display a message: time is up
def displayMessageTimeIsUp ():
    """ Display a message indicating that time is up """
    print()
    print("···· Time is up!! GAME OVER!! ····")
    print()


# check if the time is less than 2 minutes
def timeIsUp (init_time, actual_time, max_seconds):
    """ check if the user still has time to play/guess """
    if ((actual_time - init_time) > max_seconds):
        return True
    else:
        return False

    
# function that controls Easy Mode functionality
def easyMode():
    """ Easy Mode Functionality """
    tries = 0 #number of guesses

    num = pickRandomNumber(1, 100)
    #print("Computer's number: ", num)
    option = getOptionMode("easy")
    
    while (option != 0):
        if (equalsNumbers(num, option)): # check if computer's number is equals to user's number
            tries = tries + 1
            displayMessageWinner()
            displayMessageTriesToWin(tries)
            break

        else:
            if (isGreater (num, option)): # if user's number is greater than computer's number
                displayMessageTooHigh()

            else:
                displayMessageTooLow()

            tries = tries + 1
            displayMessageTries(tries)

        option = getOptionMode("easy")


# function that controls Difficult Mode functionality
def difficultMode ():
    """ Difficult Mode Functionality """
    tries = 0 # number of guesses
    max_tries = 10 # maximun number of tries that the user has to guess the number

    num = pickRandomNumber(1, 100)
    #print("Computer's number: ", num)
    option = getOptionMode("difficult")

    while (option != 0):
        if (equalsNumbers(num, option)): # check if computer's number is equals to user's number
            tries = tries + 1
            displayMessageWinner()
            displayMessageTriesToWin(tries)
            break

        else:
            if (isGreater (num, option)): # if user's number is greater than computer's number 
                displayMessageTooHigh()

            else:
                displayMessageTooLow()

            tries = tries + 1
            displayMessageTries(tries) 

            if (isMaxTries(tries, max_tries)): # if no more tries left
                displayMessageNoTriesLeft()
                break
            else:
                displayMessageTriesLeft(tries, max_tries)

        option = getOptionMode("difficult")
    

# function that controls Challenging Mode functionality 
def challengingMode ():
    """ Challenging Mode Functionality """
    tries = 0 #number of guesses
    max_seconds = 60 # number of seconds that the user has to guess the number

    num = pickRandomNumber(1, 100)
    #print("Computer's number: ", num)
      
    init_time = time.time() # set the timer
    
    option = getOptionMode("challenging")

    while (option != 0):
        if (equalsNumbers(num, option)): # check if computer's number is equals to user's number
            tries = tries + 1
            displayMessageWinner()
            displayMessageTriesToWin(tries)
            break

        else:
            if (isGreater (num, option)): # if user's number is greater than computer's number 
                displayMessageTooHigh()  

            else:
                displayMessageTooLow()

            tries = tries + 1
            displayMessageTries(tries) 

            actual_time = time.time()
            if (timeIsUp (init_time, actual_time, max_seconds)): # check if time is up
                displayMessageTimeIsUp()
                break             
        
        option = getOptionMode("challenging")          

# -------------------------------------------------------------------------------

# ---------------------------- Computer's Functions -----------------------------
# display Computer Mode Menu
def computerModeMenu():
    """ Display Computer Mode Menu """
    print()
    print("Menu options: ")
    print("  * Choose a number between 1 and 100")
    print("  * Exit Computer Mode (0)") 
    print()


# display Computer Play Menu
def computerPlayMenu():
    """ Display Computer Play Menu (let the computer play again or exit )"""
    print()
    """
    print("Menu options: ")
    print("  * Press any key to keep playing ")
    print("  * Exit Computer Mode  (0)")
    """
    print()
    op = input("**** Press any key to keep playing  or   Exit Computer Mode  (0):  ")
    print()
    return op


# check if the option chosen is valid
def isComputerValidOption (op, start, end):
    """ Check if the option entered is valid """
    if ((op >= start) and (op <= end)) or (op == 0):
        return True
    else:
        return False


# check if the option chosen is keep playing or exit game
def keepPlaying (op):
    """ Check if the option chosen is keep playing or exit game """
    if (op != '0'): #keep playing
        return True
    else: # exit game
        return False


# get a valid option from the user
def getValidUserOption(isValid, op, start, end):
    """ Check if the option is valid and prompt the user to enter a correct option in case it is not """
    while (isValid == False):
        displayMessageInvalidOption(op) # display a message of invalid option
        computerModeMenu() # display computer mode menu
        option = getMenuOption() # prompt the user to enter a user menu option
        if (isPossibleConvert(option)):
            op = int(option)
            isValid = isComputerValidOption (op, start, end) # check if the option chosen is valid
    return int(op)


# display the user menu and returns the option chosen by the user
def getUserOption (start, end):
    """" Display the user menu and returns the option chosen by the user """
    computerModeMenu() # display computer mode menu
    option = getMenuOption() # prompt the user to enter a user menu option
    if (isPossibleConvert(option)):
        op = int(option)
        isValid = isComputerValidOption (op, start, end) # check if the option chosen is valid
        if (not isValid):
            op = getValidUserOption(isValid, option, start, end) # get a valid option from the user
    else:
        op = getValidUserOption(False, option, start, end) # get a valid option from the user
    return op    


# display user's number
def displayUsersNumber (num):
    """ Display the number chosen by the user """
    print()
    print("···· The number that you chose is", num, " ····")


# display computer's number
def displayComputersNumber (num):
    """ Display the number chosen by the computer """
    print()
    print("···· The number chosen by the computer is", num, " ····")
    print()


# display message: computer guessed the number
def displayComputerMessageWinner ():
    """ Display a message indicating that the computer has won """
    print()
    print("···· The computer has guessed the number! It WON! ····")
    print()
    

# display a message: tries that took the computer to win
def displayComputerMessageTriesToWin (tries):
    """ Display a message of the number of tries that took the computer to win """
    print("···· It took the computer", tries, "tries to win. ····")
    print()



# function that controls Computer Mode functionality
def computerMode():
    """ Function that controls Computer Mode functionality """
    # range between start and end (for example: 1 and 100)
    start = 1 # start number of the range
    end = 100 # end number of the range
    tries = 0 #number of guesses
        
    option = getUserOption(start, end) # display the computer mode menu and returns the option chosen by the user

    if (option == 0): #if the first time the option chosen is Exit Computer Mode
        displayMessageExitComputerMode()

    else:

        displayUsersNumber(option) # display the number chosen by the user

        num = pickRandomNumber(start, end)  #computer picks a number
        displayComputersNumber(num) # display the number chosen by the computer

        while (option != 0):
            if (equalsNumbers(num, option)):  #check if this option works!!!!
                tries = tries + 1
                displayComputerMessageWinner()
                displayComputerMessageTriesToWin(tries)
                #break

                start = 1 # start number of the range
                end = 100 # end number of the range
                #range = [start, end]
                tries = 0 #number of guesses

                option = getUserOption(start, end) # display the computer mode menu and returns the option chosen by the user

                if (option != 0):
                    displayUsersNumber(option) # display the number chosen by the user
                    num = pickRandomNumber(start, end)  #computer picks a number
                    displayComputersNumber(num) # display the number chosen by the computer

            else:
                if (isGreater(option, num)): #if computer's number > user's number
                     end = num # computer's number become the end number of the range [start, computer's number]
                     #print("range: [",start,",",end,"]")

                else:
                    start = num  # computer's number become the start number of the range [computer's number, end]

                tries = tries + 1
                displayMessageTries(tries) 
                # print("range: [",start,",",end,"]")

                op = computerPlayMenu()
                #op = getMenuOption()
            
                if (keepPlaying (op)): # keep playing
                    displayUsersNumber(option) # display the number chosen by the user
                    num = pickRandomNumber(start, end)  #computer picks a number
                    displayComputersNumber(num) # display the number chosen by the computer

                else:
                    option = 0 # exit computer mode game 
                    displayMessageExitComputerMode()
                    break

        else:
            displayMessageExitComputerMode()
# -------------------------------------------------------------------------------

# --------------------------------- Main Program --------------------------------
welcome() # welcome message
op =  getInitOption () # display the initial menu and returns the option chosen by the user

while (op != '3'):

    if (op == '1'): # You play against the computer (you have to guess)
        displayMessageWelcomeUserMode()
        option = getOption() # display the menu and returns the option chosen by the user

        while (option != '4'):
            if (option == '1'): # play Easy Mode
                displayMessageWelcomeEasyMode()
                easyMode()
            elif (option == '2'): # play Difficult Mode
                displayMessageWelomeDifficultMode()
                difficultMode()
            else: # play Challenging Mode
                displayMessageWelcomeChallengingMode()
                challengingMode()
                           
            option = getOption() # display the menu and returns the option chosen by the user
                    
        else:
            # exit User Mode
            displayMessageExitUserMode()

    elif (op == '2'): # The computer plays against you (computer has to guess)
        displayMessageWelcomeComputerMode()
        computerMode() 

    op =  getInitOption() # display the initial menu and returns the option chosen by the user

else:
    exitGame()
# -------------------------------------------------------------------------------
