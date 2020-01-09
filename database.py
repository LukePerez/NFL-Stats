import sys
Drew_Lock = {
    'Name': "Drew Lock",
    'Starts': 3,
    'Completing': "61.1% of his passes",
    'Yards': 651,
    'Touchdowns': 5,
    'Interceptions': 3
    }
Tom_Brady = {
    'Name': "Tom Brady",
    'Starts': 14,
    'Completing': "60.1% of his passes",
    'Yards': 3565,
    'Touchdowns': 21,
    'Interceptions': 7
    }
Patrick_Mahomes = {
    'Name': "Patrick Mahomes",
    'Starts': 12,
    'Completing': "65.7% of his passes",
    'Yards': 3606,
    'Touchdowns': 23,
    'Interceptions': 4
    }
Russell_Wilson = {
    'Name': "Russell Wilson",
    'Starts': 14,
    'Completing': "67.4% of his passes",
    'Yards': 3708,
    'Touchdowns': 28,
    'Interceptions': 5
    }  
players = [
    Drew_Lock, Tom_Brady, Patrick_Mahomes, Russell_Wilson
    ]


print("Welcome to the NFL stat anylizer!!\n")
def prompt():# Asks user for player selection
    while True:
        print("Would you like to research a player's stats?")
        response = input("Enter y or n: ")
        if response == 'y':
            answer = input("Please enter a player: ")
            return answer
        elif response == 'n':# Kills the program
            print("Good-bye!")
            sys.exit()
        else:
            print("Invalid input.\n")


def get_player(name): # Connects user input to player from 'players' list
    for things in players: # Iterates through players list
        for key, value in things.items(): # Settles on name key
            if value == name: #If name value is same as input, application proceeds
                return things #returns chosen dictionary
    print("Player not found. Be sure to spell and capitalize corectly!")
    program_body()# Returns to main function

                
def stats(player):
    print("\n")
    for key, value in player.items(): #Iterates through player dict key:value pairs
        if key == 'Name': #Does not print name key
            print(value)
            continue
        print(key + " " + str(value))
    print("\n")


def program_body():
    while True: #Loops until user selects 'n' under prompt()
        true_player = get_player(prompt())
        stats(true_player)


program_body() #ultimately, a single function call
