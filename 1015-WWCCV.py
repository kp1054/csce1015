# Credit Card Validator version .1
# This is the world's worst credit card number validator. It checks to see if the number is 16 digits long and that is it.  

# anything that starts with a pound sign (hashtag if you are under 30) is a comment. The computer ignores these.

# Let's tell the world whose awful credit card validator this is.
# print ("Joe Dirt Modified This Credit Card Validator")

# # Let's get the card number from the user
# card_number = input("Enter your 16-digit credit card number: ")

# # Check if card number is 16 digits long

# # len means 'length', and the '==' is testing one thing against the other. A single equal sign would set one thing equal to the other (not what we want to do). 
# # card_number.isdigit() is checking if this is numbers instead of someone typing 'cheeseburger' for their credit card number.

# if len(card_number) == 15 and card_number.isdigit():     
#     print ("Card is valid.")
# else:
#     print ("Invalid card number. It must be 16 digits long.") 

# def run_tests():
#     try:

#         assert is_credit_card_valid("4111111111111111"), '4111111111111111 should pass but did not'

#         assert is_credit_card_valid("5105105105105100"), '5105105105105100 should pass but did not'

#         assert not is_credit_card_valid("134"), '134 should not pass but did'

#         assert not is_credit_card_valid("1234567890123456"), '1234567890123456 should not pass but did'

#         assert not is_credit_card_valid("000000000000"), 'This is a bad test and we will get an error message'
#         print("All tests passed successfully!")
#     except AssertionError as e:
#         printf(f"Test failed: {e}")
# run_tests() 
# let's go get some software that someone else wrote
import luhn  

# a function that uses the 'luhn' code - it takes a 'card_number' and returns 'true' or 'false' if the card is valid.
def is_credit_card_valid(card_number):    
    return luhn.verify(card_number)

# Let's tell the world whose awful credit card validator this is.
print(" Krushi Credit Card Validator")

# Let's get the card number from the user
card_number = input("Enter your 16-digit credit card number: ")

# Validate the credit card number using the Luhn algorithm
if is_credit_card_valid(card_number):  # we are calling the function above and sending it the card_number to validate
    print("The credit card number is valid.")
else:
    print("The credit card number is invalid.")



def is_credit_card_valid(card_number):
    # Reverse the card number and convert each digit to an integer
    digits = [int(digit) for digit in reversed(card_number)]
    
    # Double every second digit from the right
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        # If doubling results in a number greater than 9, subtract 9
        if digits[i] > 9:
            digits[i] -= 9
    
    # Sum all the digits
    total_sum = sum(digits)
    
    # The card number is valid if the total sum is a multiple of 10
    return total_sum % 10 == 0

def run_tests():
    try:
        assert is_credit_card_valid("4111111111111111"), '4111111111111111 should pass but did not'
        assert is_credit_card_valid("5105105105105100"), '5105105105105100 should pass but did not'
        assert not is_credit_card_valid("134"), '134 should not pass but did'
        assert not is_credit_card_valid("1234567890123456"), '1234567890123456 should not pass but did'
        assert not is_credit_card_valid("0000000000000000"), '0000000000000000 should not pass but did'
        print("All tests passed successfully!")
    except AssertionError as e:
        print(f"Test failed: {e}")