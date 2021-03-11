from random import randrange

def option():
    choice = input("Ready to play? (yes/no): ").lower().strip()

    if choice == "yes":
        print("Great! :)")
        return choice
    elif choice == "no":
        print("That's too bad :(")
        exit()
    else:
        print("Invalid option! Try again!")
        option()

def continueRoll(otherNum):
    playAgain = input("Would you like to try again...? (yes/no): ").lower().strip()

    if playAgain == "yes":
        sameNum = input("Do you want to keep the same number? (yes/no): ").lower().strip()
        if sameNum == "yes":
            otherSum = playGame()
            logic(otherNum, otherSum)
        elif sameNum == "no":
            selectNum()
        else:
            print("Not an option! Choose 'yes' or 'no' please.")
            continueRoll(otherNum)
    elif playAgain == "no":
        print("Okay, we'll let you go :( thanks for playing!")
        exit()
    else:
        print("Not an option! Choose 'yes' or 'no' please.")
        continueRoll(otherNum)

def logic(number, sum):
    if number != sum:
        print("You rolled a %d, your number was %d, you lose :(" % (sum, number))
        continueRoll(number)

    else:
        print("You rolled a %d, your number was %d!, you win :)" % (sum, number))
        continueRoll(number)

def playGame():
    roll = input("Whenever you're ready, roll the die (roll): ").lower().strip()

    if roll == "roll":
        diceOne = randrange(1, 6)
        diceTwo = randrange(1, 6)

        sumDice = diceOne + diceTwo

        return sumDice

    else:
        print("Still not ready? Choose 'roll' to play..... (roll)")
        playGame()

def selectNum():
    userNumber = int(input("Start by choosing a number between 2 and 12: "))

    if userNumber < 2:
        print("Number is too low...try again...")
        selectNum()
    elif userNumber > 12:
        print("Number is too high... try again...")
        selectNum()
    else:
        print("You chose %d, let us continue with the game!" % userNumber)
        sumRoll = playGame()
        logic(userNumber, sumRoll)

if __name__ == '__main__':

    print("Welcome to the Dice Rolling Game!")
    print("Created by Isaac Lacombe")
    print("Rules: \tChoose a number between 2 and 12")
    print("\t\tRoll two die and if they land on your number, you win!")
    print("\t\tIf it doesn't you lose...")

    option()
    selectNum()