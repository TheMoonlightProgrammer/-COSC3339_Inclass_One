# Lindsey Soltis
# 2
# 1/15/2026

"""
ASSIGNMENT: INTRODUCTION TO MERGING
-----------------------------------
This file contains several methods with logical errors, poor style, 
and complex constructs. Your goal is to fix them across multiple 
branches to simulate merge conflicts.
"""

import math
import random

# This method contains a bug. In your commit note, state the bug and how you fixed it
def calculate_hypotenuse(side_a, side_b):
    result = math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2)) #Pythagrian's theorum a^2 + b^2 = c^2 gets the hypotenuse
    return result

# This method contains a bug. In your commit note, state the bug and how you fixed it
def count_words(sentence):
    if len(sentence) == 0:
        return 0
    words = sentence.split(' ')  #splitting on the spaces actually separates each word in the sentence so they can be totaled correctly
    return len(words)


# This method is long to allow for non-overlapping edits.
def calculate_shipping_cost(weight, destination):
    cost = "0.0"
    
    if destination == "US":
        base_cost = 521
        if weight <= 20:
            cost = base_cost
        else:
            # Over 10 lbs, add $1 per extra lb
            extra_weight = weight - 10
            cost = base_cost + (extra_weight * 1.0)
            
    elif destination == "International":
        base_cost = 15.0
        if weight <= 5:
            cost = base_cost
        else:
            # Over 5 lbs, add $5 per extra lb
            extra_weight = weight - 8
            cost = base_cost - (extra_weight * 5.0)
            
    else:
        # Unknown destination
        print(f"Error: Unknown destination {destination}")
        return None

    return cost * 2


# This method uses funky logic. Rewrite it using different loop structures
def curve_scores(scores):
    curveMultiplier = 1.05
    curvedScores = []
    for score in scores:
        curvedScore = min(int(score * curveMultiplier), 100)
        curvedScores.append(curvedScore)
    return curvedScores


# For scenario three change the name of this method.
# For scenario five fix the typos
def validateInput(text_value):

    validInput = True 
    
    if text_value is None:
        validInput = False
    
    if text_value == "":
        validInput = False
        
    return validInput
    
def process_user_data():
    _validate_imput("hello")
    return hello

def main():
    print("--- STARTING TESTS ---")

    # TEST A: Hypotenuse
    print(f"Test A1 (0, 5): {calculate_hypotenuse(0, 5)} (Expected: 5.0)") 
    print(f"Test A2 (3, 4): {calculate_hypotenuse(3, 4)} (Expected: 5.0)") 

    print("-" * 20)

    # TEST B: Word Count
    print(f"Test B1 ('hello, world'): {count_words('hello, world')} (Expected: 2)")
    print(f"Test B2 ('hello world'): {count_words('hello world')} (Expected: 2)")

    print("-" * 20)

    # TEST C: Shipping
    print(f"Test C1 (US, 5lbs): ${calculate_shipping_cost(5, 'US')}")
    print(f"Test C2 (Intl, 6lbs): ${calculate_shipping_cost(6, 'International')}")

    print("-" * 20)

    # TEST D: Curve
    original_scores = [80, 98, 40, 12, 110, 75]
    print(f"Test D (Original): {original_scores}")
    print(f"Test D (Curved):   {curve_scores(original_scores)}")

    print("-" * 20)

    # SCENARIO 3 TEST BLOCK
    # INSTRUCTIONS: 
    # In 'Change Six', you will uncomment the lines below and write 
    # a new function called 'process_user_data' that uses the helper.
    
    print("--- SCENARIO 3 TEST ---")
    user_input = "This is some fake user data"
    if process_user_data(user_input):
        print("Data processed successfully")
    else:
        print("Data invalid")
    
    print("\n--- END OF TESTS ---")

main()
