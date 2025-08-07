text = input("enter your text : ")

file1 = open('output.txt', 'w')
writing_file = file1.write(text)
print(writing_file)
file1.close()

file1 = open('output.txt', 'r')
reading_file = file1.read()
print(reading_file)
file1.close()

other = input('what do you want to append : ')

file1 = open('output.txt', 'a')
appending_file = file1.write(other)
print(appending_file)
file1.close()

file1 = open('output.txt', 'r')
reading_file2 = file1.read()
print(reading_file2)
file1.close()
