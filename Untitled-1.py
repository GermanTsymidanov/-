#Базовые операции
#1
a = int(input("Type first number:"))
b = int(input("Type second number:"))

sum = a + b
difference = a - b
prod = a * b

print(f"Sum: {sum}")
print(f"Difference: {difference}")
print(f"Product: {prod}")

#2
number = int(input("Type the random number: "))
percentage = int(input("Type the percentage for the random number: "))

calculations = (number * percentage) / 100

print(f"{percentage}% from {number} is equal to {calculations}")

#3
length = int(input("Give me length of wished rectangle: "))
width = int(input("Give me width of wished rectangle: "))

area = length * width

print(f"Here is the area of a rectangle: {area}")

#4
celsius = int(input("Type your needed celcius to converte it in fahrenheit: "))

fahrenheit = (celsius * 9/5) + 32

print(f"Your fahrenheit is {fahrenheit}")

#Работа с числами и обчислением
#1
first_number = int(input("Type your first number: "))
second_number = int(input("Type your second number: "))
third_number = int(input("Type your third number: "))

mean = (first_number + second_number + third_number) / 3

print(f"Here is your mean number that you are looking for: {mean}")

#2
base = int(input("Give me a base number: "))
power = int(input("Give me a power number: "))

result = base ** power

print(f"Get the result: {result}")

#3
import math
radius = int(input("Enter the radius of a circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Area of a circle is {area}")
print(f"Circumference of a circle is {circumference}")

#4
uah_usd = int(input("Welcome to UAH bank. Type the amount of money you want to transit to usd(United States Dollar): "))
uah_euro = int(input("Type the amounth of money you want to transit to euro: "))
uah_bitcoin = int(input("Type the amounth of money you want to transit to bitcoin: "))

usd = uah_usd * 0.024
euro = uah_euro * 0.023
bitcoin = uah_bitcoin * 0.00000025000

print(f"For usd you will get: {usd}")
print(f"For euro you will get: {euro}")
print(f"For bitcoin you will get: {bitcoin}")

#5
kilometres = int(input("Type the needed number of kilometres: "))

mile = kilometres / 1.609
nautical_mile = kilometres / 1.852

print(f"I translated your amount of kilometres to miles and nautical miles and that's what I got: miles are {mile} and nautica miles are {nautical_mile}")

#6.1
a = int(input("Type value of a: "))
b = int(input("Type value of b: "))

temp = a
a = b
b = temp

print(f"After change: a = {a}, b = {b}")

#6.2
a = int(input("Type value of a: "))
b = int(input("Type value of b: "))

a, b = b, a

print(f"After change: a = {a}, b = {b}")

#Работа с числами и порядками
#2
num = input("Type four-digit number: ")

sum_result = int(num[0]) + int(num[2])
diff_result = int(num[1]) - int(num[3])

print(f"Sum of first and third part is {sum_result}. Difference between second and fourth part is {diff_result}")

#3
num = input("Type three-digit number: ")

result = num[0] + num[2]

print(f"Number after deleting the middle part: {result}")

#6
number = input("Type three-digital number: ")

reversed_number = number[::-1]

print("Reversed number is:", reversed_number)

#Сложные задачи с оброботкой данных
#1
planet_masses = {
    "Mercury": 3.30e23,
    "Venus": 4.87e24,
    "Earth": 5.97e24,
    "Mars": 6.42e23,
    "Jupiter": 1.90e27,
    "Saturn": 5.68e26,
    "Uranus": 8.68e25,
    "Neptune": 1.02e26
}

total_mass = sum(planet_masses.values())

average_mass = total_mass / len(planet_masses)

planet_percentages = {planet: (mass / total_mass) * 100 for planet, mass in planet_masses.items()}

largest_planet = max(planet_masses, key=planet_masses.get)
largest_planet_mass = planet_masses[largest_planet]

other_planets_mass = total_mass - largest_planet_mass
mass_ratio = largest_planet_mass / other_planets_mass

print(f"Total mass of all planets in the Solar System: {total_mass:.2e} kg")
print(f"Average mass of planets: {average_mass:.2e} kg")
print("\nMass of each planet as a percentage of the total mass:")
for planet, percentage in planet_percentages.items():
    print(f"{planet}: {percentage:.2f}%")

print(f"\nThe largest planet: {largest_planet}")
print(f"Mass of the largest planet: {largest_planet_mass:.2e} kg")
print(f"The mass of the largest planet is {mass_ratio:.2f} times greater than the sum of the masses of all other planets.")
