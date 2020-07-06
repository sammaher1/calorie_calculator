PROTEIN_PER_LB = 0
MIN_FAT_PER_LB = 0
FAT_PERCENTAGE = 0


def update_constants():
    """
    Updates global variables by reading constant.txt
    and setting variables equal to read values.
    """
    global PROTEIN_PER_LB
    global MIN_FAT_PER_LB
    global FAT_PERCENTAGE
    const_file = open("constant.txt", 'r')
    const_list = const_file.readlines()
    PROTEIN_PER_LB = float(const_list[1])
    MIN_FAT_PER_LB = float(const_list[3])
    FAT_PERCENTAGE = float(const_list[5])
    const_file.close()


def test_if_num(x):
    """
    Validates user input by checking if parameter x is a int, float, or
    a other data type that can be directly converted to a float.
        >>> test_if_num(5)
        True
        >>> test_if_num("Five")
        False
    """
    try:
        x = float(x)
        return True
    except ValueError:
        return False


def protein_carbs_fats(cal, lbs, protein_per_lb, min_fat_per_lb, fat_percentage):
    """
    Given calories, lbs, protein_per_lb, min_fat_per_lb, and desired fat_percentage,
    returns list of macro grams, in order from protein, carbs, and fats.
        >>> protein_carbs_fats(2500, 150)
        [135.0, 302.5, 83.33333333333333]
    """
    protein = lbs * protein_per_lb
    min_fats = lbs * min_fat_per_lb
    if (protein * 4) + (min_fats * 9) > cal:
        print("Not enough calories for minimum protein and fats")
        return -1
    else:
        if min_fats * 9 > (fat_percentage * cal):
            fats = min_fats
            cal -= protein * 4
            cal -= fats * 9
            carbs = cal/4
        else:
            fats = (cal * fat_percentage)/9
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

        p_c_f_list = protein_carbs_fats(calories, weight, PROTEIN_PER_LB, MIN_FAT_PER_LB, FAT_PERCENTAGE)
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