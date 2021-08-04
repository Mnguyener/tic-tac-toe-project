from IPython.display import clear_output
def main():
    # user_check()
    display_game(row1,row2,row3)
    position_choice()
    replacement_choice(row1,1)
    gameon_choice()

def user_check():

    choice = ''
    acceptable_range = range(0,11)
    within_range = False

    while choice.isdigit() == False or within_range == False:

        choice = input("Please enter a number (0-10): \n")

        # DIGIT CHECK
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
        # RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range == True
                break
            else:
                within_range == False
    return choice

row1 = [0,1,2]
row2 = [3,4,5]
row3 = [6,7,8]
    # for tic tac toe, see if you can print out three rows for the player to choose from
def display_game(row1, row2, row3):
    print("Here is the current board: ")
    print(row1)
    print(row2)
    print(row3)



def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2']:
        choice = input("Pick a position (0,1,2): \n")

        if choice not in ['0','1','2']:
            print("Sorry,invalid choice!")
    return int(choice)

def replacement_choice(row, position):


    position_index = (input("Type in a X or O at position: \n")).upper()
    row[position] = position_index
    print(row)
    return row

def gameon_choice():

        choice = 'null'
        while choice not in ['Y','N']:
            choice = (input("Do you want to continue the game? \n")).upper()

            if choice not in ['Y','N']:
                print("Sorry, I don't understand. Please choose Y or N! ")
        if choice == 'Y':
            return True
        #indiciates the game is still on
        else:
            return False
        return int(choice)

game_on = True
row1 = [0,1,2]
row2 = [3,4,5]
row3 = [6,7,8]

while game_on:

    display_game(row1,row2,row3)

    position = position_choice()
    # have to assign the variable again because it was a local variable

    row = replacement_choice(row1, position)
    # these were also local variables in previous functions

    display_game(row1,row2,row3)
    # displays the updated positions

    game_on = gameon_choice()






if __name__ == '__main__':
    main()