import os

def rename_files():
	file_list = os.listdir(r"C:\Users\Caleb\Desktop\UDACITY\Python\Misc\secret_message\message")
	saved_path = os.getcwd()
	os.chdir(r"C:\Users\Caleb\Desktop\UDACITY\Python\Misc\secret_message\message")
	for file in file_list:
		file = os.rename(file, file.translate(None, "0123456789"))
		print file
	os.chdir(saved_path)

rename_files()