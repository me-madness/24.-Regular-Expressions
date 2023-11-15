# First task from the lecture

import re

names = input()
valid_names = "\b[A-Z][a-z]+ [A-Z][a-z]+\b"
matches = re.findall(valid_names names)
print(" ".join(matches))

# Second task from me

