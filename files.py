
out_file = open("name.txt", 'w')
name1 = input("Please enter your name: ")
out_file.write(name1)
out_file.close()

###

open_file = open("name.txt", "r")
name2 = open_file.read()
print("Your name is ", name2)
open_file.close()


###

open_file = open("numbers.txt", "r")
number1 = int(open_file.readline())
number2 = int(open_file.readline())
print(number1 + number2)
open_file.close()


###

open_file = open("numbers.txt", "r")
total = 0
for line in open_file:
    total += int(line)
print(total)
open_file.close()