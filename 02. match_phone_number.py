# First task from the lecture

import re

phone_number = input()
phone_number_regex = "(\+359-2-[0-9]{3}-[0-9]{4}\\b|\+359 2 [0-9]{3} [0-9]{4}\\b)"
matches = re.findall(phone_number_regex, phone_number)
print(" ".join(matches)) 

# Second task from me

