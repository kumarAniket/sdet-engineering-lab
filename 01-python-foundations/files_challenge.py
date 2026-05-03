# Writing to a txt file
with open('file_challenge.txt', mode='w') as file:
    file.write("This is my SDET Journey\n")
    file.write("Preparing for MAANG\n")
    file.write("90 Days Exit Hackathon....")

print("Lines written to file!!!")
print()
print("Reading the lines from the file:\n")

# Appending to the file
with open('file_challenge.txt',mode='a') as appendFile:
    appendFile.write("\nThis is the last line")

# Reading from the txt file
with open('file_challenge.txt',mode='r') as readFile:
    for line in readFile:
        print(line)