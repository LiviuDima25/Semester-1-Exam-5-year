#### Describe each datatype below:(4 marks)

## 4         = integer
## 5.7       = float
## True      = boolean
## Good Luck = string

#### Which datatype would be useful for storing someone's height? (1 mark)
## Answer = Float

#### Which datatype would be useful for storing someone's hair colour?(1 mark)
## Answer = String


####Create a variable tha will store the users name.(1 mark) 

name = input("Enter Your Name: ")


####Create a print statement that will print the first 4 characters of the person's name.(3 marks)

print("Your first for letters are", name[0:4])

####Convert the user's name to all uppercase characters and print the result

namecaps = name.upper()
print (namecaps)



####Find out how many times the letter A occurs in the user's name

namecaps.count("A")



#### Create a conditional statement to ask a user to enter their age. If they are older than 18 they receive a message saying they can enter the competition, if they are under 18, they receive a message saying they cannot enter the competition.

age=int(input("Please enter your age: "))
if age<18:
  print ("You cannot enter this competition")
else:
  print ("You can enter this competition")
#### Create an empty list called squareNumbers (3 marks)

squareNumbers = []

#### Square numbers are the solutions to a number being multiplied by itself( example 1 is a square number because 1 X 1 = 1, 4 is a square number because 2 X 2 = 4 ). 
###Calculate the first 20 square numbers and put them in the list called squareNumbers. (With loop and .append 10 marks, without, Max 6 marks).

count=1
while count<21:
  num=count*count
  squareNumbers.append(num)
  count+=1

# ####Print your list (1 mark)
count=0
while count<20:
  print(squareNumbers[count])
  count+=1

####Create a variable called userSquare that asks the user for their favourite square number

userSquare=int(input("Type in your favourite Square Number: "))



#### Add this variable to the end of your list called SquareNumbers

squareNumbers.append(userSquare)

### Create a variable called choice. This variable should choose a random element from your list. Print the variable called choice.(3 marks)

choice=squareNumbers.randit()
print(choice)

####Create another print statement that prints tha following output: The random square number is: XX, where XX is where the random square number chosen by the computer.(4 marks)

print("The random square number is: ", choice)