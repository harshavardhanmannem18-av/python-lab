#	Write	a	program	that	imports	the	

import keyword

# Retrieve the list of all keywords for the current Python version
kw_list = keyword.kwlist

# Print the total number of keywords
print(f"Total number of keywords in Python {keyword.__name__}: {len(kw_list)}")

# Print the full list of keywords
print("\nFull list of Python keywords:")
print(kw_list)