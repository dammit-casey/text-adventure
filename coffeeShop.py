#Stephen
#Jan/31/2022
#Coffee Shop


print()
print()
print("     #######################")
print("     #                     #")
print("     #     coffee shop     #")
print("     #                     #")
print("     #######################")
print()
print("Cold rain sprinkles the air around you.")
print("Bundled tight you turn a corner and find a coffee shop.")
print("The warm glow of light radiates outwards.")

#1st question
def enter_coffeeshop():
    print()
    print("The bell chimes as you open the door,")
    print("The sound of happy customers floods the room as they chatter without worry.")
    print("A voice cuts the air,")
    print("\"I'll Be Right With You\"!")
    print()
    print("A short woman weasels through the crowd to greet you,")


do_you_enter = input("\nWould you like to go in?").upper()
if do_you_enter == "NO" or do_you_enter == "N":
    print()
    print("You carry on, wet and cold.")
elif do_you_enter == "YES" or do_you_enter == "Y":
    enter_coffeeshop()

#For how many
def follow_me():
    print("")
    print("\"Please follow me\"")
    print("\"There's a table by the window over here.\"")
    print("She leads you through the busy room to a cozy table in the corner.")
    print("You take your seat and scoot yourself in")
    print("\"Here is a menu, i'll be back in a moment.\"")
    print("The menu is short, but you take your time to read it.")
    print("  ____________________")
    print(" |        MENU        |")
    print(" |                    |")
    print(" |  1 Bagel    $1.50  |")
    print(" |  2 Coffee   $0.50  |")
    print(" |  3 Macaroon $4.00  |")
    print(" |  4 Fries    $5.00  |")
    print(" |                    |")
    print("  --------------------")

how_many = input("\"Hi there, for how many?\"")
if how_many == str(1):
    follow_me()
else:
    print("\"If you say so\"")
    print("...")
    follow_me()

inventory = {"Bagel": 1.50, "Coffee": 0.50, "Macaroon": 4, "Fries":5}

#Give Food Map ask if need more time

#Eat tasty food

#Grab and add up bill
