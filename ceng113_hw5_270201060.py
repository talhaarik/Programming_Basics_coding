#  Talha Arık 270201060
import random

class Gamebot:

    def __init__(self, play_hand, stack):
        self.play_hand = play_hand                  # a reference to the player's hand
        self.stack = stack                          # a reference to the stack
        self.count_deck = [['b', 1], ['b', 1], ['b', 1], ['b', 2],  # a list to count the remaining
                           ['b', 2], ['b', 3], ['b', 3], ['b', 4],  # cards in the deck
                           ['w', 1], ['w', 1], ['w', 1], ['w', 2],
                           ['w', 2], ['w', 3], ['w', 3], ['w', 4]]
        for card in play_hand:                      # bot has already seen the player's hand,so it knows
            self.update_count_deck(card)            # that those cards are not in the deck anymore.
        self.hand = [['!', -1], ['!', -1], ['!', -1]]    # bot's hand. '!' indicates unknown color,
                                                         # -1 indicates unknown value

    def get_tip(self, tip):
        tip = tip.split(",")
        for i in range(len(tip)-1):
            if (tip[-1] == "b" or tip[-1] == "w"):  # if the tip given is related to the letter
                self.hand[int(tip[i]) - 1][0] = tip[-1]
            else:  # if the tip given is related to the number
                self.hand[int(tip[i]) - 1][1] = int(tip[-1])


    def update_count_deck(self, card):
        self.count_deck.remove(card)


    def update_hand(self, num):
        self.hand.pop(num)
        if (len(deck) > 0):  # If there are any cards left in the deck
            self.hand.append(["!", -1])
        return num


    def give_tip(self):
        my_array = play_hand
        num_array = [0, 0, 0, 0]
        flag_num = False
        for elem in my_array:
            for i in range(1, 5):
                if (elem[1] == i):
                    num_array[i - 1] += 1
        for elem in num_array:
            if (elem > 1):
                flag_num = True

        color_array = [i[0] for i in my_array]

        if not flag_num:  # Checks if only color tip can be given.
            if (color_array.count("w") > 1):
                order_list = [i + 1 for i in range(len(color_array)) if color_array[i] == "w"]
                print("The tip given by computer is: ", end="")
                for elem in order_list:
                    print(str(elem) + " ", end="")
                print("w")

                for elem in order_list:
                    play_hand[elem - 1][0] = "w"

            elif (color_array.count("b") > 1):
                order_list = [i + 1 for i in range(len(color_array)) if color_array[i] == "b"]
                print("The tip given by computer is: ", end="")
                for elem in order_list:
                    print(str(elem) + " ", end="")
                print("b")
                for elem in order_list:
                    play_hand[elem - 1][0] = "b"

        else:  # Two tips can be given.
            random_number = random.randint(1, 2)

            if (random_number == 1):  # Number tip
                place_array = [i[1] for i in my_array]
                tip_num = -10
                for i in range(len(num_array)):
                    if (num_array[i] > 1):
                        tip_num = i + 1
                num_order_list = [i + 1 for i in range(len(place_array)) if place_array[i] == tip_num]
                print("The tip given by computer is: ", end="")
                for elem in num_order_list:
                    print(str(elem) + " ", end="")
                print(tip_num)
                for elem in num_order_list:
                    play_hand[elem - 1][1] = tip_num


            else:  # Color tip
                if (color_array.count("w") > 1):
                    order_list = [i + 1 for i in range(len(color_array)) if color_array[i] == "w"]
                    print("The tip given by computer is: ", end="")
                    for elem in order_list:
                        print(str(elem) + " ", end="")
                    print("w")
                    for elem in order_list:
                        play_hand[elem - 1][0] = "w"

                elif (color_array.count("b") > 1):
                    order_list = [i + 1 for i in range(len(color_array)) if color_array[i] == "b"]
                    print("The tip given by computer is: ", end="")
                    for elem in order_list:
                        print(str(elem) + " ", end="")
                    print("b")
                    for elem in order_list:
                        play_hand[elem - 1][0] = "b"


    def pick_stack(self):
        for card in self.hand:
            if (card != ['!',-1]):  # the situation where the color and number of the card is known
                if (len(self.stack[0]) == 0 and card == ["b",1]):  # when the stack is empty
                    return self.hand.index(card)
                if (len(self.stack[1]) == 0 and card == ["w",1]):  # when the stack is empty
                    return self.hand.index(card)
                if (len(self.stack[0]) != 0):
                    if (card[1] == self.stack[0][-1][1]+1):  # suitable to stack for the last card in the stack
                        return self.hand.index(card)
                if (len(self.stack[1]) != 0):
                    if(card[1] == self.stack[1][-1][1]+1):  # suitable to stack for the last card in the stack
                        return self.hand.index(card)

        return -1


    def pick_discard(self):
        for card in self.hand:
            if (card in self.stack[1] or card in self.stack[0]):  # if the card is already in the stack
                return self.hand.index(card)
        for card in self.hand:
            if (card[0] == '!' and card[1] == -1):  # if there is no right to tip, discard the card that has no information about it
                return self.hand.index(card)
            if (card[0] == '!'):  # Discard if we don't know the color
                return self.hand.index(card)
            if (card[1] == -1):  # Discard if we don't know the number
                return self.hand.index(card)



def shuffle(deck):
    for i in range(len(deck)-1, 0, -1):  # Navigating the list named deck
        j = random.randint(0, 15)  # Random selection 0 to 16
        deck[i], deck[j] = deck[j], deck[i]


