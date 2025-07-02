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

#2.Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

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

#2(b).To improve your code so that it accepts user input and stores it in the array

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

#3.You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

import random
#generate an array with random integers with a length of atleast 3
array = [random.choice([random.randint(0, 10) * 2, random.randint(0, 10) * 2 + 1]) for i in range(random.randint(3, 20))]
print(f"array: {array}")
    
def find_outlier(integers):
    #determine the number of odd and even numbers in the array
    even_count = 0
    odd_count = 0
    for num in integers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count +=1
    print(f"even number count is {even_count} and odd number count is {odd_count}")
    
    #find the outlier
    if even_count > odd_count:
        for num in integers:
            if num % 2 != 0:
                return num #returns odd number if even number is the majority
    else:
        for num in integers:
            if num % 2 == 0:
                return num #returns even number if odd number is the majority
            
outlier = find_outlier(array)
print(f"the outlier is {outlier}")

#4.given a string of words, return the shortest word and its length.
#String will never be empty and you do not need to account for different data types.

#find length of shortest word
def find_short(sentence):
    # Your code goes here
    sentence = sentence.split()
    short_word = min(sentence, key=len)
    return short_word, len(short_word)
    
sentence = "Kenyan youth are against tribalism"
short_word, short_word_length = find_short(sentence)
print(f"the shortest word is '{short_word}' and its length is {short_word_length}")

#5.given a string of words, return the  longest word and its length.
#String will never be empty and you do not need to account for different data types.

#find length of longest word
def find_long(sentence):
    # Your code goes here
    sentence = sentence.split()
    long_word = max(sentence, key=len)
    return long_word, len(long_word)
    
sentence = "Kenyan youth are against corruption"
long_word, long_word_length = find_long(sentence)
print(f"the longest word is '{long_word}' and its length is {long_word_length}")

#6.write code to input a string of words, return the shortest word and its length.
#String will never be empty and you do not need to account for different data types.

#find length of shortest word
def find_short(sentence):
    # Your code goes here
    sentence = sentence.split()
    short_word = min(sentence, key=len)
    return short_word, len(short_word)
    
sentence = input("enter your sentence")
short_word, short_word_length = find_short(sentence)
print(f"the shortest word is '{short_word}' and its length is {short_word_length}")

#7.write code to input a string of words, return the longest word and its length.
#String will never be empty and you do not need to account for different data types.

#find length of longest word
def find_long(sentence):
    # Your code goes here
    sentence = sentence.split()
    long_word = max(sentence, key=len)
    return long_word, len(long_word)
    
sentence = input("enter your sentence")
long_word, long_word_length = find_long(sentence)
print(f"the longest word is '{long_word}' and its length is {long_word_length}")

#8.write code to input a string of words, return the shortest word and its length.
#String will never be empty and you do not need to account for different data types.Incooporate input validation handled by try-except block.

#find length of shortest word
def find_short(sentence):
    # Your code goes here
    sentence = sentence.split()
    short_word = min(sentence, key=len)
    return short_word, len(short_word)

def get_input():
    prompt = "Enter your sentence with at least two words: "
    while True:
        user_input = input(prompt).strip()
        try:
            #Reject the input if it's empty OR contains fewer than two words.
            if not user_input or len(user_input.split()) < 2:  #This checks if the input is empty or just whitespace and also If the sentence has fewer than 2 words, it's considered invalid.
                raise ValueError("Please enter a sentence with at least two words!")
            return user_input
        except ValueError as e:
             # Update the prompt for the next loop iteration
             prompt = f"ERROR! {e} Try again: "

#main 
sentence = get_input()
short_word, short_word_length = find_short(sentence)
print(f"the shortest word is '{short_word}' and its length is {short_word_length}")

