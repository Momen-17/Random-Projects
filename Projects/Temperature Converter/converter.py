while True:
    # Ask user to choose conversion direction
    try:
        option = int(input('Convert to Fahrenheit (1) or Convert to Celsius (2): '))
    except ValueError:
        print('Invalid input. Please enter a number: 1 or 2.')
        continue
    if option not in [1, 2]:
        print('Please input either 1 or 2.')
    else:
        break

while True:
    # Ask user to enter a temperature
    try:
        temperature = float(input('Temperature: '))
        break
    except ValueError:
        print('Invalid input. Please enter a valid number.')

# Convert based on the chosen option
if option == 1:
    # Celsius to Fahrenheit
    result = round(temperature * 9 / 5 + 32, 2)
    print(f'{temperature} Celsius = {result} Fahrenheit')
else:
    # Fahrenheit to Celsius
    result = round((temperature - 32) * 5 / 9, 2)
    print(f'{temperature} Fahrenheit = {result} Celsius')
