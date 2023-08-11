# To perform the exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying the concepts of list comprehension to start solidifying them for the future. They can be very useful in your professional practice!

# For the following list of temperatures in Fahrenheit, express these same values in a new list of temperature values in Celsius. The conversion between types of units is as follows:

# °C = (°F - 32) * (5/9)

# or expressed in another way:

# (degrees_fahrenheit-32)*(5/9)

# The temperature list is as follows:

# temperature_fahrenheit = [32, 212, 275]
# Store this new list in a variable called degrees_celsius

temperature_fahrenheit = [32, 212, 275]
 
degrees_celsius = [(temperature-32)*(5/9) for temperature in temperature_fahrenheit]
print(degrees_celsius)