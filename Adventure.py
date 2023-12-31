import random
import math

best_friend_name = "Jimothy the Fourth"

what_are_we_fighting = ["giant space worm",
                        "asteroid",
                        "alien spaceship"]

random_number = 0

def print_options(options):
    for option in options:
        print(option)

def forget_about_jimothy():
    pass

def send_out_rescue_ship_to_jimothy():
    pass

def damaged_life_support():
    pass

def start_engines_and_fly_out():
    print("You realise as you're lightyears away from where you entered hyperspace that you have forgotten your best friend,", best_friend_name,", at the mining outpost.")
    print("What do you do?")

    options = ["0: Turn the ship around and head back to them",
               "1: Leave him to continue mining and making profit for you",
               "2: Call a rescue ship to retrieve", best_friend_name, "and deal with the", what_are_we_fighting[random_number]]

    print_options(options)

    user_input = input("What is your choice: ")
    if user_input == "0":
        print("You quickly activate the hyperjump engines and within seconds you emerge right in front of the", what_are_we_fighting[random_number], ", it destroys your ship and you perish")
        print("RIP the end. THank you again for playing")
    if user_input == "1":
        print("You decide it's in your best interest to forget about", best_friend_name, "and continue your journey through space.")
        forget_about_jimothy()
    if user_input == "2":
        print("You phone up RescueCorp and they promptly send a ship out to collect", best_friend_name)
        send_out_rescue_ship_to_jimothy()

def main_function():
    intro_text_1 = "You are at the mining planet B27-2. You look out into the vastness of the cosmos. In the distance you see"
    intro_text_1_options = ["a giant space worm",
                            "an asteroid",
                            "an alien spaceship"]

    intro_text_2 = "coming towards you. What do you do?"

    action_options_1 = ["0: Run to the cockpit",  # Good option
                        "1: Run to the turret",  # Leads to a chain of events
                        "2: Stand and watch"]  # Dead

    random_number = math.floor(random.random() * len(intro_text_1_options))
    print(intro_text_1, intro_text_1_options[random_number], intro_text_2)

    print_options(action_options_1)

    user_input = input("What is your choice: ")

    if user_input == "0":
        print("You run to the cockpit, start the engines, and blast on out of there, narrowly avoiding destruction.")
        start_engines_and_fly_out()
    if user_input == "1":
        print("You blast the", what_are_we_fighting[random_number], "and it is obliterated! A piece of the", what_are_we_fighting[random_number], "comes out from behind the explosion and crashes"
                                                                    " in to your life support systems. Every alarm on the ship is blaring.")
        damaged_life_support()
    if user_input == "2":
        print("You watch as the", what_are_we_fighting[random_number], "hurdles towards you and obliterates your ship.")
        print("You die. The end. Thanks for playing :)")


if __name__ == "__main__":
    main_function()
