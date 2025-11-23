# Task 1: Welcome message
print("Welcome to the Savings Goal Tracker!")

# Task 2: Ask the user for input
# Collect:
# - their name (optional)
# - their total savings goal
# - how much they have saved so far
# - how much they plan to save each week

name = input("What is your name? (Press Enter to skip) ")

goal_input = input("What is your total savings goal in dollars? ")
current_input = input("How much have you saved so far in dollars? ")
weekly_input = input("How much do you plan to save each week in dollars? ")

# Task 3: Convert Input & Perform calculations

# How much is left to reach the goal
remaining_amount = savings_goal - current_savings

# If the user already met or passed their goal:
if remaining_amount <= 0:
    # Task 4 pt1: Display a clear result
    if name.strip():
        print(f"\nGreat job, {name}! You have already reached your savings goal!")
    else:
        print("\nGreat job! You have already reached your savings goal!")
    exit()

# Calculate weeks needed and percent toward goal
weeks_needed = remaining_amount / weekly_contribution
percent_complete = (current_savings / savings_goal) * 100
