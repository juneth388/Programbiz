import re

pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
	print("Match")
else:
	print("No match")

# Metacharacters are characters that are interpreted in a special way by a RegEx engine. 
# [] . ^ $ * + ? {} () \ |

# [] - Square brackets specifies a set of characters you wish to match.
# You can also specify a range of characters using - inside square brackets. [1-9], [a-e]
# [^abc] means any character except a or b or c.


# . - Period matches any single character (except newline '\n')


# ^ - Caret symbol ^ is used to check if a string starts with a certain character. ^a


# $ - Dollar symbol $ is used to check if a string ends with a certain character. a$


# * - Star symbol * matches zero or more occurrences of the pattern left to it.

# ma*n
# mn - 1 match
# maaan - 1 match
# main - No match (a is not followed by n)


# + - Plus symbol + matches one or more occurrences of the pattern left to it.

# ma+n
# mn - No match (no a character)
# maaan - 1 match
# main - No match (a is not followed by n)
# woman - 1 match


# ? - Question Mark symbol ? matches zero or one occurrence of the pattern left to it.

# ma?n
# mn - 1 match
# maaan - No match (more than one a character)
# main - No match (a is not followed by n)
# woman - 1 match


# {} - Braces Consider this code: {n,m}. This means at least n, and at most m repetitions of the pattern left to it.

# a{2,3}
# abc dat - No match
# abc daat - 1 match (at daat)
# aabc daaat - 2 matches (at aabc and daaat)


# | - Alternation Vertical bar | is used for alternation (or operator).

# a|b
# cde - No match
# ade - 1 match (match at ade)
# acdbea - 3 matches (at acdbea)


# () - Group Parentheses () is used to group sub-patterns. 
# For example, (a|b|c)xz match any string that matches either a or b or c followed by xz


# \ - Backslash \ is used to escape various characters including all metacharacters.



# Special Sequences
# \d - Matches any decimal digit. Equivalent to [0-9]

# \D - Matches any non-decimal digit. Equivalent to [^0-9]

# \s - Matches where a string contains any whitespace character. Equivalent to [ \t\n\r\f\v].

# \S - Matches where a string contains any non-whitespace character. Equivalent to [^ \t\n\r\f\v].

# \w - Matches any alphanumeric character (digits and alphabets). Equivalent to [a-zA-Z0-9_]. 
# By the way, underscore _ is also considered an alphanumeric character.

# \W - Matches any non-alphanumeric character. Equivalent to [^a-zA-Z0-9_]

# \Z - Matches if the specified characters are at the end of a string. \A , \b, \B


# If the pattern is not found, re.split() returns a list containing the original string.
import re

string = 'Twelve:12 Eighty nine:89. 12'
pattern = '\d+'

result = re.split(pattern, string) 
print(result)

# Output: ['Twelve:', ' Eighty nine:', '.']


# re.findall()  method returns a list of strings containing all matches.
# re.split() method splits the string where there is a match and returns a list of strings where the splits have occurred.
# re.sub()
# re.sub(pattern, replace, string)The method returns a string where matched occurrences are replaced with the content of replace variable.
# re.subn()
# re.search()

# # Three digit number followed by space followed by two digit number
# pattern = '(\d{3}) (\d{2})'


# Program to remove all whitespaces
import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.sub(pattern, replace, string) 
print(new_string)

# Output: abc12de23f456

# When r or R prefix is used before a regular expression, it means raw string.

import re

string = '\n and \r are escape sequences.'

result = re.findall(r'[\n\r]', string) 
print(result)

# Output: ['\n', '\r']
