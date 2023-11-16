# First task from the lecture

import re
data = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
matches = re.finditer(pattern, data)
for match in matches:
    print(match.group(), end="")
    

# Second task from me

