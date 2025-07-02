#1.Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

def create_phone_number(n):
    phone_number=f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"
#This part takes the first three integers from the numbers list (numbers[0], numbers[1], numbers[2]), and puts them together inside parentheses.
#For example, if numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], it will evaluate to "123", so this part becomes "(123)".c;
    return phone_number
    
n=[1,2,3,4,5,6,7,8,9,0]
phone_number = create_phone_number(n)
print(phone_number)

#1(b).To improve your code so that it accepts user input and stores it in the array

def create_phone_number(n):
    # Format the phone number using an f-string
    phone_number = f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"
    return phone_number  # Return the formatted phone number

def get_input():
    # Prompt the user to input 10 digits, ensuring that only valid digits are entered
    while True:
        try:
            # Accept input from the user
            user_input = input("Enter 10 digits for the phone number (without spaces or dashes): ")

            # Check if the input contains exactly 10 digits
            if len(user_input) != 10 or not user_input.isdigit():
                raise ValueError("Please enter exactly 10 digits.")

            # Convert the input string to a list of integers
            n = [int(digit) for digit in user_input]

            return n  # Return the list of digits
        except ValueError as e:
            print(e)  # Print the error message and ask for input again

# Get user input
n = get_input()

# Generate the phone number and print it
phone_number = create_phone_number(n)
print(f"The formatted phone number is: {phone_number}")

#3.Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

def spin_words(sentence):
    # Your code goes here
    sentence = sentence.split()
    
    for i in range(len(sentence)):
        if len(sentence[i]) >= 5:
            sentence[i] = sentence[i][::-1]
    return ' '.join(sentence)

sentence = "William Ruto must go"
new_sentence = spin_words(sentence)
print(new_sentence)

#3(b).To improve your code so that it accepts user input and stores it in the array

def spin_words(sentence):
    # Your code goes here
    sentence = sentence.split()
    
    for i in range(len(sentence)):
        if len(sentence[i]) >= 5:
            sentence[i] = sentence[i][::-1]
    return ' '.join(sentence)

sentence = input("enter your sentence: ")
new_sentence = spin_words(sentence)
print("output:", new_sentence)