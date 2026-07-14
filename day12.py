# Check if a number is prime using a loop.
num = int(input("Enter: "))
print("prime" if num % 2 != 0 else "Not prime")


# using loop
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


# Print all prime numbers between 1 and 100.
for i in range(0, 100):
    if i % 2 != 0:
        print(i)

# Use break to stop a loop as soon as a number greater than 50 is found in a range.
for i in range(100):
    if i < 50:
        print(f"Found number greater than 50: {i}")
        break
    print(i)


# Use continue to print all numbers from 1 to 20 except multiples of 3.
for i in range(21):
    if i % 3 == 0:
        continue
    print(i)

# loops finshed

# Section 5: Strings (Q41–52)
# 41. Take a string and print its length using len() .
name = input("Enter name: ")
print(len(name))


# 42. Reverse a string using slicing.

name = "VIRAT KOHLI"
rev_name = name[::-1]
print(rev_name)


# 43. Check if a string is a palindrome.
name = input("Enter: ")
reversed = name[::-1]
print("its palidrome" if name == reversed else "not palidrome")


# 44. Count the number of vowels in a string.

name = input("Enter:")
vowels = "aeiouAEIOU"
count = 0
for letter in name:
    if letter in vowels:
        count += 1
print(f"Number of vowels: {count}")

# 45. Convert a string to uppercase and lowercase using built-in methods.
name = "ROHITH SHARMA"
print(upper := name.lower())

name = "ROHITH SHARMA"
print(upper := name.upper())


# 46. Check if a string starts with "Py" and ends with "on" using .startswith() and
# .endswith() .

name = "python"
print(name.startswith("py"))

photo = "Img.jpg"
print(photo.endswith("jpg"))

# 47. Replace all occurrences of a character in a string using .replace() .
name = "Abhishek sharma is a odi opener"
print(replacing := name.replace("Abhishek ", "Rohith"))


# 48. Split a sentence into a list of words using .split() , then join them back with a
# hyphen using .join() .
sentence = "Kohli is king"
print(answer := sentence.split())

sent = " "
print(answer := sent.join(sentence))
"ಸೆಂಟ್ ನಾ ಜೋಯಿನ್ ಮಾಡು ಸೆಂಟೆಕ್ನೆ ಅಲ್ಲಿ"

# 49. Count the occurrences of a specific word in a sentence.

name = "Arun shergill"
special_let = "Ll"
count = 0
for letter in name:
    if letter in special_let:
        count += 1
print(count)

# 50. Remove all whitespace from the beginning and end of a string using .strip() .

print(name := " Goutham ghambir ", name2 := name.strip())


# 51. Check if a string contains only digits, only alphabets, or is alphanumeric using
# .isdigit() , .isalpha() , .isalnum() .

print("12345".isdigit())  # True (All numbers)
print("123a5".isdigit())  # False (Has a letter 'a')
print("12 3".isdigit())  # False (Has a space)


print("Hello".isalpha())  # True (All letters)
print("Hello1".isalpha())  # False (Has a number '1')
print("Hi There".isalpha())  # False (Has a space)

print("Password123".isalnum())  # True (Letters + Numbers)
print("ABC".isalnum())  # True (Just letters is okay)
print("999".isalnum())  # True (Just numbers is okay)
print("User@1".isalnum())  # False (The '@' symbol is not allowed)


# 52. Take a full name as input and print the initials (e.g., "John Ronald Reuel" → "J.R.R").

name = input("Enter: ")
dot = "."
print(extra_name := dot.join(name))
