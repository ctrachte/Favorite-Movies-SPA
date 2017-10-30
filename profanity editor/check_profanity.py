import urllib

def read_text():
	quotes = open("C:\Users\Caleb\Desktop\UDACITY\Python\Misc\profanity editor\profanity_test.txt")
	contents = quotes.read()
	number_of_words = len(contents)
	print("Number of characters in file = " + str(number_of_words))
	print(contents)
	quotes.close()
	check_profanity(contents)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output = connection.read()
	if output:
		print "--This text contains profanity.--"
	elif not output:
		print "--This text does not contain profanity.--"
	else:
		"!!!!Error reading text!!!!"
	connection.close()
read_text()