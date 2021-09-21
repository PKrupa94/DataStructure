myFile = open('test.txt')
print(myFile.read())
print(myFile.read())  # it will print noting

# once you read file your cursor goes to end of the file to read file again you need to reset the cursor
myFile.seek(0)
print(myFile.read())
myFile.seek(0)

# read file as a list of new lines
print(myFile.readlines())
#output: ['Hello,This is a text file\n', 'This is second line\n', 'This is third line']

# close file
myFile.close()

# when you don't need to handle close file manually use below

with open('test.txt') as new_file:
    context = new_file.readlines()
    print(context)


# append new line to file
with open('text.txt', mode='a') as new_file:
    new_file.write('\nThis is Fourth line')

with open('text.txt', mode='r') as new_file:
    print(new_file.read())
