print("Welcome to the Weekly Calorie Tracker")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
calories = []

total_calories = sum(calories)
print("Total calories:", total_calories)

average = total_calories / 7
print("Average calories:" , average)

print("Highest:", max(calories)
print("Lowest:", min(calories)

with open("calories.txt", "w") as file:
    for c in calories:
        file.write(str(c) + "\n")
