#Data types

#String
print("Hello"[4])

print("hello" + " " + "world")

#Integer
print(123 + 345)

123_456_789

#Float
3.14159

#Boolean
True
False

# type() tells you what data is in it
type(123)
type("Hello!")

num_char = len(input("What is your name?"))

#Changes the data type from int -> str
new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")

#Dividing gives the answer as a float
print(6/2)

#Exponent is counted with **
print(2 ** 3)

#round() to get round floats right and after colon to tell by how many decimals
print(round(8 / 3, 2))

#add a number to previous value (or take away or divice with correct characters)
score = 0
score += 1
print(score)

#Combine different types of data into a string more easily
score = 0
height = 1.8
isWinning = True
#f-String
print(f"your score is {score}, your height is {height} you are winning is {isWinning}")
