# Creates a dictionary called my_dictionary, for which, when a searched keyword is not found, 
# it is loaded with the string "Value not found".

# Load the dictionary with at least the following data pair:

# keyword = age

# value = 44

# It uses the defaultdict method of the Collections module.

from collections import defaultdict
 
my_dictionary = defaultdict(lambda:"Value not found")
my_dictionary["age"] = 44