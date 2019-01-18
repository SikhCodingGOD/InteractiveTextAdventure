import world, tiles
from Player import Player

def play():
    world.load_tiles()
    player = Player()
    while player.is_alive() and not player.victory:
        #sets room variable to the tile where the player is
        room = world.tile_exists(player.location_x,player.location_y)
        if player.in_battle == False and player.in_shop == False:
            print(room.intro_text(),"\n")
        room.modify_player(player)
        #Check again as room can change the player's state
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions(player)
            for action in available_actions:
                print(action)
            player_action = input("What do you do?\n")
            for action in available_actions:
                if player_action == action.name:
                    player.do_action(action,**action.kwargs)
                    break
            if player_action != action.name:
                print("That is not a valid action.")
    if not player.is_alive():
        print("You have been slain!\nYour remains will rot for eternity...")
    if player.victory:
        print("Congratulations! You have completed the Interactive Text Adventure by Jovin Bains.\n\
Version 2.0 is in the works and will be finished in the near future. Contact Jovin Bains for further details.")

#always at the bottom of file, runs the game when the file is opened
if __name__ == "__main__":
    play()
