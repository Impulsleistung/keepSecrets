import random
import string

# Generate a string of 100 random characters
characters = string.ascii_letters + string.digits + string.punctuation
random_string = ''.join(random.choice(characters) for i in range(100))

# Write the string to a file
with open('pass.txt', 'w') as file:
    file.write(random_string)

# End of this file