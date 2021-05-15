# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#Monster & player set of commmands

# Monster Game template
print("Hello, Welcome to the Monster Game")
print("What is your name? ")
player = raw_input()
print("Hello, " + player)
print("Who is your worst enemy? ")
monster = raw_input()
print("Okay, you are going to play a game against " + monster)
player_health_points = 1000
monster_health_points = 1000
print("You can attack the monster (1)."
      "Heal yourself (2)."
      "Ask what the current status of the fight is. (3)")
print("What do you want to do?")
next_action = raw_input()  # type: int
for num in next_action:
    if (next_action == 1):
        monster_health_points = monster_health_points - 10
        print("Great move!")
        print("Now Monster will attack back!")
    elif (next_action == 2):
        print(num)
        print("Healing..")
    player_health_points = player_health_points + 10
    else:
        print('The score now is {} : {}'.format(player_health_point)(monster_health_points))
def score():
    if player_health_points > monster_health_points:
        print("You win!")
        print("Do you want to play another game?")
    elif player_health_points == monster_health_points:
        print("Its a tie! Try again")
    else:
        print("Game over")

