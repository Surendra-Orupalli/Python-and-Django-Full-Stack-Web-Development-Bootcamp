import re

# Example-1
patterns = ['term1', 'term2']

text = "This is a string with term1, and not the other!"

for pattern in patterns:
    print("I am searching for: " + pattern)

    if re.search(pattern, text):
        print("MATCH!")
    else:
        print("NO MATCH!")


# Example-2
split_term = '@'
email = 'user@gmail.com'
print(re.split(split_term,email))


# Example-3
print(re.findall('match', 'test pharse match in match middle'))


# Helper function
def multi_re_find(patterns,phrase):

    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

test_phrase = "sdsd..sssddd..sdddsddd....dsds...dssssss...sddddd"

# s followed by zero or more d
test_pattern = ['sd*']
multi_re_find(test_pattern, test_phrase)

# s follwed by one or more d
test_pattern = ['sd+']
multi_re_find(test_pattern, test_phrase)

# s followed by zero or one d
test_pattern = ['sd?']
multi_re_find(test_pattern, test_phrase)

# s followed by two d
test_pattern = ['sd{3}']
multi_re_find(test_pattern, test_phrase)

# s followed by one or three d
test_pattern = ['sd{1,3}']
multi_re_find(test_pattern, test_phrase)

# s followed by one or more s, one or more d
test_pattern = ['s[s,d]+']
multi_re_find(test_pattern, test_phrase)


# Excluding special characters by using ^
test_phrase = "This is a string! But it has a punctuation. How can we remove it?"
test_pattern = ['[^!.?]+']
multi_re_find(test_pattern, test_phrase)

# Getting sequences for lower case letters
test_phrase = "This is a string! But it has a punctuation. How can we remove it?"
test_pattern = ['[a-z]+']
multi_re_find(test_pattern, test_phrase)

# Getting sequences for upper case letters
test_phrase = "This is a string! But it has a punctuation. How can we remove it?"
test_pattern = ['[A-Z]+']
multi_re_find(test_pattern, test_phrase)

# Getting sequences of digits using r'\
test_phrase = "This is a string with numbers 12312 and a symbol #hashtag"
test_pattern = [r'\d+']
multi_re_find(test_pattern, test_phrase)

# Getting sequences of non digits r'\
test_phrase = "This is a string with numbers 12312 and a symbol #hashtag"
test_pattern = [r'\D+']
multi_re_find(test_pattern, test_phrase)

# Getting sequences of white spaces r'\
test_phrase = "This is a string with numbers 12312 and a symbol #hashtag"
test_pattern = [r'\s+']
multi_re_find(test_pattern, test_phrase)

# Getting sequences of non white spaces r'\
test_phrase = "This is a string with numbers 12312 and a symbol #hashtag"
test_pattern = [r'\S+']
multi_re_find(test_pattern, test_phrase)

# Getting sequences of alpha-numeric r'\
test_phrase = "This is a string with numbers 12312 and a symbol #hashtag"
test_pattern = [r'\w+']
multi_re_find(test_pattern, test_phrase)


# Getting sequences of non alpha-numeric r'\
test_phrase = "This is a string with numbers 12312 and a symbol #hashtag"
test_pattern = [r'\W+']
multi_re_find(test_pattern, test_phrase)
