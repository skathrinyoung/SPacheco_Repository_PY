##Created by Savannah Pacheco on 11/26/2024

print("Hello, I hope you are having a wonderful today. Welcome to the temperature convertor. Please type if you would like to convert from 'Fahrenheit' or 'Celsius'.") ##Initial client-facing line
tempMeasurement = input() ##Client's input into if they will be presenting data as fahrenheit or as celsius 

##Code to switch from Fahrenheit to Celsius
if (tempMeasurement == "Fahrenheit"): ## If user inputs fahrenheit 
    print("Great! What whole number is the temperature you would like to convert?") ## Gets users to input the whole number they are looking to convert
    tempFahrenheit = input() ## Collects user's answer in the tempFahrenheit variable
    print("Wonderful, let me do some quick math to convert " + tempFahrenheit + "F to Celsius for you.") ## lets the user know what the computer is doing, acts as a confirmation that data was input correctly
    tempFahrenheit = int(tempFahrenheit) ## Changes the string to an integer, so that i can use numerical operations
    tempCelsius = ((tempFahrenheit - 32)*(5/9)) ## Formula to change F to C
    tempFahrenheit = str(tempFahrenheit) ## Stringifies fahrenheit for my last statement
    tempCelsius = str(tempCelsius) ##Stringifies celsius for my last statement
    print(tempFahrenheit + "F converted to Celsius is " + tempCelsius + "C.") ##Final calculation presented to the client
 

 ##Code to switch from Celsius to Fahrenheit
elif(tempMeasurement == "Celsius"): ## If user inputs celsius
    print("Great! What whole number is the temperature you would like to convert?") ## Gets users to input the whole number they are looking to convert
    tempCelsius = input() ## Collects user's answer in the tempCelsius variable
    print("Wonderful, let me do some quick math to convert " + tempCelsius + "C to Fahrenheit for you.") ## lets the user know what the computer is doing, acts as a confirmation that data was input correctly
    tempCelsius = int(tempCelsius) ## Changes string to integer
    tempFahrenheit = ((tempCelsius * 9/5) + 32) ## Calculates fahrenheit using the proper formula
    tempCelsius = str(tempCelsius) ##Converts Celsius variable back into a string
    tempFahrenheit = str(tempFahrenheit) ##COnverts Fahrenheit variable back into a string
    print(tempCelsius + "C converted to Fahrenheit is " + tempFahrenheit + "F.")
else:
    print("You may have had a typo, or did not capitalize correctly. Please try again.") ##Simple error message
