import random
import string

key_len = 50

# Generate a string of 100 random characters
characters = string.ascii_letters + string.digits + string.punctuation
random_string = ''.join(random.choice(characters) for i in range(key_len))

# Write the string to a file
with open('howto_encrypt\pass.txt', 'w') as file:
    file.write(random_string)

# End of this file