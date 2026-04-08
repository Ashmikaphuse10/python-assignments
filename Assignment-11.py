#Opening the file and performing writing operation
file= open("example.txt","w")
file.write("\nThis is my first line")
file.write("\nThis is my second line")
print("The File written successfully")

#Opening the file and reading the file
file=open("example.txt","r")
contents=file.read()
print("\n*** The contents of the file are***")
print(contents)

#opening the file anf performing appending operation and closing the file
file=open("example.txt","a")
file.write("\nThis is the appended line")
file.close()
print("The file appended successfully")