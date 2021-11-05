N = int(input("Enter a number > "))
while N < 1:
    N = int(input("The number must be at least 1. Enter a number > "))

sum_of_odd_numbers = 0
sum_of_even_numbers = 0
number_of_even_numbers = 0

for num in range(1, N + 1):
    if num % 2 == 0: #even
        sum_of_even_numbers += num
        number_of_even_numbers += 1
    else:
        sum_of_odd_numbers += num

print ("The sum of odd numbers is", sum_of_odd_numbers)
print ("The average of even numbers is", sum_of_even_numbers/number_of_even_numbers)