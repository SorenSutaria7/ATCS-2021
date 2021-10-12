list = ['minecraft', 'fortnite', 'COD', 'fifa']

print("I like to play: " + list[0] + ", " + list[1] + ", " + list[2] + ", " + list[3])

cont = raw_input("Would you like to add a game(y/n): ")
while(cont == "y"):
    new_game = raw_input("What game do you like to play: ")
    list.append(new_game)
    cont = raw_input("Would you like to add another game(y/n): ")

print("We like to play: ")
for game in list:
    print(game)