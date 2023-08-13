# Create a generator that subtracts the lives of a video game character one by one, and returns a message each time it is called:

# "You have 3 lives left"

# "You have 2 lives left"

# "You have 1 life left"

# "Game Over"

# Store the generator in the lose_life variable

def message():
     x = "You have 3 lives left"
     yield print(x)
    
     x = "You have 2 lives left"
     yield print(x)
 
     x = "You have 1 life left"
     yield print(x)
    
     x = "Game Over"
     yield print(x)
 
[_ for _ in message()]