"""
Author: Omar Adel Badawy
Date: 17/12/2021
Description: Game every player takes a number from the list of any player whose sum equal 15 first Win!

"""

play_list = [1,2,3,4,5,6,7,8,9]
player1_list = []
player2_list = []

def player1_turn():
    global play_list, player1_list
    
    print(play_list)
    select1 = int(input(" player 1 choose number from the list: \n "))

    if select1 in play_list:
        player1_list.append(select1)
        play_list.remove(select1)

    else:
        print("your selection is not in the list please try again!!")
        player1_turn()

    check_winner1()
        

def player2_turn():
    global play_list, player2_list
    
    print(play_list)
    select2 = int(input(" player 2 choose number from the list: \n "))

    if select2 in play_list:
        player2_list.append(select2)
        play_list.remove(select2)

    else:
        print("your selection is not in the list please try again!!")
        player2_turn()

    check_winner2()


def check_winner1():
    stop = False
    try:
        if (player1_list[0]+player1_list[1]+player1_list[2] == 15 or player1_list[0]+player1_list[2]+player1_list[3] == 15 
        or player1_list[1]+player1_list[2]+player1_list[3] == 15 or player1_list[0]+player1_list[1]+player1_list[3] == 15):
            print("\n Player 1 WIN !!\n")
            stop = True
    except:
        pass
    
    if stop == True:
        quit()


def check_winner2():
    stop = False
    try:
        if (player2_list[0]+player2_list[1]+player2_list[2] == 15 or player2_list[0]+player2_list[2]+player2_list[3] == 15 
        or player2_list[1]+player2_list[2]+player2_list[3] == 15 or player2_list[0]+player2_list[1]+player2_list[3] == 15):
            print("\n Player 2 WIN !!\n") 
            stop = True          
    except:
        pass
    
    if stop == True:
        quit()


for i in range(4):
    player1_turn()
    player2_turn()

print("The game is a draw !!")
