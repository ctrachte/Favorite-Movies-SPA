def read_text():
	quotes = open("C:\Users\Caleb\Desktop\UDACITY\Python\Misc\profanity editor\profanity_test.txt")
	contents = quotes.read()
	number_of_words = len(contents)
	print("Number of characters in file = " + str(number_of_words))
	print(contents)

read_text()