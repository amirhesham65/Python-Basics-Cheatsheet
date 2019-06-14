# Single line comment
''' Multiline 
    comments '''

# VARIABLES
name = "amir"
age = 17
gpa = 4.0
isTall = True

# PRINTING
print("Your name is: ", name)

# CASTING
print(int(gpa))
print(float(3))
print(str(True))
print(int("50") + int("70"))

# STRING
programmingLanguage = "python"
print(len(programmingLanguage))
print(programmingLanguage[0])
print(programmingLanguage[-1])
print(programmingLanguage.find("py"))
print(programmingLanguage[2:4])
print(programmingLanguage[2:])

# ARITHMETIC
print(6 + 5)
print(10 - 4)
print(2 * 3)
print(6 / 3)
print(2 ** 3)
print(10 % 3)
num = 10
num += 100
print(num)

# MATH
import math
print(pow(2, 3))
print(math.sqrt(144))
print(round(2.7))

# INPUT
name = input("Enter your name:")
print("Hello", name + "!")

# LISTS
colors = ["red", "green", "blue", "blue", "yellow"]
colors[1] = "cyan"
print(colors[1]) # same methods as the string on line 20
colors.append("purple")
colors.insert(1, "black")
colors.index("black")
colors.remove("black")
colors.count("blue")
colors.sort()
colors.clear()

# 2D LISTS
grid = [[1, 2], [3, 4]]
grid[0][1] = 5
print(grid[0][1])

# TUPLES
id = (1, 67, 4.5, "KOALA") # Same methods as lists

# FUNCTIONS
def addNumbers(num1, num2 = 99):
    return num1 + num2
sum = addNumbers(46)
print(sum)

# CONDITIONALS
if isTall and age == 17:
    print("Good!")
elif age < 20 and not(isTall):
    print("You are tall!")
else:
    print("Some thing else!")

# DICTIONARIES
grades = {
    "Amir": "A+",
    "Azoz": "A+",
    "Seif": "A+"
}
print(grades.get("Azoz", "No grades provided!"))

# LOOPS
index = 1
while index <= 5:
    print(index)
    index += 1

for index in range(5):
    print(index)

for color in colors:
    print(color)

# EXCEPTION CATCHING
try:
    num = 10/0
except ZeroDivisionError as e:
    print(e)
except:
    print("errrror!")

# OOB
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @property
    def title(self):
        print("Getting author...")
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @title.deleter
    def title(self):
        del self._title

    def readBook(self):
        print("Reading: " + self.title + " by " + self.author)

book1 = Book("Harry Potter", "JK Rowling")
book1.title = "The Half-Blood"
print(book1.title)
book1.readBook()

# Inheritance
class Story(Book):
    def __init__(self, title, author, rythm):
        self.rythm = rythm
        super().__init__(title, author)

    def sing(self):
        print("singing")

    def readBook(self):
        print("Reading a story")

myStory = Story("The red fox", "no-author", "LAY")
myStory.sing()

# IO
# Reading a text file
friendsFile = open('friends.txt', 'r')
print(friendsFile.readable())
print(friendsFile.read()) # readline(), readlines()
friendsFile.close()

# Appending to a text file
friendsFile = open('friends.txt', 'a')
friendsFile.write("\nSamir")
friendsFile.close()

# Writing to a text file
friendsFile = open('text.html', 'w')
friendsFile.write("<h1>This is test.html ;)</h1>")
friendsFile.close()

# Modules
import MyMathModule
print(MyMathModule.subTwoNumbers(100, 49))
