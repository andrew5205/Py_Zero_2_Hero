
example = [1, 2, 3, 4, 5, 6,7 , 8, 9, 10]

from random import shuffle

result = shuffle(example)
print(result)               # None  // shuffle wont return anything 

# have to include shuffle into a function
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

print(shuffle_list(example))



# game to shuffle the list
my_other_list = [" ", "O", " "]
shuffle_game = shuffle_list(my_other_list)
print(shuffle_game)


# player guess
def player_guess():
    guess = ""
    while guess not in [0, 1, 2]:
        guess = input("Pick a number: 0, 1, or 2")
    return int(guess)
result = player_guess()
print(result)


def check_guess(my_other_list, guess):
    if my_other_list[guess] == "O":
        print("Correct!!")
    else:
        print("try again")
        print(my_other_list)


