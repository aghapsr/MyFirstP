numbers = []
for i in range(5):
    num = float(input("Enter a number: "))
    numbers.append(num)
    
total = 0
for num in numbers:
    total = total + num
    
avarage = total / len(numbers)

maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num


print(f"sum: {total}")
print(f"avarage: {avarage}")
print(f"maximum: {maximum}")