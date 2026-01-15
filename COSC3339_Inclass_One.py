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
def calculate_hypotenuse(SIDE_A, SIDE_B):
    RESULT = math.sqrt(math.pow(SIDE_A, 2) + math.pow(SIDE_B, 2)) # Pythagrian's theorum a^2 + b^2 = c^2 gets the hypotenuse
    return RESULT

# This method contains a bug. In your commit note, state the bug and how you fixed it
def count_words(SENTENCE):
    if len(SENTENCE) == 0:
        return 0
    WORDS = SENTENCE.split(' ')  # Splitting on the spaces actually separates each word in the sentence so they can be totaled correctly
    return len(WORDS)


# This method is long to allow for non-overlapping edits.
def calculate_shipping_cost(WEIGHT, DESTINATION):
    COST = "0.0"
    
    if DESTINATION == "US":
        BASE_COST = 521
        if WEIGHT <= 20:
            COST = BASE_COST
        else:
            # Over 10 lbs, add $1 per extra lb
            EXTRA_WEIGHT = WEIGHT - 10
            COST = BASE_COST + (EXTRA_WEIGHT * 1.0)
            
    elif DESTINATION == "International":
        BASE_COST = 15.0
        if WEIGHT <= 5:
            COST = BASE_COST
        else:
            # Over 5 lbs, add $5 per extra lb
            EXTRA_WEIGHT = WEIGHT - 8
            COST = BASE_COST - (EXTRA_WEIGHT * 5.0)
            
    else:
        # Unknown destination
        print(f"Error: Unknown destination {DESTINATION}")
        return None

    return COST * 2


# This method uses funky logic. Rewrite it using different loop structures
def curve_scores(SCORES):
    CURVE_MULTIPLIER = 1.05
    CURVED_SCORES = []
    for SCORE in SCORES:
        CURVED_SCORE = min(int(SCORE * CURVE_MULTIPLIER), 100)
        CURVED_SCORES.append(CURVED_SCORE)
    return CURVED_SCORES


# For scenario three change the name of this method.
# For scenario five fix the typos
def validateInput(TEXT_VALUE):

    validInput = True 
    
    if text_value is None:
        validInput = False
    
    if text_value == "":
        validInput = False
        
    return validInput
    
def process_user_data():
    _VALIDATE_IMPUT("hello")
    return HELLO

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
    ORIGINAL_SCORES = [80, 98, 40, 12, 110, 75]
    print(f"Test D (Original): {ORIGINAL_SCORES}")
    print(f"Test D (Curved):   {curve_scores(ORIGINAL_SCORES)}")

    print("-" * 20)

    # SCENARIO 3 TEST BLOCK
    # INSTRUCTIONS: 
    # In 'Change Six', you will uncomment the lines below and write 
    # a new function called 'process_user_data' that uses the helper.
    
    print("--- SCENARIO 3 TEST ---")
    USER_INPUT = "This is some fake user data"
    if process_user_data(USER_INPUT):
        print("Data processed successfully")
    else:
        print("Data invalid")
    
    print("\n--- END OF TESTS ---")

main()
