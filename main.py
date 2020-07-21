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


def protein_carbs_fats(cal, lbs):
    """
    Given calories and lbs, using global values returns list of macro grams, 
    in order from protein, carbs, and fats.
        >>> protein_carbs_fats(2500, 150)
        [135.0, 302.5, 83.33333333333333]
    """
    protein = lbs * PROTEIN_PER_LB
    min_fats = lbs * MIN_FAT_PER_LB
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
    pcf_dict = {"protein": protein, "carbohydrates": carbs, "fats": fats}
    return pcf_dict

def main_float_input(message):
    """
    Takes message to print when asking for input, the converts to float.
    Repeats user input until it can be converted to float without error.
    Returns that float once done.
    """
    user_input = input(message)
    while True:
        try:
            x = float(user_input)
            return x
        except ValueError:
            user_input = input("Not a valid input, try again: ")


update_constants()
while True:
    print("1. Calculate Macros")
    print("2. Edit Constants")
    print("3. Exit")
    user_input = input("Please choose an option: ")
    if user_input == "1":
        calories = main_float_input("Please enter your daily calories: ")
        weight = main_float_input("Please enter your weight: ")
        p_c_f_dict = protein_carbs_fats(calories, weight)
        if p_c_f_dict != -1:
            macro_message = f"Total daily calories: {calories}\n"   \
                            f"Total daily protein: {p_c_f_dict['protein']}\n"   \
                            f"Total daily carbs: {p_c_f_dict['carbohydrates']}\n" \
                            f"Total daily fats: {p_c_f_dict['fats']}\n"
            print(macro_message)
    elif user_input == "2":
        update_constants()
        break
    elif user_input == "3":
        break
    else:
        print("Invalid Selection, please try again")