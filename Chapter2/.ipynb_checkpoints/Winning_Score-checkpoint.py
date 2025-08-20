def Winning_team():
    # Apples scores
    apples_3 = int(input())  # number of 3-point shots
    apples_2 = int(input())  # number of 2-point field goals
    apples_1 = int(input())  # number of 1-point free throws

    # Bananas scores
    bananas_3 = int(input())
    bananas_2 = int(input())
    bananas_1 = int(input())

    apple_score = apples_3 * 3 + apples_2 * 2 + apples_1 * 1
    banana_score = bananas_3 * 3 + bananas_2 * 2 + bananas_1 * 1

    if apple_score > banana_score:
        print("A")
    elif banana_score > apple_score:
        print("B")
    else:
        print("T")


Winning_team()
