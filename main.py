PROTEIN_PER_LB = 0
MIN_FAT_PER_LB = 0
FAT_PERCENTAGE = 0


def update_constants():
    """
    Refreshes global variables by reading constant.txt
    and setting variables equal to read values.
    """
    global PROTEIN_PER_LB
    global MIN_FAT_PER_LB
    global FAT_PERCENTAGE
    with open('constant.txt', 'r') as const_file:
        const_list = const_file.readlines()
    PROTEIN_PER_LB = float(const_list[1])
    MIN_FAT_PER_LB = float(const_list[3])
    FAT_PERCENTAGE = float(const_list[5])
    const_file.close()


def write_constants(protein_per_lb=False, min_fat_per_lb=False, fat_percentage=False):
    """
    Changes values constant.txt to new values given by parameters,
    then calls update_constants() to refresh global variables.
    If a field is empty it ignores that value and does not update it.
        >>> PROTEIN_PER_LB = 0.9
        >>> write_constants(0.3)
        >>> PROTEIN_PER_LB
        0.3
    """
    with open('constant.txt', 'r') as const_file:
        new_data = const_file.readlines()
    if protein_per_lb:
        new_data[1] = str(protein_per_lb) + '\n'
    if min_fat_per_lb:
        new_data[3] = str(min_fat_per_lb) + '\n'
    if fat_percentage:
        new_data[5] = str(fat_percentage) + '\n'
    with open('constant.txt', 'w') as const_file:
        const_file.writelines(new_data)
    update_constants()


def protein_carbs_fats(cal, lbs):
    """
    Given calories and lbs, using global values returns list of macro grams, 
    in order from protein, carbs, and fats.
        >>> PROTEIN_PER_LB = 0.9
        >>> MIN_FAT_PER_LB = 0.45
        >>> FAT_PERCENTAGE = 0.30
        >>> protein_carbs_fats(2500, 150)
        {'protein': 135.0, 'carbohydrates': 302.5, 'fats': 83.33333333333333}
    """
    protein = lbs * PROTEIN_PER_LB
    min_fats = lbs * MIN_FAT_PER_LB
    if (protein * 4) + (min_fats * 9) > cal:
        print("Not enough calories allocated for minimum protein and fats")
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
    try_input = input(message)
    while True:
        try:
            x = float(try_input)
            return x
        except ValueError:
            try_input = input("Not a valid input, try again: ")


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
            print('\n' + macro_message)
    elif user_input == "2":
        while True:
            print("\n1. Grams of protein per pound" + ' (Current: ' + str(PROTEIN_PER_LB) + ')')
            print("2. Minimum grams fat per pound" + ' (Current: ' + str(MIN_FAT_PER_LB) + ')')
            print("3. Desired fat as percentage of calories" + ' (Current: ' + str(FAT_PERCENTAGE) + ')')
            print("4. Return to Main Menu")
            user_input = input('Please choose an option: ')
            if user_input == '1':
                value = main_float_input('Please enter desired grams of protein per lb (recommended: 0.9): ')
                write_constants(value)
            elif user_input == '2':
                value = main_float_input('Please enter minimum grams of fat per lb (recommended: 0.45): ')
                write_constants(False, value)
            elif user_input == '3':
                value = main_float_input('Please enter desired percentage of calories from fat (recommended: 0.3): ')
                write_constants(False, False, value)
            elif user_input == '4':
                print()
                break
            else:
                print('Invalid Selection, please try again')
    elif user_input == "3":
        break
    else:
        print("Invalid Selection, please try again")
