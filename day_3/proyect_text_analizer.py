# Ask the user to write a paragraph.
# Ask the user to type three letters.
# Write a code to say the following:
# -How many times the letters he chose appear in the text.
# -print how many words there are in total
# -first and last letter
# - iverse the text and print it
# -confirm or deny if the word "python" is in the text
text=input("Please write a paragraph ")
l1=input("Please type the first letter what you are looking for in the text ")
l2=input("Please type the second letter what you are looking for in the text ")
l3=input("Please type the third letter what you are looking for in the text ")
text_lower=text.lower()

task1_l1=text.count(l1)
task1_l2=text.count(l2)
task1_l3=text.count(l3)


list_of_letters=list(text_lower)
list_of_words=text_lower.split(" ")

first_letter=(list(list_of_letters)[0])
last_letter=(list(list_of_letters)[-1])

quantity_words=len(list_of_words)
inverted_text= text_lower[::-1]
search_python= "python" in text_lower
dic={True:"is", False:"ins't"}



print(f"The letter {l1} appears in the text {task1_l1} times, the letter {l2} appears in the text {task1_l2} times and the letter {l3} appears in the text {task1_l3} times")
print(f"There is {quantity_words} words in the text")
print(f"The first letter in the text is {first_letter} and the last one is {last_letter}")
print(f"The inverted text says: {inverted_text}")
print(f"The word 'Python' {dic[search_python]} in the text")












