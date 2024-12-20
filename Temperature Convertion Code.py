
tempMeasurement = input("Hello, I hope you are having a wonderful today. Welcome to the temperature convertor. Please type if you would like to convert from 'Fahrenheit' or 'Celsius'? ") ##Client's input into if they will be presenting data as fahrenheit or as celsius 

##Code to switch from Fahrenheit to Celsius
if (tempMeasurement == "Fahrenheit"): ## If user inputs fahrenheit 
    tempFahrenheit = input("Great! What is the temperature you would like to convert? ") ## Collects user's answer in the tempFahrenheit variable
    print("Wonderful, let me do some quick math to convert " + tempFahrenheit + "F to Celsius for you.") ## lets the user know what the computer is doing, acts as a confirmation that data was input correctly
    tempFahrenheit = float(tempFahrenheit) ## Changes the string to floating, so that I can use numerical operations
    tempCelsius = ((tempFahrenheit - 32)*(5/9)) ## Formula to change F to C
    tempFahrenheit = str(tempFahrenheit) ## Stringifies fahrenheit for my last statement
    tempCelsius = str(tempCelsius) ##Stringifies celsius for my last statement
    print(tempFahrenheit + "F converted to Celsius is " + tempCelsius + "C.") ##Final calculation presented to the client
 

 ##Code to switch from Celsius to Fahrenheit
elif(tempMeasurement == "Celsius"): ## If user inputs celsius
    tempCelsius = input("Great! What is the temperature you would like to convert? ") ## Collects user's answer in the tempCelsius variable
    print("Wonderful, let me do some quick math to convert " + tempCelsius + "C to Fahrenheit for you.") ## lets the user know what the computer is doing, acts as a confirmation that data was input correctly
    tempCelsius = float(tempCelsius) ##changes string to floating, so that I can use numerical operations
    tempFahrenheit = ((tempCelsius * 9/5) + 32) ##applies the formula to change celsius to fahrenheit
    tempCelsius = str(tempCelsius) ##Turns variable tempCelsius into a string
    tempFahrenheit = str(tempFahrenheit) ##turns variable tempFahrenheit into a string
    print(tempCelsius + "C converted to Fahrenheit is " + tempFahrenheit + "F.") ##prints final statement
else:
    print("You may have had a typo, or did not capitalize correctly. Please try again.") #basic error message
