#Experimenting with functions and conditional statements in a text-based adventure game.

#Define the main function to start the game.
def start_game():
    
    #Function loop allowing for replayability.
    while True:
        player_name = input('Enter your name: ')
        print(f'Welcome {player_name}, to an adventure game!')
        first_choice = input('You see a massive cave entrance, would you like to enter the cave or follow a path to a nearby forest? (Cave/Forest): ')
        
        #Defining the cave path based on user input.
        if first_choice.lower() == 'cave':
            def cave_path():
                cave_choice = input('Inside the cave, you see a glittering treasure chest and a sleeping dragon. Do you want to open the chest or sneak past the dragon? (Chest/Dragon): ')
                if cave_choice.lower() == 'chest':
                    
                    #If the player wins the game.
                    print('You found gold and jewels! You win!')
                elif cave_choice.lower() == 'dragon':
                    
                    #If the players loses the game.
                    print('The dragon wakes up and devours you whole!')
                else:
                    
                    #If the input doesn't match expected options.
                    print('Invalid choice. Game over, retry?')
            cave_path()
        
        #Defining the forest path based on user input.
        #Function mirrors the cave path structure.
        elif first_choice.lower() == 'forest':
            def forest_path():
                forest_choice = input('In the forest, you find a sparkling river and a tall tree with a rope ladder. Do you want to swim in the river or climb the tree? (River/Tree): ')
                if forest_choice.lower() == 'river':
                    print('You are ambushed by river crocodiles! Game over, retry?')
                elif forest_choice.lower() == 'tree':
                    print('You scale the massive tree and over the horizon, you spot a hidden sanctuary filled with magical flora! You win!')
                else:
                    print('Invalid choice. Game over, retry?')
            forest_path()
        else:
            
            #If the first_choice input doesn't match expected options.
            print('Invalid choice. Game over, retry?')
        
        #Allows the player to choose to replay or exit the game.
        retry = input('Do you want to play again? (yes/no): ')
        if retry.lower() != 'yes':
            print('Thanks for playing! Goodbye!')
            
            #Exits the loop.
            break

#Begins the function when the script is run.
start_game()