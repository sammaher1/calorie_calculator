# Constant Macro Calculator

This program is a tool for those tracking their macronutrients(macros) and calories, and would like a more accurate way to track them. The calculator is built using constants rather than percentages. Unlike most macro/calorie calculators, which calculate protein, fats, and carbs using a percentage of total calories, this calculator calculates using constant grams of macronutrient per lb of bodyweight. This is useful for people like weightlifters who change calorie requirements depending on the season. 

With a normal percentage based macro calculator, a user may require 25% of daily calories from protein. If they are gaining weight they could have a caloric requirement of 2500, requiring 156.25 grams of protein. However once they switch to losing weight, they may only require 1800 calories. 25% of this would be only 112.5 grams of protein. If a user wanted to keep their protein constant(as many weightlifters do), they would need to constantly manually adjust their percentages every time their caloric requirements changed.

Not so with this calculator. You set your desired protein per lb of bodyweight, minimum required fats(for health reasons), and your desired percentage of calories from fats. Then when you want to calculate your macros you give the calculator your caloric requirement and current weight. This will keep important macros like protein and fat constant while varying carbohydrates depending on your user-set constants and daily calories and weight.

## Getting Started

To get started simply download the project and a version of Python >= 3.6. Keep constant.txt and main.py in the same folder.
The constant.txt file is used to keep track of your preferred constants between runs of the program. You can edit it manually or through main.py.

## Examples

Calculating Macros (with default constants)
```
1. Calculate Macros
2. Edit Constants
3. Exit
Please choose an option: 1
Please enter your daily calories: 2500
Please enter your weight: 140

Total daily calories: 2500.0
Total daily protein: 126.0
Total daily carbs: 311.5
Total daily fats: 83.33333333333333

1. Calculate Macros
2. Edit Constants
3. Exit
Please choose an option: 
```

Editing Constants
```
1. Calculate Macros
2. Edit Constants
3. Exit
Please choose an option: 2

1. Grams of protein per pound (Current: 0.9)
2. Minimum grams fat per pound (Current: 0.45)
3. Desired fat as percentage of calories (Current: 0.3)
4. Return to Main Menu
Please choose an option: 1
Please enter desired grams of protein per lb (recommended: 0.9): 0.45

1. Grams of protein per pound (Current: 0.45)
2. Minimum grams fat per pound (Current: 0.45)
3. Desired fat as percentage of calories (Current: 0.3)
4. Return to Main Menu
```

## Built With

* [Python 3.6](https://www.python.org/downloads/release/python-360/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
