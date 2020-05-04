import constant


def test_if_num(x):
    try:
        x = float(x)
        return True
    except ValueError:
        return False


def protein_carbs_fats(cal, lbs):
    protein = lbs * constant.PROTEIN_PER_LB
    min_fats = lbs * constant.FAT_PER_LB
    if (protein * 4) + (min_fats * 9) > cal:
        print("Not enough calories for minimum protein and fats")
        return -1
    else:
        if min_fats * 9 > (constant.FAT_PERCENTAGE * cal):
            fats = min_fats
            cal -= protein * 4
            cal -= fats * 9
            carbs = cal/4
        else:
            fats = (cal * constant.FAT_PERCENTAGE)/9
            cal -= protein * 4
            cal -= fats * 9
            carbs = cal/4
    pcf = [protein, carbs, fats]
    return pcf


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
    final_message = f"Total daily calories: {calories}\n"   \
                    f"Total daily protein: {p_c_f_list[0]}\n"   \
                    f"Total daily carbs: {p_c_f_list[1]}\n" \
                    f"Total daily fats: {p_c_f_list[2]}\n"
    print(final_message)
input("Press enter to close")