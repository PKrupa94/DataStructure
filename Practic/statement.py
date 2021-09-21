# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'

for word in st.split():
    if word[0] == 's':
        print(word)

# Use range() to print all the even numbers from 0 to 10.
for i in range(0, 10, 2):
    print(i)
# return in form of list
print(list(range(0, 10, 2)))

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print([num for num in range(1, 50) if num % 3 == 0])


# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print('even!')

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
print([num[0] for num in st.split()])
