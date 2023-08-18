#maintenance calories calculation
print("Welcome to Hassan's Diet Tracker")
while True:
    weight_entry = input("Enter a number for your body weight in pounds: ")
    try:
        weight = int(weight_entry)
        break  # Exit the loop if the input is an integer
    except ValueError:
        try:
            weight = float(weight_entry)
            break  # Exit the loop if the input is a float
        except ValueError:
            print("Error: Invalid input. Please enter a NUMBER value for body weight in pounds.")
            continue  # Continue the loop if the input is not a number
maintenance = float(weight*15)
print("We have calculated your maintenance calories to be:", maintenance)

#users fitness goals
while True:
     print("Please select an option for your fitness goals: ")
     print("1. Lose 0.5 lbs per week (250 calorie deficit)")
     print("2. Maintain current weight")
     print("3. Gain 0.5 lbs per week (250 calorie surplus)")
     goal = input("Please select your fitness goal from the three options above (1-3): ")
     if goal == "1":
          calories = maintenance - 250
          print("You have selected to lose 0.5 lbs per week")
          print("Your target daily caloric intake is:", calories)
     elif goal == "2":
          calories = maintenance
          print("You have selected to maintain your current weight")
          print("Your target daily caloric intake is:", calories)
     elif goal == "3":
          calories = maintenance + 250
          print("You have selected to gain 0.5 lbs per week")
          print("Your target daily caloric intake is:", calories)
     else:
          print("Invalid selection. Please enter a number between 1 and 3 from the menu.")
          continue
     break

#define food database
Food_Library = {
    "apple" : 52,
    "banana" : 89,
    "brown_bread" : 85, #calories per slice
    "white_bread" : 75, #calories per slice
    "egg" : 80,
    "rice" : 170, #calories per cup
    "yogurt" : 160, #calories per cup
    "protein_bar" : 160,
    "almond_milk" : 90, #calories per cup
    "protein_powder" : 130, #calories per scoop(35 grams)
    "chicken_drumstick": 160, #calories per 100 grams
    "potatoes" : 73, #calories per 100 grams
    "pasta" : 131, #calories per cup
}

#calculate total calories for what user ate for BREAKFAST
breakfast_dict = {} #empty dictionary for the breakfast items
breakfast_calories = []  #empty list to store calorie values of various breakfast items
while True:
    breakfast_food = input("Enter your breakfast items name: ")
    if breakfast_food in Food_Library:
        breakfast_foodcalories = Food_Library[breakfast_food]
        print("Calories for", breakfast_food, "were found in our database, with", Food_Library[breakfast_food], "calories")
    else:
        print("That item was not found in our database.")
        breakfast_foodcalories = float(input("Enter the items calorie count: "))
    breakfast_dict[breakfast_food] = breakfast_foodcalories
    breakfast_calories.append(breakfast_foodcalories)
    print("You have successfully added", breakfast_food, "with", breakfast_foodcalories, "calories to your breakfast entries.")

    while True:
        print("Do you want to add another item to your breakfast entries? (y/n)")
        another_item = input("Enter your selection: ")
        if another_item == "y":
            break
        if another_item == "n":
            break
        else:
            print("Invalid selection. Please select 'y' for yes or 'n' for no.")
    if another_item == "n":
        break
breakfast_total = sum(breakfast_calories)
print("Your breakfast had", breakfast_total, "calories")

#calculate total calories for what user ate for LUNCH
lunch_dict = {} #empty dictionary for the lunch items
lunch_calories = []  #empty list to store calorie values of various lunch items
while True:
    lunch_food = input("Enter your lunch items name: ")
    if lunch_food in Food_Library:
        lunch_foodcalories = Food_Library[lunch_food]
        print("Calories for", lunch_food, "were found in our database, with", Food_Library[lunch_food], "calories")
    else:
        print("That item was not found in our database.")
        lunch_foodcalories = float(input("Enter the items calorie count: "))
    lunch_dict[lunch_food] = lunch_foodcalories
    lunch_calories.append(lunch_foodcalories)
    print("You have successfully added", lunch_food, "with", lunch_foodcalories, "calories to your lunch entries.")

    while True:
        print("Do you want to add another item to your lunch entries? (y/n)")
        another_item = input("Enter your selection: ")
        if another_item == "y":
            break
        if another_item == "n":
            break
        else:
            print("Invalid selection. Please select 'y' for yes or 'n' for no.")
    if another_item == "n":
        break
lunch_total = sum(lunch_calories)
print("Your lunch had", lunch_total, "calories")

#calculate total calories for what user ate for DINNER
dinner_dict = {} #empty dictionary for the dinner items
dinner_calories = []  #empty list to store calorie values of various dinner items
while True:
    dinner_food = input("Enter your dinner items name: ")
    if dinner_food in Food_Library:
        dinner_foodcalories = Food_Library[dinner_food]
        print("Calories for", dinner_food, "were found in our database, with", Food_Library[dinner_food], "calories")
    else:
        print("That item was not found in our database.")
        dinner_foodcalories = float(input("Enter the items calorie count: "))
    dinner_dict[dinner_food] = dinner_foodcalories
    dinner_calories.append(dinner_foodcalories)
    print("You have successfully added", dinner_food, "with", dinner_foodcalories, "calories to your dinner entries.")

    while True:
        print("Do you want to add another item to your dinner entries? (y/n)")
        another_item = input("Enter your selection: ")
        if another_item == "y":
            break
        if another_item == "n":
            break
        else:
            print("Invalid selection. Please select 'y' for yes or 'n' for no.")
    if another_item == "n":
        break
dinner_total = sum(dinner_calories)
print("Your dinner had", dinner_total, "calories")

#ask user if they want to enter a calories burnt from exercise value
exercise = float(input("Enter how many calories you burnt through exercise (if applicable): "))


#define class and function to find differential of calories and print results for caloric intake
class Diet:
    def __init__(self, breakfast_total, lunch_total, dinner_total, exercise, calories):
        self.breakfast_total = breakfast_total
        self.lunch_total = lunch_total
        self.dinner_total = dinner_total
        self.exercise = exercise
        self.calories = calories
    def calorie_differential(self):
        differential = self.calories + self.exercise - (self.breakfast_total + self.lunch_total + self.dinner_total)
        return differential
    
fitness = Diet(breakfast_total, lunch_total, dinner_total, exercise, calories)
weekly_differential = 7*fitness.calorie_differential()
total = breakfast_total + lunch_total + dinner_total
print("You ate a total of", total, "calories today, and burned a total of", exercise, "calories through exercise.")
if fitness.calorie_differential() > 0:
    print("This means you ate", round((calories-total)), "calories below your daily target!")
elif fitness.calorie_differential() == 0:
    print("This means you hit your daily target of", calories, "on the dot!")   
elif fitness.calorie_differential() < 0:
    print("This means you ate", round((total-calories)), "calories above your daily target!")

if weekly_differential > 0:
    print("If you eat like today everyday, you will lose", round(weekly_differential/3500, 2), "lb per week")
elif weekly_differential == 0:
    print("If you eat like today everyday, you will maintain your weight")
elif weekly_differential < 0:
    print("If you eat like today everyday, you will gain", round((-1*(weekly_differential/3500)), 2), "lb per week")