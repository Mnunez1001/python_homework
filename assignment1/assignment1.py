# Task #1
#A function that returns the string "Hello!" when called.

def hello():
    return "Hello!"

print("==========Task 1==========")
print(hello()) 

# Task 2: Write a greet function that takes one argument, a name, and returns Hello, <name>!. 
#  Again, what matters here is what the function returns.

def greet(name):
    return f"Hello, {name}!"

print("==========Task 2==========")
print(f"\n{greet('Alex')}")

#Task 3: Calculator, Using a Match Statement
#Create a function called calc. It takes three parameters, two numbers and an operation.

def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return "Invalid operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
print("==========Task 3==========")
print(f"\n{calc(5, 6)}")
print(f"\n{calc(5, 6, 'add')}")
print(f"\n{calc(20, 5, 'divide')}")
print(f"\n{calc(14, 2.0, 'multiply')}")
print(f"\n{calc(12.6, 4.4, 'subtract')}")
print(f"\n{calc(9, 5, 'modulo')}")
print(f"\n{calc(10, 0, 'divide')}")
print(f"\n{calc(2, 3, 'power')}")
print(f"\n{calc('first', 'second', 'multiply')}")
print(f"\n{calc(10, 3, 'int_divide')}")

#Task 4: Data Type Conversion
#Create a function called data_type_conversion. It takes two parameters, a value and a data type. 
# The function converts the value to the data type specified and returns the result.

def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "float":
                return float(value)
            case "str":
                return str(value)
            case "int":
                return int(value)
            case _:
                return "Invalid data type"
    except ValueError:
        return f"You can't convert {value} into a {data_type}."

print("==========Task 4==========")
print(f"\n{data_type_conversion('110', 'int')}")
print(f"\n{data_type_conversion('5.5', 'float')}")
print(f"\n{data_type_conversion('nonsense', 'float')}")
print(f"\n{data_type_conversion(7, 'str')}")
print(f"\n{data_type_conversion('banna', 'int')}")

#Task 5: Grade, Using *args
#Create a function called grade. It takes an arbitrary number of arguments, which are the scores
def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."

print("==========Task 5==========")
print(f"\n{grade(75, 85, 95)}")
print(f"\n{grade('two', 'wide', 'dog')}")

#Task 6: Repeat, Using a Loop
#Create a function called repeat. It takes two parameters, a string and a count.

def repeat(string, count):
    result = ""
    for i in range(count):
        result += string
    return result

print("==========Task 6==========")
print(f"\n{repeat('hello,', 3)}")

#Task 7: Student Scores, Using **kwargs
#Create a function called student_scores. It takes one parameter, a mode, and an arbitrary number of keyword arguments,
#  which are the names and scores of students.
def student_scores(mode, **kwargs):
    if mode == "best":
        return max(kwargs, key=kwargs.get)
    elif mode == "mean":
        return sum(kwargs.values()) / len(kwargs)
    else:
        return "Invalid mode"

print("==========Task 7==========")
print(f"\n{student_scores('best', Alex=85, Michelle=90, Allison=75)}")
print(f"\n{student_scores('mean', Alex=85, Michelle=90, Allison=75)}")

#Task 8: Titleize, Using String Operations
#Create a function called titleize. It takes one parameter, a string.

def titleize(title):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = title.split()
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()
    return ' '.join(words)

print("==========Task 8==========")
print(f"\n{titleize('cheese and crackers')}")
print(f"\n{titleize('more cake and ice cream')}")
print(f"\n{titleize('after the rain')}")

#Task 9: Hangman, with String Operations
#Create a function called hangman. It takes two parameters, a secret word and a string.

def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

print("==========Task 9==========")
print(f"\n{hangman('Massachusetts', 'as')}")
print(f"\n{hangman('Mississippi', 'is')}")

#Task 10: Pig Latin
#Create a function called pig_latin. It takes one parameter, a string.

def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    pig_latin_words = []

    for word in words:
        if word[0] in vowels:
            pig_latin_word = word + "ay"
        else:
            consonant_cluster = ""

            while len(word) > 0 and word[0] not in vowels:
                if word.startswith("qu"):
                    consonant_cluster += "qu"
                    word = word[2:]
                else:
                    consonant_cluster += word[0]
                    word = word[1:]

            pig_latin_word = word + consonant_cluster + "ay"

        pig_latin_words.append(pig_latin_word)

    return " ".join(pig_latin_words)

print("==========Task 10==========")
print(f"\n{pig_latin('alex')}")
print(f"\n{pig_latin('big')}")
print(f"\n{pig_latin('cat')}")
print(f"\n{pig_latin('quiet in the corner')}")
print(f"\n{pig_latin('square')}")