#define a function for reverse digits
def reverse_digits(number):
    #add reverse as 0
    reverse = 0
    #while loop
    while number > 0:
        reverse = reverse * 10 + (number % 10)
        number = number // 10
    #add return to reverse
    return reverse
#add the numbers then print
number = 123456
print("Original number:", number)
print("Reversed number:", reverse_digits(number))