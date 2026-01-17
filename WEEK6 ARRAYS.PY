import random

numbers = []
for i in range(20):
    numbers.append(random.randint(1, 100))
    
    print(numbers)

odd_numbers = []
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

        print("Even numbers:", even_numbers)
        print("Odd numbers:", odd_numbers)