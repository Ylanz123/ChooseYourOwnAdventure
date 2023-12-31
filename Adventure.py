import random
import math


class StoryData:
    best_friend_name = "Jimothy the Fourth"
    what_are_we_fighting = None


def print_options(options):
    for option in options:
        print(option)


def forget_about_jimothy(story_data):
    print("You arrive safely at your home planet. As you're relaxing, you hear a knock on your door as Jimothy "
          "has come to take revenge. He executes you. Better luck next time :)")


def send_out_rescue_ship_to_jimothy(story_data):
    print("You arrive safely at your home planet and Jimothy is waiting for you. He thanks you and gives you "
          "a hefty reward for saving him from the", story_data.what_are_we_fighting)


def damaged_life_support(story_data):
    options = ["0: Manually repair them",
               "1: Send repair bot",
               "2: Ignore it"]
    print_options(options)
    user_input = input("What do you do?")
    if user_input == "0":
        print("You grab a wrench and successfully repair your life support systems. You blast into hyperspace and "
              "arrive safely at your home planet.")
    if user_input == "1":
        print("You send the repair bot but it malfunctions. Your life support systems fail and you suffocate. "
              "GG thanks for playing :)")
    if user_input == "2":
        print("You ignore your failing life support systems. Just as you are about to blast off, clouds of toxic"
              " smoke envelops the ship and you die a painful death from suffocation. GG, shouldn't ignore failing"
              " life support systems :)")
    pass


def start_engines_and_fly_out(story_data):
    print(
        "You realise as you're lightyears away from where you entered hyperspace that you have forgotten your best friend,",
        story_data.best_friend_name, ", at the mining outpost.")
    print("What do you do?")

    options = ["0: Turn the ship around and head back to them",
               "1: Leave him to continue mining and making profit for you",
               "2: Call a rescue ship to retrieve your best friend"]

    print_options(options)

    user_input = input("What is your choice: ")
    if user_input == "0":
        print("You quickly activate the hyperjump engines and within seconds you emerge right in front of the",
              story_data.what_are_we_fighting, ", it destroys your ship and you perish")
        print("RIP the end. Thank you again for playing")
    if user_input == "1":
        print("You decide it's in your best interest to forget about", story_data.best_friend_name,
              "and continue your journey through space.")
        forget_about_jimothy(story_data)
    if user_input == "2":
        print("You phone up RescueCorp and they promptly send a ship out to collect", story_data.best_friend_name)
        send_out_rescue_ship_to_jimothy(story_data)


def main_function():
    story_data = StoryData()

    intro_text_1 = "You are at the mining planet B27-2. You look out into the vastness of the cosmos. In the distance you see"
    intro_text_1_options = ["a giant space worm",
                            "an asteroid",
                            "an alien spaceship"]

    fight_options = ["giant space worm",
                     "asteroid",
                     "alien spaceship"]

    intro_text_2 = "coming towards you. What do you do?"

    action_options_1 = ["0: Run to the cockpit",  # Good option
                        "1: Run to the turret",  # Leads to a chain of events
                        "2: Stand and watch"]  # Dead

    random_number = math.floor(random.random() * len(intro_text_1_options))
    story_data.what_are_we_fighting = fight_options[random_number]
    print(intro_text_1, intro_text_1_options[random_number], intro_text_2)

    print_options(action_options_1)

    user_input = input("What is your choice: ")

    if user_input == "0":
        print("You run to the cockpit, start the engines, and blast on out of there, narrowly avoiding destruction.")
        start_engines_and_fly_out(story_data)
    if user_input == "1":
        print("You blast the", story_data.what_are_we_fighting, "and it is obliterated! A piece of the",
              story_data.what_are_we_fighting, "comes out from behind the explosion and crashes"
                                               " in to your life support systems. Every alarm on the ship is blaring.")
        damaged_life_support(story_data)
    if user_input == "2":
        print("You watch as the", story_data.what_are_we_fighting, "hurdles towards you and obliterates your ship.")
        print("You die. The end. Thanks for playing :)")


if __name__ == "__main__":
    main_function()
