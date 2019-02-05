# CIS118_FinalProject
# Description: Number Guessing Game

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