def print_menu():
    print("Hit 'v' to view the status of the game.")
    print("Hit 't' to spend a tip.")
    print("Hit 's' to try and stack your card.")
    print("Hit 'd' to discard your card and earn a tip.")
    print("Hit 'h' to view this menu.")
    print("Hit 'q' to quit.")


def update_hand(hand, deck, num):
    hand.pop(num)  # Remove the played card from hand.

    # If there are any cards left in the deck,
    if (len(deck) > 0):
        hand.append(deck[0])  # Add the top card to hand
        deck.pop(0)
    return num


def try_stack(card, stack, trash, lives):
    if (card[0] == 'b'):
        if(len(stack[0]) == 0):
            if(card[1] == 1):
                stack[0].append(card)  # append to the black part
                print("\nBlack:", stack[0], "\nWhite:", stack[1], "\n")
            else:
                print("Wrong Card")
                lives -= 1
                trash.append(card)
                trash.sort(key=lambda x: x[1])
                print(trash)
        else:
            if(card[1] == stack[0][-1][-1] +1):
                stack[0].append(card)  # append to the black part
                print("\nBlack:", stack[0], "\nWhite:", stack[1], "\n")
            else:
                print("Wrong Card")
                lives -= 1
                trash.append(card)
                trash.sort(key=lambda x: x[1])
                print(trash)
    if (card[0] == 'w'):
        if (len(stack[1]) == 0):
            if (card[1] == 1):
                stack[1].append(card)  # append to the white part
                print("\nBlack:", stack[0], "\nWhite:", stack[1], "\n")
            else:
                print("Wrong Card")
                lives -= 1
                trash.append(card)
                trash.sort(key=lambda x: x[1])
                print(trash)
        else:
            if (card[1] == stack[1][-1][-1] + 1):
                stack[1].append(card)  # append to the white part
                print("\nBlack:", stack[0], "\nWhite:", stack[1], "\n")
            else:
                print("Wrong Card")
                lives -= 1
                trash.append(card)
                trash.sort(key=lambda x: x[1])
                print(trash)
    return lives


def discard(card,trash,tips):
    trash.append(card)  # Add the card to trash.
    tips += 1  # Increment of number of tips.
    trash.sort(key=lambda x: x[1])
    print("Trash: ", trash)
    print("Number of tips: ", tips)

    return tips

print("Welcome! Let's play!")
print_menu()
deck = [['b', 1], ['b', 1], ['b', 1], ['b', 2], ['b', 2], ['b', 3], ['b', 3], ['b', 4],
        ['w', 1], ['w', 1], ['w', 1], ['w', 2], ['w', 2], ['w', 3], ['w', 3], ['w', 4]]
stack = [[], []]  # 0  means black, 1 means white
trash = []
lives = 2
tips = 3
shuffle(deck)
# First hands are dealt.
comp_hand = [deck[0], deck[1], deck[2]]
play_hand = [deck[3], deck[4], deck[5]]
del deck[0:6]
bot = Gamebot(play_hand, stack)  # Gamebot object is created.
turn = 0                        # 0 means player, 1 means computer. So for each game, the player starts.
while True:
    if turn == 0:
        inp = input("Your turn:")
        if (inp == 'v'):
            print("Computer's hand:", comp_hand)
            print("Number of tips left:", tips)
            print("Number of lives left:", lives)
            print("Current stack:")
            print("Black:", stack[0])
            print("White:", stack[1])
            print("Current trash:", trash)
        elif inp == "t":
            if tips > 0:
                turn = 1        # Switch turns.
                giving_tip = input("Give a tip: ")
                bot.get_tip(giving_tip)
                tips -= 1
            else:
                print("Not possible! No tips left!")
        elif inp == "s":
            turn = 1
            stack_card = input("Which card would you like to use? ")
            lives = try_stack(play_hand[int(stack_card)-1], stack, trash, lives)
            update_hand(play_hand, deck, int(stack_card)-1)

        elif inp == "d":
            turn = 1
            discard_card = input("Which card would you like to use? ")
            if (discard_card == '1' or discard_card == '2' or discard_card == '3'):  # if player enters 1, 2, or 3
                tips = discard(play_hand[int(discard_card)-1], trash, tips)
                update_hand(play_hand, deck, int(discard_card)-1)
            else:
                print("Invalid Option")

        elif inp == "h":
            print_menu()
        elif inp == "q":
            break
        else:
            print("Please enter a valid choice (v,t,s,d,h,q)!")

    else:
        if (tips >= 1 and len(play_hand) > 0):
            bot.give_tip()
            tips -= 1
            print("Remaining tip:", tips)
        else:
            bot_stack = bot.pick_stack()
            bot_discard = bot.pick_discard()
            if (bot_stack != -1):
                try_stack(comp_hand[bot_stack], stack, trash, lives)
                bot.update_hand(bot_stack)
                update_hand(comp_hand, deck, bot_stack)
            else:
                tips = discard(comp_hand[bot_discard], trash, tips)
                bot.update_hand(bot_discard)
                update_hand(comp_hand, deck, bot_discard)


        turn = 0  # Switch turns
    score = sum([len(d) for d in stack])
    if lives == 0:
        print("No lives left! Game over!")
        print("Your score is", score)
        break
    if len(comp_hand+play_hand) == 0:
        print("No cards left! Game over!")
        print("Your score is", score)
        break
    if score == 8:
        print("Congratulations! You have reached the maximum score!")
        break
