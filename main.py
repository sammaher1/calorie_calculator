PROTEIN_PER_LB = 0
FAT_PER_LB = 0
FAT_PERCENTAGE = 0


def update_constants():
    global PROTEIN_PER_LB
    global FAT_PER_LB
    global FAT_PERCENTAGE
    const_file = open("constant.txt", 'r')
    const_list = const_file.readlines()
    PROTEIN_PER_LB = float(const_list[1])
    FAT_PER_LB = float(const_list[3])
    FAT_PERCENTAGE = float(const_list[5])
    const_file.close()

def test_if_num(x):
    try:
        x = float(x)
        return True
    except ValueError:
        return False


def protein_carbs_fats(cal, lbs):
    protein = lbs * PROTEIN_PER_LB
    min_fats = lbs * FAT_PER_LB
    if (protein * 4) + (min_fats * 9) > cal:
        print("Not enough calories for minimum protein and fats")
        return -1
    else:
        if min_fats * 9 > (FAT_PERCENTAGE * cal):
            fats = min_fats
            cal -= protein * 4
            cal -= fats * 9
            carbs = cal/4
        else:
            fats = (cal * FAT_PERCENTAGE)/9
            cal -= protein * 4
            cal -= fats * 9
            carbs = cal/4
    pcf = [protein, carbs, fats]
    return pcf


while True:
    update_constants()
    print("1. Calculate Macros")
    print("2. Edit Constants")
    print("3. Exit")
    user_input = input("Please choose an option: ")
    if user_input == "1":
        user_input = input("Please enter your daily calories: ")
        while True:
            if test_if_num(user_input):
                calories = float(user_input)
                break
            else:
                user_input = input("Not a valid input, try again: ")

        user_input = input("Please enter your weight: ")
        while True:
            if test_if_num(user_input):
                weight = float(user_input)
                break
            else:
                user_input = input("Not a valid input, try again: ")

        p_c_f_list = protein_carbs_fats(calories, weight)
        if p_c_f_list != -1:
            macro_message = f"Total daily calories: {calories}\n"   \
                            f"Total daily protein: {p_c_f_list[0]}\n"   \
                            f"Total daily carbs: {p_c_f_list[1]}\n" \
                            f"Total daily fats: {p_c_f_list[2]}\n"
            print(macro_message)
    elif user_input == "2":
        break
    elif user_input == "3":
        break
    else:
        print("Invalid Selection, please try again")