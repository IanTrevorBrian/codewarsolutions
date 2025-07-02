#1.Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

def create_phone_number(n):
    phone_number=f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"
#This part takes the first three integers from the numbers list (numbers[0], numbers[1], numbers[2]), and puts them together inside parentheses.
#For example, if numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], it will evaluate to "123", so this part becomes "(123)".c;
    return phone_number
    
n=[1,2,3,4,5,6,7,8,9,0]
phone_number = create_phone_number(n)
print(phone_number)