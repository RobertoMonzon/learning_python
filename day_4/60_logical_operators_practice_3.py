# Checks if the words stored in the following variables:
# word1 = "success", and
# word2 = "technology"
# are not found in the sentence below, and stores the result of this check (a boolean) in a variable called my_bool:
# "When something is important enough, you do it even if the odds are not with you"

word1="success"
word2="techonolgy"

text="When something is important enough, you do it even if the odds are not with you"
my_bool= word1 and word2 not in text
print(my_bool)
