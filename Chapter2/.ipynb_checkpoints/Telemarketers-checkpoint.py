digit_1 = int(input())
digit_2 = int(input())
digit_3 = int(input())
digit_4 = int(input())

# validate input
if not (0 <= digit_1 <= 9 and 0 <= digit_2 <= 9 and 0 <= digit_3 <= 9 and 0 <= digit_4 <= 9):
    print("Invalid inputs")
else:
    if (digit_1 in [8, 9]) and (digit_4 in [8, 9]) and (digit_2 == digit_3):
        print("ignore")
    else:
        print("answer")
