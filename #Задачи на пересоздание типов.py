#Задачи на пересоздание типов
#1
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

whole_sum = int(num1) + int(num2)
fraction_sum = (num1 % 1) + (num2 % 1)

print(f"Sum of whole parts: {whole_sum}")
print(f"Sum of fractional parts: {fraction_sum}")

#2
amount = int(input("Enter the amount in UAH: "))
hryvnia = int(amount)
kopeyki = int(round((amount % 1) * 100))

print(f"{hryvnia} UAH {kopeyki} kopeyki")

#3
weight = int(input("Enter the weight in tonnes: "))
tonnes = int(weight)
kilograms = int((weight % 1) * 1000)
grams = int(round(((weight % 1) * 1000 % 1) * 1000))

print(f"{tonnes}t {kilograms}kg {grams}g")

#4
seconds = int(input("Enter time in seconds: "))
days = seconds // 86400
seconds %= 86400
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

#5
file_size = int(input("Enter the file size in GB: "))
connection_speed = int(input("Enter the internet speed in Mbps: "))

file_size_mb = file_size * 1024 * 8
download_time = file_size_mb / connection_speed

print(f"Download time: {download_time} seconds")

#If-else, if-elif-else
#1
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

print(f"The smallest number is: {min(num1, num2, num3)}")

#2
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#3
integer = int(input("Enter an integer (up to 4 digits): "))
print(f"The number has {len(str(abs(integer)))} digits.")

#4
top_left_x = float(input("Enter the top-left x coordinate: "))
top_left_y = float(input("Enter the top-left y coordinate: "))
bottom_right_x = float(input("Enter the bottom-right x coordinate: "))
bottom_right_y = float(input("Enter the bottom-right y coordinate: "))
x = float(input("Enter the x coordinate of the point: "))
y = float(input("Enter the y coordinate of the point: "))

if top_left_x <= x <= bottom_right_x and bottom_right_y <= y <= top_left_y:
    print("The point is inside the rectangle.")
else:
    print("The point is outside the rectangle.")

#Match-case
#1
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Remainder of division")

operation = int(input("\nEnter the operation number (1-5): "))

if operation == 1:
    print(f"Result: {num1 + num2}")
elif operation == 2:
    print(f"Result: {num1 - num2}")
elif operation == 3:
    print(f"Result: {num1 * num2}")
elif operation == 4:
    if num2 == 0:
        print("Error: cannot divide by 0!")
    else:
        print(f"Result: {num1 / num2}")
elif operation == 5:
    if num2 == 0:
        print("Error: cannot divide by 0!")
    else:
        print(f"Result: {num1 % num2}")
else:
    print("Invalid operation choice!")

#Тернарный оператор
#1
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#2
num = int(input("Enter a number: "))
if 0 <= num <= 100:
    print("The number is within the range of 0 to 100.")
else:
    print("The number is not within the range of 0 to 100.")

#3
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
    print("The number is divisible by 3, 5, and 7 simultaneously.")
else:
    print("The number is not divisible by 3, 5, and 7 simultaneously.")

#Случайные числа
#1
import random
def molfar_3000():
    responses = [
        "Yes, of course!",
        "No, not right now.",
        "Maybe in the future.",
        "Be patient.",
        "Everything will be fine!",
        "I'm not sure about that."
    ]
    
    input("Ask Molfar-3000 any question: ")
    answer = random.choice(responses) 
    print(f"Molfar-3000 says: {answer}")

molfar_3000()