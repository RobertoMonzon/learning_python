# #To perform the exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying the concepts of list comprehension to start solidifying them for the future. They can be very useful in your professional practice!
# Creates a squared_values list made up of the numbers in the values squared.

# values = [1, 2, 3, 4, 5, 6, 9.5]

values = [1, 2, 3, 4, 5, 6, 9.5]
 
square_values = [value**2 for value in values]
print(square_values)