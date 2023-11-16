# First task from the lecture

import re

dates = input()
pattern = "\\b(?P<day>\\d{2})([-.\\/])(?P<month>[A-Z][a-z]{2})\\2(?P<year>\\d{4})\\b"
matches = re.findall(pattern, dates)
print(" ".join(matches))

# Second task from me

