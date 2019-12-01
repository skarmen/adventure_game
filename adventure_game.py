import time
import random

from termcolor import colored

items = []
creatureType = ['gorgon', 'troll', 'dragon', 'zombie']
weaponType = ['Sword of Ogoroth', 'Magic Missile', "Flame Ax"]
creature = random.choice(creatureType)
weapon = random.choice(weaponType)


def print_pause(message_to_print, color='yellow'):
    """ Print messages with pause

    :param str message_to_print: message to print
    """
    #print(message_to_print)
    print(colored(message_to_print, color))
    time.sleep(0.2)


def valid_input(prompt, option1, option2):
    """Get valid input

    This function will only return once the input corresponds to
    one of the options.

    :param str prompt: the message to print
    :param str option1: the first option
    :param str option2: the second option
    :return: one of option1 or option2
    """

    while True:
        print(colored(prompt, color='green'))
        response = input()
        # for option in option1 and option2:
        # if option1 or option2 in reponse:
        if (option1 == response) or (option2 == response):
            return response


def field():
    """ Print messages to describe the field setting"""
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {creature} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.")


def get_main_choice():
    """Get the main choice and act on it"""
    prompt = ("(Please enter 1 or 2.)\n")
    option1 = '1'
    option2 = '2'
    print_pause("Enter 1 to knock on the door of the house.\n"
                "Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    # TODO: use valid_input()
    response = valid_input(prompt, option1, option2)
    if response == option1:
        house()
    elif response == option2:
        cave()


def to_play_again():
    """ Get the valid_input for play_again"""
    play_again = valid_input("Would you like to play again? (y/n)", 'y', 'n')
    if play_again == 'y':
        print_pause("Excellent! Restarting the game...")
        field()
        get_main_choice()  # restart the game ( call the main function + intro)
    elif play_again == 'n':
        print_pause("Thanks for playing! See you next time.")


def to_fight_or_run():
    """ Get the valid_input for fight_or_run"""
    fight_or_run = valid_input("Would you like to (1) fight or (2) run away? ",
                               '1', '2')
    if fight_or_run == '1':
        if 'sword' in items:
            print_pause(f"As the {creature} moves to attack, you unsheath  "
                        f"your new {weapon}.")
            print_pause(f"The {weapon} shines brightly in your hand as you "
                        "brace yourself for the attack.")
            print_pause(f"But the {creature} takes one look at your shiny "
                        "new toy and runs away!")
            print_pause(f"You have rid the town of the {creature}. "
                        "You are victorious!")
        else:
            print_pause("You do your best...\n"
                        f"but your dagger is no match for the {creature}.")
            print_pause("You have been defeated!")
        to_play_again()
    elif fight_or_run == '2':
        print_pause("You run back into the field. Luckily, you don't seem to "
                    "have been followed.")
        print_pause(" ")
        get_main_choice()


def cave():
    """ Print messages to describe the cave setting"""
    if 'sword' in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You have been here before, and gotten all "
                    "the good stuff."
                    "It's just and empty cave now.")
        print_pause("You walk back out to the field.")
        get_main_choice()
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of a metal behind a rock.")
        print_pause(f"You have found the magical {weapon}")
        items.append("sword")
        print_pause("You discard you silly old dagger and take the "
                    f"{weapon} with you.")
        print_pause("You walk back out to the field.")
        print_pause(" ")
        get_main_choice()


def house():
    """ Print messages to describe the cave setting"""
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens"
                f" and out steps a {creature}.")
    print_pause(f"Eep! This is the {creature}'s house!")
    print_pause(f"The {creature} attacks you!")

    # TODO: this should only happen if we don't have a sword
    if 'sword' not in items:
        print_pause("You feel a bit under-prepared for ths, "
                    "what with only having a tiny dagger.")
    to_fight_or_run()  # do I need else here?


def main():
    """ Main function running the game"""
    field()
    get_main_choice()

if __name__ == '__main__': 
    # the if statetment is tru when run directly from the shell $ and the funct ion gets called 
    # if imported it only executes any code outside the functions 
    # or if __name__ == '__adventure_game__'
    main()

if __name__ == '__main__':
    # this file was run directly from the command line
    pass
if __name__ == '__adventure_game__':
    # this file was imported from another file
    pass
