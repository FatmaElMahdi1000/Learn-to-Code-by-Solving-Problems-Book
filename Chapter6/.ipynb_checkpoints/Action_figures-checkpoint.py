from sys import exit

def final_arrang(sorted_Boxes, unsorted_Boxes):
    Arranged = []
    Not_Arranged = []

    # Step 1: If any unsorted box exists, automatically impossible
    if unsorted_Boxes:
        return "NO"

    # Step 2: Sort boxes by their first (smallest) value
    sorted_Boxes.sort(key=lambda x: x[0])

    # Step 3: Check if each box can follow the previous one
    i = 0
    while i < len(sorted_Boxes) - 1:
        curr_box = sorted_Boxes[i]
        next_box = sorted_Boxes[i + 1]

        curr_max = max(curr_box)
        next_min = min(next_box)

        if curr_max <= next_min:
            Arranged.append(curr_box)
        else:
            Not_Arranged.append(next_box)

        i += 1

    # Add the last box if it’s not yet included
    if sorted_Boxes[-1] not in Arranged and sorted_Boxes[-1] not in Not_Arranged:
        Arranged.append(sorted_Boxes[-1])

    # Step 4: Decide if arrangement is possible
    if Not_Arranged:
        return "NO"
    else:
        return "YES"

                
def Box_arrang(Boxes):
    Sorted = []
    Unsorted = []
    
    for Box in Boxes:
        if Box == sorted(Box):
            Sorted.append(Box)
        else:
            Unsorted.append(Box)
    return Sorted, Unsorted
    

def fig(n): #fig_num and height

    Boxes_List = []
    for box in range(0,n): #range(0, n)
        k = input() #number of figures in a box
        for k_input in k:
            box_attributes = list(map(int, (k.split())))
            fig_num = box_attributes[0]
            fig_heights = box_attributes[1:] #list of heights
            if not (fig_num == len(fig_heights)):
                exit(1) #something is wrong
        Boxes_List.append(fig_heights)
    return Boxes_List

n = int(input()) #number of boxes
if not (1 <= n <100):
    exit(1) #**return 1** (or any non-zero value) → means “an error occurred” or “something went wrong.”
Boxes = fig(n)
sorted_Boxes = Box_arrang(Boxes)[0]
unsorted_Boxes = Box_arrang(Boxes)[1]

print(Box_arrang(Boxes))
print(final_arrang(sorted_Boxes, unsorted_Boxes))