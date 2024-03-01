def blckjck():
    ch = input("Do you want to play a game of blackjack? Type 'y' or 'n'")
    if ch == "y":
        from art import logo
        import random
        print(logo)
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        user_cards = [random.choice(cards)]
        comp_cards = [random.choice(cards)]
        cont = "y"
        while cont == "y":
            def card_selection():
                user_cards.append(random.choice(cards))
                score = 0
                for i in user_cards:
                    score += i
                print(f"Your cards: {user_cards}, current score: {score}")
                comp_cards.append(random.choice(cards))
                print(f"Computer's first card: {comp_cards[1]}")
                if score > 21:
                    if 11 in user_cards:
                        position = user_cards.index(11)
                        user_cards[position] = 1
                    else:
                        print("You went over. You lose")
                        blckjck()
                elif score == 21 and len(user_cards) == 2:
                    score = 0
                    print(f"You hit the blackjack. Score is: {score}")

                else:
                    another = input("Type 'y' to get another card, type 'n' to pass")
                    if another == "n":
                        print(f"Your final hand: {user_cards},final score:{score}")
                        comp_score = 0
                        for i in comp_cards:
                            comp_score += i
                        while comp_score < 17:
                            comp_cards.append(random.choice(cards))
                            comp_score += comp_cards[-1]
                        print(f"Computer's final hand: {comp_cards},final score: {comp_score}")
                        if comp_score > 21:
                            print("Opponent went over. You win")
                        elif comp_score > score:
                            print("You lose")
                        elif comp_score < score:
                            print("You win")
                        else:
                            print("Draw")
                        blckjck()
            card_selection()
    else:
        exit()
blckjck()